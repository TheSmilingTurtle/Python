#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include "stdbool.h"
#include "math.h"

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
    double *cx = malloc(Nx * sizeof(double));
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        cx[nx] = xmin + width * (nx / (double)(Nx - 1));
    }
    double *cy = malloc(Ny * sizeof(double));
    for (uint32_t ny = 0; ny < Ny; ny++)
    {
        cy[ny] = ymin + height * (ny / (double)(Ny - 1));
    }
    printf("Computed plane.\n");

    //initialize to 0
    double *zr = malloc(Nx * Ny * N * sizeof(double));
    for (uint32_t n = 0; n < N; n++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            for (uint32_t ny = 0; ny < Ny; ny++)
            {
                zr[nx + ny * Nx + n * Nx * Ny] = 0;
            }
        }
    }
    double *zi = malloc(Nx * Ny * N * sizeof(double));
    for (uint32_t n = 0; n < N; n++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            for (uint32_t ny = 0; ny < Ny; ny++)
            {
                zi[nx + ny * Nx + n * Nx * Ny] = 0;
            }
        }
    }

    // compute mandelbrot history
    for (uint32_t ny = 0; ny < Ny; ny++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            for (uint32_t n = 0; n < N - 1; n++)
            {
                uint32_t current_idx = nx + ny * Nx + n * Nx * Ny;
                uint32_t next_idx = nx + ny * Nx + (n + 1) * Nx * Ny;

                zr[next_idx] = zr[current_idx] * zr[current_idx] - zi[current_idx] * zi[current_idx] + cx[nx];
                zi[next_idx] = 2 * zr[current_idx] * zi[current_idx] + cy[ny];

                if (xmin > zr[next_idx] || zr[next_idx] > xmax || ymin > zi[next_idx] || zi[next_idx] > ymax)
                {//if it has escaped the image, then the values is inconsequential and we can assume that it is NaN
                //this assumption is only valid when the entire set is contained within the image. (I think)
                    for (; n < N - 1; n++)
                    {
                        uint32_t next_idx = nx + ny * Nx + (n + 1) * Nx * Ny;

                        zr[next_idx] = NAN;
                        zi[next_idx] = NAN;
                    }
                    break;
                }
            }
        }
    }
    free(cx);
    free(cy);
    printf("Computed mandelbrot history.\n");

    //initialize to 0
    uint8_t *bd = malloc(Nx * Ny * sizeof(uint8_t));
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            bd[nx + ny * Nx] = 0;
        }
    }

    //compute buddahbrot traces
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            uint32_t end_idx = nx + ny * Nx + (N - 1) * Nx * Ny;
            double end_abs = zr[end_idx] * zr[end_idx] + zi[end_idx] * zi[end_idx];
            if (end_abs > 4 || isnan(zr[end_idx]) || isnan(zi[end_idx]))
            {
                for (uint32_t n = 0; n < N; n++)
                {
                    uint32_t n_idx = nx + ny * Nx + n * Nx * Ny;
                    if (xmin <= zr[n_idx] && zr[n_idx] <= xmax && ymin <= zi[n_idx] && zi[n_idx] <= ymax)
                    {
                        uint32_t x = ((zr[n_idx] - xmin) / width + 0.5 / (double)Nx) * (Nx - 1); // implicit cast here
                        uint32_t y = ((zi[n_idx] - ymin) / height + 0.5 / (double)Ny) * (Ny - 1);

                        bd[x + y * Nx]++;
                    }
                }
            }
        }
    }
    free(zr);
    free(zi);
    printf("Computed raw buddhabrot.\n");

    //the 0 point will always have an insanely high value bc of nan or smth, i dont fully understand
    if (xmin <= 0 && 0 <= xmax && ymin <= 0 && 0 <= ymax)
    {
        uint32_t x = (uint32_t)((-xmin / width + 0.5 / (double)Nx) * (Nx - 1));
        uint32_t y = (uint32_t)((-ymin / height + 0.5 / (double)Ny) * (Ny - 1));

        bd[x + y * Nx] = 1;
    }

    //find maximum
    double bd_max = 0;
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            bd_max = fmax(bd[nx + ny * Nx], bd_max);
        }
    }
    printf("Computed maximum.\n");

    //normalize brightness
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            bd[nx + ny * Nx] = 256 - 256 * exp(-bd[nx + ny * Nx] * bd[nx + ny * Nx] / bd_max) * exp(1 / bd_max); // bunch of implicit casts here
        }
    }
    printf("Polished buddhabrot.\n");

    //*
    {//file header
        FILE *f = fopen("out2.pgm", "wb");
        fprintf(f, "P5\n%i %i %i\n", Nx, Ny, UINT8_MAX);
        fclose(f);
    }//write data to file
    FILE *f = fopen("out2.pgm", "a");
    fwrite(bd, 1, Nx * Ny, f);
    fclose(f);
    /*
    for (uint32_t ny = 0; ny < Ny; ny++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            fputc((uint8_t)(UINT8_MAX * bd[nx + ny * Nx]), f);
        }
    }
    fclose(f);
    //*/
    printf("Saved the file, enjoy :)\n");

    return 0;
}