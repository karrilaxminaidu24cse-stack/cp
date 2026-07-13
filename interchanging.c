#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    int i, minIndex = 0, maxIndex = 0;

    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (arr[i] < arr[minIndex])
            minIndex = i;
        if (arr[i] > arr[maxIndex])
            maxIndex = i;
    }
    int temp = arr[minIndex];
    arr[minIndex] = arr[maxIndex];
    arr[maxIndex] = temp;
    for (i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i != n - 1)
            printf(" ");
    }

    return 0;
}
