#include <stdio.h>

int main() {

    int a, b, c, max, ans = 0;

    scanf("%d%d%d", &a, &b, &c);

    if (c-b > b-a) {
        max = c-b;
    } else {
        max = b-a;
    }

    printf("%d", max-1);
    return 0;
}