#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 20
typedef struct Node {
    char a[MAX];
    struct Node* next;
} Node;

int findSum(char* b, int j) {
    int sum = 0;
    for(int i = 0; i <= j; i++) {
        sum += (b[i]-'a'+1); 
    }
    return sum;
}
void makeCopy(char a[],char b[],int j)
{
    for(int i=0;i<=j;i++)
    a[i]=b[i];
    a[j + 1] = '\0';
}
void insertNode(Node** head, int sum, Node* temp) {
    Node* temper = head[sum];
    if (!temper)
        head[sum] = temp;
    else {
        while (temper->next) {
            temper = temper->next;
        }
        temper->next = temp;
    }
}

Node** makeOpenTable(char a[], int k) {
    Node** head = (Node**)calloc(k, sizeof(Node*));
    for (int i = 0; i < k; i++) { 
        head[i] = NULL;
    }
    Node* temp;
    char b[50];
    int j = -1, i = 0;
    for (int i = 0; i < strlen(a); i++) { 
        if (a[i] == ' '||a[i]=='.'|| a[i] == '\0') {
            int sum = findSum(b, j) % k;
            temp = (Node*)malloc(sizeof(Node));
            temp->next = NULL;
            makeCopy(temp->a,b,j);
            insertNode(head, sum, temp);
            j=-1;
        }
        else {
            b[++j] = a[i];
        }
    }
    return head;
}

int main() {
    // a fool and his money are soon parted.
    char s[100];
    int k;
    printf("Enter the value of k: ");
    scanf("%d", &k);
    printf("Enter the sentence: ");
    getchar(); // Consume the newline character left in the input buffer
    fgets(s, sizeof(s), stdin);
    Node** head = makeOpenTable(s, k);
    for (int i = 0; i < k; i++) {
        int c = 0;
        printf("%d:", i);
        Node* temp = head[i];
        while (temp) {
            c++;
            printf(" %s,", temp->a);
            temp = temp->next;
        }
        printf(" (%d)\n", c); 
    }
    return 0;
}
