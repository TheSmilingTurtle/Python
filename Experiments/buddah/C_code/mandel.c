#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include "pthread.h"
#include "time.h"
#include "png.h"

struct Args
{
    uint8_t *bd;
    uint32_t Nx;
    uint32_t Ny;
    uint32_t offset;
    uint32_t period;
    double xmin;
    double ymin;
    double width;
    double height;
};

void *mandel(void *__args)
{
    const struct Args *args = (struct Args *)__args;
    uint8_t *bd = args->bd;
    const uint32_t Nx = args->Nx;
    const uint32_t Ny = args->Ny;
    const uint32_t offset = args->offset;
    const uint32_t period = args->period;
    const double xmin = args->xmin;
    const double ymin = args->ymin;
    const double width = args->width;
    const double height = args->height;

    double cr;
    double ci;
    double zr;
    double zi;
    double zr2;
    double zi2;

    for (uint32_t nx = 0; nx < Nx; nx++)
    {
        for (uint32_t ny = offset; ny < Ny; ny += period)
        {
            cr = xmin + width * (nx / (double)(Nx - 1));
            ci = ymin + height * (ny / (double)(Ny - 1));
            zr = cr;
            zi = ci;
            zr2 = zr * zr;
            zi2 = zi * zi;

            for (uint8_t n = 0; n < 255; n++)
            {
                if (!(zr2 + zi2 < 4))
                {
                    break;
                }
                bd[nx + ny * Nx]++;
                zi = (zr + zr) * zi + ci;
                zr = zr2 - zi2 + cr;
                zr2 = zr * zr;
                zi2 = zi * zi;
            }
        }
    }

    return NULL;
}

int main(int argc, char *argv[])
{
    uint32_t Nx = 1200;
    uint32_t Ny = 800;
    uint32_t thread_cnt = 4;

    double xmin = -2;
    double xmax = 1;
    double ymin = -1;
    double ymax = 1;

    if (argc == 1)
    {
    }
    else if (argc == 3)
    {
        Nx = atoi(argv[1]);
        Ny = atoi(argv[2]);
    }
    else if (argc == 4)
    {
        Nx = atoi(argv[1]);
        Ny = atoi(argv[2]);
        thread_cnt = atoi(argv[3]);
    }
    else if (argc == 7)
    {
        Nx = atoi(argv[1]);
        Ny = atoi(argv[2]);
        xmin = atof(argv[3]);
        xmax = atof(argv[4]);
        ymin = atof(argv[5]);
        ymax = atof(argv[6]);
    }
    else if (argc == 8)
    {
        Nx = atoi(argv[1]);
        Ny = atoi(argv[2]);
        xmin = atof(argv[3]);
        xmax = atof(argv[4]);
        ymin = atof(argv[5]);
        ymax = atof(argv[6]);
        thread_cnt = atoi(argv[7]);
    }
    else
    {
        printf("Wrong number of arguments.\n");
    }

    const double width = xmax - xmin;
    const double height = ymax - ymin;

    printf("Calculating Mandelbrot.\n");

    uint8_t *bd = malloc(Nx * Ny * sizeof(uint8_t)); // create and initialize
    for (uint32_t i = 1; i < Nx * Ny; i++)
    {
        bd[i] = 0;
    }

    pthread_t *threads = malloc(thread_cnt * sizeof(pthread_t));
    struct Args *thread_args = malloc(thread_cnt * sizeof(struct Args));

    uint32_t large_threads = Ny % thread_cnt;
    uint32_t large_work = Ny / thread_cnt + 1;
    uint32_t start = 0;
    for (uint32_t i = 0; i < large_threads; i++)
    {
        struct Args tmp = {bd, Nx, Ny, i, thread_cnt, xmin, ymin, width, height};
        start += large_work;
        thread_args[i] = tmp;
    }

    uint32_t small_threads = thread_cnt - large_threads;
    uint32_t small_work = Ny / thread_cnt;
    for (uint32_t i = large_threads; i < small_threads + large_threads; i++)
    {
        struct Args tmp = {bd, Nx, Ny, i, thread_cnt, xmin, ymin, width, height};
        start += small_work;
        thread_args[i] = tmp;
    }

    struct timespec t_start, end;
    clock_gettime(CLOCK_MONOTONIC_RAW, &t_start);
    if (thread_cnt > 1)
    {
        for (uint32_t i = 0; i < thread_cnt; i++) // initialize the threads
        {
            pthread_create(threads + i, NULL, mandel, (void *)&thread_args[i]);
        }
    }
    else
    {
        mandel((void *)&thread_args[0]);
    }
    if (thread_cnt > 1)
    {

        for (uint32_t i = 0; i < thread_cnt; i++) // just to be sure, wait for the threads to complete,
        {                                         // they might still be freeing memory or smth
            pthread_join(threads[i], NULL);
        }
    }

    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    free(threads);
    free(thread_args);

    double delta_us = (end.tv_sec - t_start.tv_sec) + (end.tv_nsec - t_start.tv_nsec) / 1000000000.0;
    FILE *f = fopen("mandel.pgm", "w");              // a very simple image image format to write to
    fprintf(f, "P5\n%i %i %i\n", Nx, Ny, UINT8_MAX); // header
    fwrite(bd, Nx * Ny, 1, f);                       // data
    fclose(f);
    printf("Done computing. Time elapsed: %fs\n", delta_us);
    free(bd);

    return 0;
}