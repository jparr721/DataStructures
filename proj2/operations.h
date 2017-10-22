#pragma once

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 20

typedef struct product {
	char pName[N];
	float quantity;
	char qUnit[N];
	float price;
	char pUnit[N]; // because it sounds like G UNIT BOIIII
	struct product* next;
} product_t;

extern int choice;
extern int profit;

void displayMenu();

void addProduct();

void purchase();

float checkPrice();

struct product* showProducts();

void cleanUpProduct();

struct product* findProduct();

void showInv();

void done();

void load(char inf[]);

void save(char outf[]);
