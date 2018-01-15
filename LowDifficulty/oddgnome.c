#include <stdio.h>
#include <stdlib.h>

int main() {

    int groups, answer, gnomes, previous, b;

    scanf("%d", &groups);

    for(int i = 0; i < groups; i++){

        scanf("%d", &gnomes);
        scanf("%d", &b);
        answer = 0;

        for (int j = 1; j < gnomes; j++) {

            previous = b;
            scanf("%d", &b);

            if (b-previous != 1) {
                answer = j;
            }
        }

        printf("%d\n", answer);

    }
}