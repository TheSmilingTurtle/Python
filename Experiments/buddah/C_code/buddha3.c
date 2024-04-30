#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
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
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            bd[nx + ny * Nx] = 0;
        }
    }

    // compute mandelbrot history
    for (uint32_t ny = 0; ny < Ny; ny++)
    {
        for (uint32_t nx = 0; nx < Nx; nx++)
        {
            for (uint32_t n = 0; n < N - 1; n++)
            {
                uint32_t next_idx = (n + 1);

                zr[next_idx] = zr[n] * zr[n] - zi[n] * zi[n] + cx[nx];
                zi[next_idx] = 2 * zr[n] * zi[n] + cy[ny];

                if (!(zr[next_idx]*zr[next_idx] + zi[next_idx]*zi[next_idx] <= 2) && (xmin > zr[n] || zr[n] > xmax || ymin > zi[n] || zi[n] > ymax))
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
    free(cx);
    free(cy);
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
    /*
    const double clamp_min = 1/10. * bd_max;
    const double clamp_max = 2/3. * bd_max;
    //*/
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
            /*
            uint32_t idx = nx + ny * Nx;
            bd[idx] = bd[idx] < clamp_min ? clamp_min : bd[idx];
            bd[idx] = bd[idx] > clamp_max ? clamp_max : bd[idx];
            bd[idx] = 255 * (bd[idx] - clamp_min) / (clamp_max - clamp_min);
            //*/
            bd[nx + ny * Nx] = 255 * bd[nx + ny * Nx] / bd_max;
        }
    }
    printf("Polished buddhabrot.\n");

    uint8_t *pic = malloc(Nx * Ny * sizeof(uint8_t));
    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = 0; ny < Ny; ny++)
        {
           pic[nx + ny * Nx] = (uint8_t)bd[nx + ny * Nx];
        }
    }
    free(bd);

    FILE *f = fopen("out3_uneven.pgm", "w");
    fprintf(f, "P5\n%i %i %i\n", Nx, Ny, UINT8_MAX); //header
    fwrite(pic, Nx * Ny, 1, f); //data
    fclose(f);
    printf("Saved the file, enjoy :)\n");

    return 0;
}