#include "stdio.h"
#include "stdlib.h"
#include "buddha1.h"
#include "stdint.h"
#include "stdbool.h"
#include "math.h"

inline bool isNaN(const complex z)
{
    return isnan(z.x) || isnan(z.y);
}

inline complex sq(const complex z)
{
    return (complex){z.x * z.x - z.y * z.y, 2. * z.x * z.y};
}

inline complex add(const complex z1, const complex z2)
{
    return (complex){z1.x + z2.x, z1.y + z2.y};
}

inline double abs2(const complex z)
{
    return z.x * z.x + z.y * z.y;
}

inline idx map_to_idx(complex key,
                      double xmin,
                      double ymin,
                      double width,
                      double height,
                      double Nx,
                      double Ny)
{
    uint32_t key_x = (uint32_t)(((key.x - xmin) / width + 0.5 / (double)Nx) * (Nx - 1));
    uint32_t key_y = (uint32_t)(((key.y - ymin) / height + 0.5 / (double)Ny) * (Ny - 1));

    return (idx){key_x, key_y};
}

inline bool lies_within(complex key,
                        double xmin,
                        double xmax,
                        double ymin,
                        double ymax,
                        double Nx,
                        double Ny)
{
    return xmin <= key.x && key.x <= xmax && ymin <= key.y && key.y <= ymax;
}

int main(int argc, char *argv[])
{
    const uint32_t Nx = 1200;
    const uint32_t Ny = 800;
    const uint32_t N = 255;

    const double xmin = -2;
    const double xmax = 1;
    const double ymin = -1;
    const double ymax = 1;

    const double width = xmax - xmin;
    const double height = ymax - ymin;

    // generate plane
    complex *c = malloc(Nx * Ny * sizeof(complex));
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            c[nx + ny * Nx].x = xmin + width * (nx / (double)(Nx - 1));
            c[nx + ny * Nx].y = ymin + height * (ny / (double)(Ny - 1));
        }
    }
    printf("Computed plane.\n");

    // compute mandelbrot history
    complex *z = malloc(Nx * Ny * N * sizeof(complex));
    for (uint32_t n = 0; n < N - 1; n++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            for (uint32_t ny = 0; ny < Ny; ny++)
            {
                z[nx + ny * Nx + (n + 1) * Nx * Ny] = add(sq(z[nx + ny * Nx + n * Nx * Ny]), c[nx + ny * Nx]);
            }
        }
    }
    free(c);
    printf("Computed mandelbrot history.\n");

    // compute buddahbrot traces
    double *bd = malloc(Nx * Ny * sizeof(double));
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            for (uint32_t n = 0; n < N; n++)
            {
                if (abs2(z[nx + ny * Nx + (N - 1) * Nx * Ny]) > 4 || isNaN(z[nx + ny * Nx + (N - 1) * Nx * Ny]))
                {
                    if (lies_within(z[nx + ny * Nx + n * Nx * Ny], xmin, xmax, ymin, ymax, Nx, Ny))
                    {
                        idx i = map_to_idx(
                            z[nx + ny * Nx + n * Nx * Ny],
                            xmin,
                            ymin,
                            width,
                            height,
                            Nx, Ny);

                        bd[i.x + i.y * Nx]++;
                    }
                }
                else
                    break;
            }
        }
    }
    free(z);
    printf("Computed raw budhabrot.\n");

    // map to nice colour values
    {
        idx i = map_to_idx(
            (complex){0, 0},
            xmin,
            ymin,
            width,
            height,
            Nx, Ny);

        bd[i.x + i.y * Nx] = 1;
    }

    double bd_max = 0;
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            bd_max = fmax(bd[nx + ny * Nx], bd_max);
        }
    }
    printf("Computed maximum.\n");

    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            bd[nx + ny * Nx] = 1 - exp(-bd[nx + ny * Nx] * bd[nx + ny * Nx] / bd_max) * exp(1 / bd_max);
        }
    }
    printf("Polished buddhabrot.\n");

    //*
    FILE *f = fopen("out.pgm", "wb");
    fprintf(f, "P5\n%i %i 255\n", Nx, Ny);
    for (uint32_t ny = 0; ny < Ny; ny++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            fputc((uint8_t)(255*bd[nx + ny * Nx]), f);
        }
    }
    fclose(f);
    printf("Saved the file, enjoy :)\n");
    //*/

    return 0;
}