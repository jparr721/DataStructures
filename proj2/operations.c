#include "operations.h"

void addProduct(product ** l, product node) {
	product * newProduct;
	newProduct = malloc(sizeof(product));

	strncpy(newProduct->pName, node.pName, 20);
	strncpy(newProduct->qUnit, node.qUnit, 20);
	strncpy(newProduct->pUnit, node.pUnit, 20);
	newProduct->quantity = node.quantity;
	newProduct->price = node.price;
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
		if (strcmp(current->pName, name) == 0) {
			printf("The price of %s is: %s%f\n\n", current->pUnit, current->pName, current->price);
		}
		current = current->next;
	}
	displayMenu();
}

void showProducts(product* l) {
	product* current = l;

	puts("Items currently in store:\n");
	 while(current != NULL) {
		printf("--%s\n\n", current->pName);
		current = current->next;
	}
	displayMenu();
}

void cleanUpProduct(product* l, char name[]) {
	product* current = l;

	if(strcmp(current->pName, l->pName) == 0) {
		list = current->next;	
	} else {
		while(current->next != NULL) {
			if(strcmp(current->next->pName, l->pName) == 0) {
				product* removed = current->next;
				if(removed->next != NULL) {
					current->next = removed->next;
					puts("Item removed successfully!");
				} else {
					current->next = NULL;
				}
				break;
			}
			current = current->next;
		}
	}
	displayMenu();
}

void findProduct(product* l, char name[]) {
	product* current = l;

	while(current != NULL) {
		if(strcmp(current->pName, name) == 0) {
			printf("Product: %s\n\nQuantity: %f%s\n\nPrice: %f%s\n", current->pName, current->quantity, current->qUnit, current->price, current->pUnit);
		} else {
			puts("Error, could not find product with that name");
		}
		current = current->next;
	}
	displayMenu();
}

void showInv(product* l) {
	product* current = l;
	puts("Full item inventory: \n");
	
	while(current != NULL) {
		printf("------------%s-------------\n", current->pName);
		printf("Quantity: %f%s\nPrice: %f%s\n", current->quantity, current->qUnit, current->price, current->pUnit);
		current = current->next;
	}
	displayMenu();
}







