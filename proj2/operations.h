#pragma once


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 20

struct product {
	char pName[N];
	float quantity;
	char qUnit[N];
	float price;
	char pUnit[N]; // because it sounds like G UNIT BOIIII
	struct product* next;
};

typedef struct product product;

extern int choice;
extern int profit;

void addProduct(product**, product);

float purchase(product*, char[], float);

float checkPrice(product*, char[]);

void showProducts(product*);

void cleanUpProduct(product*, char[]);

void findProduct(product*, char[]);

void showInv(product*);

void done();

void load(char inf[]);

int startStore(char[]);

void save(char outf[]);
