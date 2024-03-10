#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 200
char t[MAX];
void hashTable(char a[])
{
    int n = strlen(a);
    for (int i = 0; i < 200; i++)
        t[i] = n;
    for (int i = n - 2; i >= 0; i--)
    {
        if (t[a[i]] == n)
        {
            t[a[i]] = n - i - 1;
        }
    }
}
int search(char *src, char *pat)
{
    int n = strlen(pat);
    int h = strlen(pat) - 1;
    int m = strlen(src);
    int i = 0, j = 0;
    for (int i = 0; i < n; i++)
    {
        printf("%d", t[pat[i]]);
    }
    while (h < m)
    {
        // printf("beforej=%d, h=%d\n", j, h);

        j = 0;
        while (j >= 0 && src[h - j] == pat[n - 1 - j])
        {
            // printf("%c\n", pat[j]);
            j++;
        }
        // printf("afterj=%d, h=%d\n", j, h);
        if (j == n)
            return h - n + 1;
        else
        {
            // printf("%c\n", src[h - (n - 1 - j)]);
            h = h - j + t[src[h - j]];
        }
    }
    return -1;
}
int main()
{
    char src[100];
    char pat[100];
    printf("Enter the source string : ");
    scanf("%s", src);
    printf("Enter the pattern you want to search : ");
    scanf("%s", pat);
    // char src[] = "JIM_SAW_ME_IN_A_BARBERSHOP";
    // char pat[] = "BARBER";
    hashTable(pat);
    int n = strlen(pat);
    int x = search(src, pat);
    if (x == -1)
        printf("Pattern not found\n");
    else
    {
        printf("Pattern found at index: %d\n", x);
    }
    return 0;
}
