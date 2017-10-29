#include <stdio.h>
#include "operations.h"

int choice = 0;

void displayMenu() {
	system("clear");
	puts("Sah dude, welcome to my store");
	puts("Select an option bromigo");
	puts("===============================================================================================");
	puts("1: Add a product to store 			2: Purchase a product from store");
	puts("3: Check price of a product			4: Show products in store");
	puts("5: Clean up a product from store		6: Find a product");
	puts("7: Inventory					8: Done for today");
	puts("Which option?: ");
	scanf("%d", &choice);
	printf("%d selected\n\n", choice); 
}

int startStore(char data[]) {
	
}

int main() {
	while(choice != 8) {
		displayMenu();
		char productName[20];
		product* list = NULL;

		switch(choice) {
			case 1:
				puts("===========================  Add Item  ===================================");
				struct product p;
				puts("Enter the name of the new product: ");
				scanf("%s", p.pName);
				/*
				puts("Enter the quantity of the product: ");
				scanf("%lf", p.quantity);
				puts("Enter the quantity units: ");
				scanf("%s", p.qUnit);
				puts("Enter the price for this product: ");
				scanf("%lf", p.price);
				puts("Enter the price units ($/lb etc.): ");
				scanf("%s", p.pUnit);
				addProduct(&list, p);
				*/
				p.quantity = 100;
				strncpy(p.qUnit, "lb", 20);
				p.price = 4;
				strncpy(p.pUnit, "$/lb", 20);
				addProduct(&list, p);
				break;
			case 2:
				puts("===========================  Purchase Item  ================================");
				float q = 0;
				puts("Enter the name of the product you'd like to purchase: ");
				scanf("%s", productName);
				puts("Enter the amount of the product you'd like to purchase: ");
				scanf("%lf", q);
				purchase(list, productName, q);
				break;
			case 3:
				puts("==========================  Check price  ===================================");
				puts("Enter the name of the product you'd like to purchase: ");
				scanf("%s", productName);
				break;
			
		}
		return 0;
	}

}

