#include "operations.h"

int profit = 0;
int choice = 0;

void displayMenu() {
	puts("Sah dude, welcome to my store");
	puts("Select an option bromigo");
	puts("===============================================================================================");
	puts("1: Add a product to store 		2: Purchase a product from store");
	puts("3: Check price of a product		4: Show products in store");
	puts("5: Clean up a product from store		6: Find a product");
	puts("7: Inventory				8: Done for today");
	puts("Which option?: ");
	scanf("%d", &choice);
	printf("%d selected\n\n", choice); 
}

void addProduct(product_t ** l, product_t node) {
	product_t * new_product;
	new_product = malloc(sizeof(product_t));	
	puts("Enter the name of the new product: ");
	scanf("%s", new_product->pName);
	puts("Enter the quantity of the product: ");
	scanf("%f", new_product->quantity);
	puts("Enter the units for the quantity: ");
	scanf("%s", new_product->qUnit);
	puts("Enter the price for this product: ");
	scanf("%f", new_product->price);
	puts("Enter the units of the price ($/lb, or other): ");
	scanf("%s", new_product->pUnit);
	new_product->next = *l;
	*l = new_product;
}

