all: functions.h functions.o p1.o
	gcc -o functions.o p1.o

p1.o: functions.h p1.c
	gcc -c p1.c

functions.o: functions.h functions.c
	gcc -c functions.c

enc:
	./p e FEATHER infile outfile

dex:
	./p FEATHER outfile infile
