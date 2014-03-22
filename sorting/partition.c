#include <stdio.h>

int partition(void **ar, int(*cmp)(const void *, const void *),
              int left, int right, int pivotIndex) {
    int idx, store;
    void *pivot = ar[pivotIndex];

    void *tmp = ar[right];
    ar[right] = ar[pivotIndex];
    ar[pivotIndex] = tmp;

    store = left;
    for (int idx = left; idx < right; idx++)
    {
        if (cmp(ar[idx], ar[pivot]) <= 0) {
            tmp = ar[idx];
            ar[idx] = ar[store];
            ar[store] = tmp;
            store++;
        }
    }

    tmp = ar[right];
    ar[right] = ar[store];
    ar[store] = tmp;
    return store;
}

int main(int argc, char const *argv[])
{
    // create array in C?
    int ar[10];
    ar = [8, 3, 5, 9, 2, 5, 1];
}
