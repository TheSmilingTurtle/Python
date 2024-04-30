#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include "math.h"

#define __DISC
#define __CLAMP
#define PI 3.14159265358979323846

int main(int argc, char *argv[])
{
    const uint32_t Nx = 1200;
    const uint32_t Ny = 800;
    const uint32_t I = Nx * Ny;
    const uint32_t N = 1024;

    const double xmin = -2;
    const double xmax = 1;
    const double ymin = -1;
    const double ymax = 1;

    const double width = xmax - xmin;
    const double height = ymax - ymin;

    // initialize to 0
    double *zr = malloc(N * sizeof(double));
    for (uint32_t n = 0; n < N; n++)
    {
        zr[n] = 0;
    }
    double *zi = malloc(N * sizeof(double));
    for (uint32_t n = 0; n < N; n++)
    {
        zi[n] = 0;
    }

    double *bd = malloc(Nx * Ny * sizeof(double));
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        bd[i] = 0;
    }

    if (ymin == -ymax) //if it is symmetric along the real axis
    {
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
                        bd[x + (Ny - y - 1) * Nx]++;
                    }
                }
                break;
            }
        }
    }
    }else 
    {
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
    }
    free(zr);
    free(zi);
    printf("Computed raw buddhabrot.\n");

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

    FILE *f = fopen("out5.pgm", "w");
    fprintf(f, "P5\n%i %i %i\n", Nx, Ny, UINT8_MAX); // header
    fwrite(pic, Nx * Ny, 1, f);                      // data
    fclose(f);
    printf("Saved the file, enjoy :)\n");

    return 0;
}