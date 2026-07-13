#include <stdio.h>
#include <stdlib.h>
int* mergeSortedArrays(int arr1[], int n, int arr2[], int m) {
    int *merged = (int *)malloc((n + m) * sizeof(int));
    int i = 0, j = 0, k = 0;
    while (i < n && j < m) {
        if (arr1[i] <= arr2[j]) {
            merged[k++] = arr1[i++];
        } else {
            merged[k++] = arr2[j++];
        }
    }
    while (i < n) {
        merged[k++] = arr1[i++];
    }
    while (j < m) {
        merged[k++] = arr2[j++];
    }
    return merged;
}
int main() {
    int n, m;
    scanf("%d", &n);
    int arr1[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr1[i]);
    }
    scanf("%d", &m);
    int arr2[m];
    for (int i = 0; i < m; i++) {
        scanf("%d", &arr2[i]);
    }
    int *result = mergeSortedArrays(arr1, n, arr2, m);
    for (int i = 0; i < n + m; i++) {
        printf("%d ", result[i]);
    }
    free(result);
    return 0;
}
