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
	printf("Price: %f %s\n\n\n", newProduct->price, newProduct->pUnit);
	displayMenu();
}

void purchase(product* l, char name[], float quantity) {
	if (l != NULL) {
		if (quantity <= l->quantity) {
			float newQuantity = l->quantity - quantity;
			l->quantity = newQuantity;
			printf("Purchased %f %s of %s\n", l->quantity, l->qUnit, l->pName);
		} else {
			puts("We do not have enough in stock, sorry :(");
		}
	} else {
		puts("Could not find that product, please check our stock!");
	}
	displayMenu();
}

void checkPrice(product* l, char name[]) {
	product* current = l;
	while(current != NULL) {
		if (current->pName == name) {
			printf("The price of %s is: %f\n\n", current->pName, current->price);
		}
		current = current->next;
	}
	displayMenu();
}

void showProducts(product* l) {
	product* current = l;

	puts("Items currently in store:\n");
	 while(current != NULL) {
		printf("%s\n\n", current->pName);
		current = current->next;
	}
	displayMenu();
}

// void cleanUpProduct(product* l, char name[]) {
// 	product* current = l;
// 	product* p = get(name);
// 	while(current != NULL) {
// 		current = current->next;
// 	}
// }
