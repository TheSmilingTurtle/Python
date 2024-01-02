#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include "math.h"
#include "pthread.h"
#include "unistd.h"
#include "time.h"

#define __DISC
#define __CLAMP
#define PI 3.14159265358979323846

struct Args
{
    double *bd;
    uint32_t *imp;
    uint32_t *i;
    uint32_t I;
    uint32_t N;
    uint32_t Nx;
    uint32_t Ny;
    double xmin;
    double xmax;
    double ymin;
    double ymax;
    double width;
    double height;
};

void *buddha_sym(void *__args)
{
    const struct Args *args = (struct Args *)__args;
    double *bd = args->bd; // so uhm, this is where the most concurrency concerns lie,
                           // bc different threads write to the same array and could increment
                           // to the same pixel and then the pixel may be incremented only by 1
                           // and not 2. but because there are so many pixels and samples
                           // and the chances of this happening are so small, idc.
    uint32_t *imp = args->imp;
    uint32_t *i = args->i;
    const uint32_t I = args->I;
    const uint32_t N = args->N;
    const uint32_t Nx = args->Nx;
    const uint32_t Ny = args->Ny;
    const double xmin = args->xmin;
    const double xmax = args->xmax;
    const double ymax = args->ymax;
    const double width = args->width;
    const double height = args->height;

    uint32_t nx;
    uint32_t ny;
    double *zr = malloc(N * sizeof(double)); // real part of the zn's
    double *zi = malloc(N * sizeof(double)); // imaginary part of the zn's
    double zr2;
    double zi2;
#ifdef __DISC
    double r;
    double p;
#endif
    for (; *i < I; (*i)++)
    {
#ifdef __DISC
        r = rand() / (double)RAND_MAX; // generate random points on the disc
        r = 0.25 + 1.75 * r * r;       // outer circle has radius 2, inner circle has radius 0.25. ^2 to reach "uniformity"
        p = 2 * PI * rand() / (double)RAND_MAX;
        zr[0] = r * cos(p); // and store them in the first values of z
        zi[0] = r * sin(p);
#endif
#ifdef __IMP
        uint32_t largest_nx = 0;
        uint32_t largest_ny = 0;
        uint32_t largest_val = rand() * imp[0]; //most likely 0, but like consistency or smth
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            for (uint32_t ny = 0; ny < Ny; ny++)
            {
                uint32_t tmp = rand() * imp[nx + ny * Nx];
                if (tmp > largest_val)
                {
                    largest_val = tmp;
                    largest_nx = nx;
                    largest_ny = ny;
                }
            }
        }
        zr[0] = xmin + width * (largest_nx / (double)(Nx - 1));
        zi[0] = -ymax + height * (largest_ny / (double)(Ny - 1));
#endif
#ifndef __DISC
#ifndef __IMP
        zr[0] = xmin + (xmax - xmin) * rand() / (double)RAND_MAX;
        zi[0] = -ymax + (2 * ymax) * rand() / (double)RAND_MAX;
#endif
#endif
        zr2 = zr[0] * zr[0]; // minor optimisation
        zi2 = zi[0] * zi[0];
        for (uint32_t n = 0; n < N - 1; n++)
        {
            uint32_t next_idx = (n + 1);

            zr[next_idx] = zr2 - zi2 + zr[0];               // real part of the mandelbrot
            zi[next_idx] = (zr[n] + zr[n]) * zi[n] + zi[0]; // immaginary part

            zr2 = zr[next_idx] * zr[next_idx];
            zi2 = zi[next_idx] * zi[next_idx];

            if (zr2 + zi2 > 4) // if it diverged
            {

                for (; n > 0; n--) // iterate backwards over z
                {
                    if (xmin <= zr[n] && zr[n] <= xmax && -ymax <= zi[n] && zi[n] <= ymax) // if its in the image to avoid segfaults etc.
                    {
                        nx = ((zr[n] - xmin) / width + 0.5 / (double)Nx) * (Nx - 1);  // find the pixel coordinates
                        ny = ((zi[n] + ymax) / height + 0.5 / (double)Ny) * (Ny - 1); // + 0.5 / Ny to avoid floating point errors
                                                                                      // these errors may otherwise lead to black
                                                                                      // stripes across the image. It is possible
                                                                                      // that is is no longer needed, but its not
                                                                                      // in the way and it is a good way to provide
                                                                                      // a litle robustness.

                        bd[nx + ny * Nx]++;            // nx + ny * Nx because bd is a 1d array and rows are just mapped offset
                        bd[nx + (Ny - ny - 1) * Nx]++; // symmetry
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

void *buddha_asym(void *__args) // barely used at all. its perfectly fine.
{
    const struct Args *args = (struct Args *)__args;
    double *bd = args->bd;
    uint32_t *imp = args->imp;
    uint32_t *i = args->i;
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

    uint32_t nx;
    uint32_t ny;
    double *zr = malloc(N * sizeof(double));
    double *zi = malloc(N * sizeof(double));
    double zr2;
    double zi2;
    double r;
    double p;

    for (; *i < I; (*i)++)
    {
#ifdef __DISC
        r = rand() / (double)RAND_MAX;
        r = 0.25 + 1.75 * r;
        p = 2 * PI * rand() / (double)RAND_MAX;
        zr[0] = r * cos(p);
        zi[0] = r * sin(p);
#else
        zr[0] = xmin + (xmax - xmin) * rand() / (double)RAND_MAX;
        zi[0] = ymin + (ymax - ymin) * rand() / (double)RAND_MAX;
#endif
        zr2 = zr[0] * zr[0];
        zi2 = zi[0] * zi[0];
        for (uint32_t n = 0; n < N - 1; n++)
        {
            uint32_t next_idx = (n + 1);

            zr[next_idx] = zr2 - zi2 + zr[0];
            zi[next_idx] = (zr[n] + zr[n]) * zi[n] + zi[0];

            zr2 = zr[next_idx] * zr[next_idx];
            zi2 = zi[next_idx] * zi[next_idx];

            if (zr2 + zi2 > 4)
            {
                for (; n > 0; n--)
                {
                    if (xmin <= zr[n] && zr[n] <= xmax && ymin <= zi[n] && zi[n] <= ymax)
                    {
                        nx = ((zr[n] - xmin) / width + 0.5 / (double)Nx) * (Nx - 1); // implicit cast here
                        ny = ((zi[n] - ymin) / height + 0.5 / (double)Ny) * (Ny - 1);

                        bd[nx + ny * Nx]++;
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
    const uint32_t Nx = 1200;
    const uint32_t Ny = 800;
    const uint32_t I = Nx * Ny; // total number of samples
    const uint32_t N = 1024;          // Max iterations for mandelbrot
    const uint32_t thread_cnt = 4;
    const uint8_t sym = 1; // bool for symmetry

    const double xmin = -2;
    const double xmax = 1;
    const double ymin = -1;
    const double ymax = 1;

    const double width = xmax - xmin;
    const double height = ymax - ymin;

    srand(time(NULL));

    uint32_t *imp = malloc(Nx * Ny * sizeof(uint32_t));
    for (uint32_t i = 0; i < Nx * Ny; i++)
    {
        imp[i] = 0;
    }

    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            double cr = xmin + width * (nx / (double)(Nx - 1));
            double ci = ymin + height * (ny / (double)(Ny - 1)); // this is technically upside down
            double zr = cr;
            double zi = ci;
            double zr2 = zr * zr;
            double zi2 = zi * zi;

            for (uint32_t n = 0; n < N; n++)
            {
                if (zr2 + zi2 > 4)
                {
                    imp[nx + ny * Nx] = n;
                    break;
                }
                zi = (zr + zr) * zi + ci;
                zr = zr2 - zi2 + cr;
                zr2 = zr * zr;
                zi2 = zi * zi;
            }
        }
    }

    printf("Calculating Buddhabrot. \n");

    double *bd = malloc(Nx * Ny * sizeof(double)); // create and initialize
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        bd[i] = 0;
    }

    pthread_t *threads = malloc(thread_cnt * sizeof(pthread_t));         // storing th thread ids
    struct Args *thread_args = malloc(thread_cnt * sizeof(struct Args)); // will store the different arguments to the threads
    uint32_t *trackers = malloc(thread_cnt * sizeof(uint32_t));          // it is no longer free software
    for (uint32_t i = 0; i < thread_cnt; i++)
    {
        trackers[i] = 0;
    }

    // split task (/total number of samples I) into large and small tasks
    // large tasks have 1 sample more than small ones.
    // and then generate function arguments
    // doing it any other way (like initializing the threads directly) results in bizzare errors
    uint32_t large_threads = I % thread_cnt;
    uint32_t large_work = I / thread_cnt + 1;
    for (uint32_t i = 0; i < large_threads; i++)
    {
        struct Args tmp = {bd, imp, trackers + i, large_work, N, Nx, Ny, xmin, xmax, ymin, ymax, width, height};
        thread_args[i] = tmp;
    }
    uint32_t small_threads = thread_cnt - large_threads;
    uint32_t small_work = I / thread_cnt;
    for (uint32_t i = large_threads; i < small_threads + large_threads; i++)
    {
        struct Args tmp = {bd, imp, trackers + i, small_work, N, Nx, Ny, xmin, xmax, ymin, ymax, width, height};
        thread_args[i] = tmp;
    }

    for (uint32_t i = 0; i < thread_cnt; i++) // initialize the threads
    {
        if (ymin == -ymax && sym == 1)
            pthread_create(threads + i, NULL, buddha_sym, (void *)&thread_args[i]);
        else
            pthread_create(threads + i, NULL, buddha_asym, (void *)&thread_args[i]);
    }

    uint32_t total;
    uint32_t tmp;
    while (total < I) // keep track of progrss until the threads complete all they were supposed to
    {
        total = 0;
        for (uint32_t i = 0; i < large_threads; i++) // progress in large threads
        {
            tmp = trackers[i];
            total += tmp;
            printf("Thread %i: %f%%    \n", i, 100. * (double)tmp / (double)large_work);
        }

        for (uint32_t i = large_threads; i < small_threads + large_threads; i++) // progrss in small threads
        {
            tmp = trackers[i]; // uhhhh, concurrency go brrr, but bc its only a read, idc
            total += tmp;
            printf("Thread %i: %f%%    \n", i, 100. * (double)tmp / (double)small_work);
        }

        printf("Total : %f%%    \n", 100. * (double)total / (double)I);

        sleep(1);                           // lets not bug threads too often
        printf("\033[%iA", thread_cnt + 1); // jump back a few lines so u can update them on the next print
        fflush(stdout);                     // printing shenanigans
    }
    printf("\033[%iB", thread_cnt + 1);

    for (uint32_t i = 0; i < thread_cnt; i++) // just to be sure, wait for the threads to complete,
    {                                         // they might still be freeing memory or smth
        pthread_join(threads[i], NULL);
    } // yes, it is ok to send the return to NULL
    free(threads);
    free(thread_args);
    free(trackers);

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
    double bd_max = bd[0]; // compute the maximum, yes i spent a lot of time trying to find the best way to do this
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        bd_max = fmax(bd[i], bd_max);
    }

// normalize brightness
#ifdef __CLAMP
    const double clamp_min = 0;               // reduces noise in black areas, but 0 is not bad
    const double clamp_max = 2 / 3. * bd_max; // reduces peaks -> increases overall brightness
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

    uint8_t *pic = malloc(Nx * Ny * sizeof(uint8_t)); // map to uint8_t, maybe not optimal, but fast enough
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        pic[i] = (uint8_t)bd[i];
    }
    free(bd);

    FILE *f = fopen("out8.pgm", "w");                // a very simple image image format to write to
    fprintf(f, "P5\n%i %i %i\n", Nx, Ny, UINT8_MAX); // header
    fwrite(pic, Nx * Ny, 1, f);                      // data
    fclose(f);
    printf("Done computing. Enjoy :)\n");

    return 0;
}