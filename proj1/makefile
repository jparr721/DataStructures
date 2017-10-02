all: functions.h functions.o p1.o
	gcc -o p functions.o p1.o

p1.o: functions.h p1.c
	gcc -c p1.c

functions.o: functions.h functions.c
	gcc -c functions.c

enc:
	./p1 e FEATHER infile.txt outfile.txt

dec:
	./p1 FEATHER outfile infile
