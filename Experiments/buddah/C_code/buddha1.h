#include "stdint.h"
#include "stdbool.h"

typedef struct complex
{
    double x;
    double y;
} complex;

bool isNaN(const complex);

complex sq(const complex);

complex add(const complex, const complex);

double abs2(const complex);

typedef struct idx
{
    uint32_t x;
    uint32_t y;
} idx;

idx map_to_idx(complex, double, double, double, double, double, double);

bool lies_within(complex, double, double, double, double, double, double);