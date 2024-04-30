#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include "math.h"
#include "pthread.h"

#define __DISC
#define __CLAMP
#define PI 3.14159265358979323846

typedef struct
{
    double *bd;
    const uint32_t I;
    const uint32_t N;
    const uint32_t Nx;
    const uint32_t Ny;
    const double xmin;
    const double xmax;
    const double ymin;
    const double ymax;
    const double width;
    const double height;
} Args;

void *compute_sym(void *__args)
{
    const Args *args = (Args *)__args;
    double *bd = args->bd;
    const uint32_t I = args->I;
    const uint32_t N = args->N;
    const uint32_t Nx = args->Nx;
    const uint32_t Ny = args->Ny;
    const double xmin = args->xmin;
    const double xmax = args->xmax;
    const double ymax = args->ymax;
    const double width = args->width;
    const double height = args->height;

    double *zr = malloc(N * sizeof(double));
    double *zi = malloc(N * sizeof(double));

    for (uint32_t i = 0; i < I; i++)
    {
#ifdef __DISC
        double r = rand() / (double)RAND_MAX;
        r = 2 * r * r; // bc circle with radius 2 and ^2 bc the density needs to be adjusted for (i think)
        double p = 2 * PI * rand() / (double)RAND_MAX;
        zr[0] = r * cos(p);
        zi[0] = r * sin(p);
#else
        zr[0] = xmin + (xmax - xmin) * rand() / (double)RAND_MAX;
        zi[0] = -ymax + (ymax - ymin) * rand() / (double)RAND_MAX;
#endif
        for (uint32_t n = 0; n < N - 1; n++)
        {
            uint32_t next_idx = (n + 1);

            zr[next_idx] = zr[n] * zr[n] - zi[n] * zi[n] + zr[0];
            zi[next_idx] = 2 * zr[n] * zi[n] + zi[0];

            if (zr[next_idx] * zr[next_idx] + zi[next_idx] * zi[next_idx] > 4)
            {
                for (; n > 0; n--)
                {
                    if (xmin <= zr[n] && zr[n] <= xmax && -ymax <= zi[n] && zi[n] <= ymax)
                    {
                        uint32_t x = ((zr[n] - xmin) / width + 0.5 / (double)Nx) * (Nx - 1); // implicit cast here
                        uint32_t y = ((zi[n] + ymax) / height + 0.5 / (double)Ny) * (Ny - 1);

                        bd[x + y * Nx]++;
                        bd[x + (Ny - y - 1) * Nx]++;
                    }
                }
                break;
            }
        }
    }
    free(zr);
    free(zi);

    return NULL;
}

void *compute_asym(void *__args)
{
    const Args *args = (Args *)__args;
    double *bd = args->bd;
    const uint32_t I = args->I;
    const uint32_t N = args->N;
    const uint32_t Nx = args->Nx;
    const uint32_t Ny = args->Ny;
    const double xmin = args->xmin;
    const double xmax = args->xmax;
    const double ymin = args->ymin;
    const double ymax = args->ymax;
    const double width = args->width;
    const double height = args->height;

    double *zr = malloc(N * sizeof(double));
    double *zi = malloc(N * sizeof(double));

    for (uint32_t i = 0; i < I; i++)
    {
#ifdef __DISC
        double r = rand() / (double)RAND_MAX;
        r = 2 * r * r; // bc circle with radius 2 and ^2 bc the density needs to be adjusted for (i think)
        double p = 2 * PI * rand() / (double)RAND_MAX;
        zr[0] = r * cos(p);
        zi[0] = r * sin(p);
#else
        zr[0] = xmin + (xmax - xmin) * rand() / (double)RAND_MAX;
        zi[0] = ymin + (ymax - ymin) * rand() / (double)RAND_MAX;
#endif
        for (uint32_t n = 0; n < N - 1; n++)
        {
            uint32_t next_idx = (n + 1);

            zr[next_idx] = zr[n] * zr[n] - zi[n] * zi[n] + zr[0];
            zi[next_idx] = 2 * zr[n] * zi[n] + zi[0];

            if (zr[next_idx] * zr[next_idx] + zi[next_idx] * zi[next_idx] > 4)
            {
                for (; n > 0; n--)
                {
                    if (xmin <= zr[n] && zr[n] <= xmax && ymin <= zi[n] && zi[n] <= ymax)
                    {
                        uint32_t x = ((zr[n] - xmin) / width + 0.5 / (double)Nx) * (Nx - 1); // implicit cast here
                        uint32_t y = ((zi[n] - ymin) / height + 0.5 / (double)Ny) * (Ny - 1);

                        bd[x + y * Nx]++;
                    }
                }
                break;
            }
        }
    }
    free(zr);
    free(zi);

    return NULL;
}

