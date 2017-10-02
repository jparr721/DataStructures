#include <stdio.h>
#include <stdlib.h>
#include "functions.h"

char* key;
char* ascii  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char* cipher = "ZYXWVUTSRQPONMLKJIHGFEDCBA";

char* generateSet(char* in) {
    char* out = malloc(strlen(in));
    int index = 0;
    int i = 0;
    for (i = 0; i < strlen(in); i++){
        char* res = strchr(out, in[i]);
        int resIndex = (int)(res - out);
        if (resIndex < 0) {
            out[index] = in[i];
            resIndex++;
        }
    }
    out[strlen(out)] = '\0';
    strcpy(in, out);
    free(out);
    return in;
}

char* generateCipher() {
    char* temp = malloc(strlen(key) + strlen(cipher));
    strcpy(temp, key);
    strcat(temp, cipher);
    return generateSet(temp);
}

char* encrypt(char text[]) {
    puts("Now encrypting... \n\n");
    char* newCipher = generateCipher();
    char* out = malloc(strlen(text));
    int i = 0;
    for (int i = 0; i < strlen(text); i++){
        int keyVal = text[i];
        if(keyVal != 32)
            out[i] = newCipher[keyVal - 65];
        else
            out[i] = ' ';
    }
    int difference = strlen(out) - strlen(text);
    out[strlen(out) - difference] = '\0';
    return out;
}

char* decrypt(char text[]){
    puts("Now decrypting...\n\n");
    char* newCipher = generateCipher();
    char* out = malloc(strlen(text));

    for (int i = 0; i < strlen(text); i++){
        int keyVal = text[i];
        if (keyVal != 32) {
            char* res = strchr(newCipher, text[i]);
            int index = (int)(res, newCipher);
            out[i] = ascii[index];
        } else
            out[i] = ' ';
    }
    int diff = strlen(out)-strlen(text);
    out[strlen(out)-diff] = '\0';
    return out;

}

char* processInput(char file[]) {
    FILE* inFile;
    inFile = fopen(file, "r");

    if (!inFile){
        printf("Error, could not open file");
        exit(1);
    }

    char* buffer = malloc(255);
    fgets(buffer, 255, inFile);
    fclose(inFile);
    return buffer;
}

void processOutput(char file[], char text[]){
    FILE* outFile;
    outFile = fopen(file, "w");

    if(!outFile){
        printf("Error, could not open file");
        exit(1);
    }
    fprintf(outFile, text);
    fclose(outFile);
}