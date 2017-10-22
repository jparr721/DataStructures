#include "operations.h"

int main(void) {
	displayMenu();
	switch(choice) {
		case 1:
			addProduct();
			break;
		case 2:
			purchase();
			break;
		case 3:
			checkPrice();
			break;
		case 4:
			showProducts();
			break;
		case 5:
			cleanUpProduct();
			break;
		case 6:
			findProduct();
			break;
		case 7:
			showInv();
			break;
		case 8:
			done();
			break;
		default:
			printf("Invalid option selected!");
			break;
	}
}