int main(int argc, char *argv[])
{
    const uint32_t Nx = 2400;
    const uint32_t Ny = 1600;
    const uint32_t I = Nx * Ny * 40;
    const uint32_t N = 1024;
    const uint32_t thread_cnt = 6;
    const uint8_t sym = 1;

    const double xmin = -2;
    const double xmax = 1;
    const double ymin = -1;
    const double ymax = 1;

    const double width = xmax - xmin;
    const double height = ymax - ymin;

    double *bd = malloc(Nx * Ny * sizeof(double));
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        bd[i] = 0;
    }

    pthread_t *threads = malloc(thread_cnt * sizeof(pthread_t));
    uint32_t large_threads = I % thread_cnt;
    Args large_args = {bd, I / thread_cnt + 1, N, Nx, Ny, xmin, xmax, ymin, ymax, width, height};
    for (uint32_t i = 0; i < large_threads; i++)
    {
        if (ymin == -ymax && sym == 1)
            pthread_create(threads + i, NULL, compute_sym, (void *)&large_args);
        else
            pthread_create(threads + i, NULL, compute_asym, (void *)&large_args);
    }

    uint32_t small_threads = thread_cnt - large_threads;
    Args small_args = {bd, I / thread_cnt, N, Nx, Ny, xmin, xmax, ymin, ymax, width, height};
    for (uint32_t i = large_threads; i < small_threads + large_threads; i++)
    {
        if (ymin == -ymax && sym == 1)
            pthread_create(threads + i, NULL, compute_sym, (void *)&small_args);
        else
            pthread_create(threads + i, NULL, compute_asym, (void *)&small_args);
    }

    for (uint32_t i = 0; i < thread_cnt; i++)
    {
        pthread_join(threads[i], NULL);
    }

#ifdef __ELIM_ZERO
    // the 0 point will always have an insanely high value bc of nan or smth, i dont fully understand
    if (xmin <= 0 && 0 <= xmax && ymin <= 0 && 0 <= ymax)
    {
        uint32_t x = (uint32_t)((-xmin / width + 0.5 / (double)Nx) * (Nx - 1));
        uint32_t y = (uint32_t)((-ymin / height + 0.5 / (double)Ny) * (Ny - 1));

        bd[x + y * Nx] = 1;
    }
#endif

    // find maximum
    double bd_max = bd[0];
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        bd_max = fmax(bd[i], bd_max);
    }
    printf("Computed maximum.\n");

// normalize brightness
#ifdef __CLAMP
    const double clamp_min = 0;
    const double clamp_max = 2 / 3. * bd_max;
#endif
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
#ifdef __CLAMP
        bd[i] = bd[i] < clamp_min ? clamp_min : bd[i];
        bd[i] = bd[i] > clamp_max ? clamp_max : bd[i];
        bd[i] = 255 * (bd[i] - clamp_min) / (clamp_max - clamp_min);
#else
        bd[nx + ny * Nx] = 255 * bd[nx + ny * Nx] / bd_max;
#endif
    }
    printf("Polished buddhabrot.\n");

    uint8_t *pic = malloc(Nx * Ny * sizeof(uint8_t));
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        pic[i] = (uint8_t)bd[i];
    }
    free(bd);

    FILE *f = fopen("out6.pgm", "w");
    fprintf(f, "P5\n%i %i %i\n", Nx, Ny, UINT8_MAX); // header
    fwrite(pic, Nx * Ny, 1, f);                      // data
    fclose(f);
    printf("Saved the file, enjoy :)\n");

    return 0;
}