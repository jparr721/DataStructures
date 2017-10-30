#include <stdio.h>
#include "operations.h"

int choice = 0;

void displayMenu() {
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

void startStore(char data[]) {
	// displayMenu();
}

int main() {
	displayMenu();
	while(choice != 8) {
		char productName[20];

		switch(choice) {
			case 1:
				puts("===========================  Add Item  ===================================");
				struct product p;
				char* name = (char*)malloc(20*sizeof(char*));
				char* quantUnit = (char*)malloc(20*sizeof(char*));
				char* priceUnit = (char*)malloc(20*sizeof(char*));
				float quan, pPrice;
				printf("Enter the name of the new product: ");
				scanf("%s", name);
				printf("Enter the quantity of the product: ");
				scanf("%f", &quan);
				printf("Enter the quantity units: ");
				scanf("%s", quantUnit);
				printf("Enter the price for this product: ");
				scanf("%f", &pPrice);
				printf("Enter the price units ($/lb etc.): ");
				scanf("%s", priceUnit);
				strncpy(p.pName, name, 20);
				p.quantity = quan;
				strncpy(p.qUnit, quantUnit, 20);
				p.price = pPrice;
				strncpy(p.pUnit, priceUnit, 20);

				addProduct(&list, p);
				break;
			case 2:
				puts("===========================  Purchase Item  ================================");
				float q = 0;
				puts("Enter the name of the product you'd like to purchase: ");
				scanf("%s", productName);
				puts("Enter the amount of the product you'd like to purchase: ");
				scanf("%f", &q);
				purchase(list, productName, q);
				break;
			case 3:
				puts("==========================  Check price  ===================================");
				puts("Enter the name of the product you'd like to price check: ");
				scanf("%s", productName);
				checkPrice(list, productName);
				break;
			case 4:
				puts("========================== Store Inventory===================================");
				showProducts(list);
				break;
			case 5:
				puts("========================= Clean Up Product =================================");
				puts("Enter the name of the product you'd like to remove: ");
				scanf("%s", productName);
				// cleanUpProduct(list, productName);
			case 9:
			case 0:
				puts("Invalid command! Please run again\n\n");
				exit(0);
				break;
		}
	}
	system("clear");
	puts("Thanks for visiting the totally dank grocery store");
	return 0;
}
