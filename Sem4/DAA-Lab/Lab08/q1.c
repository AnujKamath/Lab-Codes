#include <stdlib.h>
#include <stdio.h>
void heapify(int h[], int n)
{
    int i, k, v, heapify, j;
    for (i = (n / 2); i >= 1; i--)
    {
        k = i;
        v = h[k];
        heapify = 0;
        while (heapify == 0 && 2 * k <= n)
        {
            j = 2 * k;
            if (j < n)
                if (h[j] < h[j + 1])
                    j = j + 1;
            if (v >= h[j])
                heapify = 1;
            else
            {
                h[k] = h[j];
                k = j;
            }
        }
        h[k] = v;
    }
    return;
}
int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    int *a = (int *)calloc(n + 1, sizeof(int));
    printf("Enter the elements");
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
        heapify(a, i);
    }
    printf("The result is: ");
    for (int i = 1; i <= n; i++)
        printf("%d ", a[i]);
    return 0;
}