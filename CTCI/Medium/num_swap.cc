#include <string>
#include <iostream>
#include <vector>

class NumberSwapper {
  public:
    void swap(std::string number, int one, int two) {
      if (two < one) {
        int t = two;
        two = one;
        one = t;
      }
      std::cout << number[two] << std::endl;
      number.replace(number.begin() + one, number.begin() + two, std::string(&number[two]) + std::string(&number[one]));
      std::cout << number << "\n" << std::endl;
      return;
    }
};

int main() {
  NumberSwapper ns;
  ns.swap("1234", 1, 2);

  return EXIT_SUCCESS;
}
