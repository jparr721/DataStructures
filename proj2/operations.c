#include "operations.h"

void addProduct(product ** l, product node) {
	product * newProduct;
	newProduct = malloc(sizeof(product));

	newProduct = &node;
	newProduct->next = *l;
	*l = newProduct;
	
	puts("New Item added \n");
	printf("Name: %s\n", newProduct->pName);
	printf("Quantity: %f%s\n", newProduct->quantity, newProduct->qUnit);
	printf("Price: %f %s\n", newProduct->price, newProduct->pUnit);

}

float purchase(product* l, char name[], float quantity) {

}

