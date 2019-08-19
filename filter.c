#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int main (int argc, char * argv[]) {
    char SEQ[] = {'\t', '"', ' ', '"', '\t'};
    char * seq = SEQ;

    if (argc < 2 || argc > 3) return 1;

    char * f = argv[1];
    FILE * fptr = fopen(f, "r");

    if (argc == 3) seq = argv[2];

    printf("File: %s\n", f, seq);

    int row = 1;
    int ind = 0;

    for (char c = fgetc(fptr); c != EOF; c = fgetc(fptr)) {
        switch (c) {
            case ' ':
            case '\t':
            case '"':
                if (c == seq[ind]) ind++;
                else break;
                if (ind == 4) {
                    printf("%d\n", row);
                    ind = 0;
                }
                break;
            case '\n':
                row++;
            default:
                ind = 0;
                
        }
    }

    fclose(fptr);

    return 0;
}
