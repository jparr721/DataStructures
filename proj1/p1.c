#include <stdio.h>
#include "functions.h"


int main(int argc, char* argv[]) {
	char cmd = *argv[1]; // either e or d
	char* file;
	char cipher[26];
	char* in;
	char* out;
	key = argv[2];
	switch(cmd) {
		case 'e':
			cmd = *processInput(argv[3]);
			in = encrypt(&cmd);
			printf("After encryption, the output is: %s\n", in);
			processOutput(argv[4], in);
			break;
		case 'd':
			cmd = *processInput(argv[3]);
			out = decrypt(&cmd);
			printf("After decryption, the output is: %s\n", out);
			processOutput(argv[4], out);
			break;
		default:
			printf("Instructions \n\n");
            printf("You're probably here because you made a mistake \n\n");
			printf("Invocation format: \n");
			printf("./p1 -e/-d key inFile outFile\n");
	}
	return 0;
}



