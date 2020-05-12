#include <iostream>
#include "lib.h"

// Find the sum of all multiples of 3 and 5 below 1000
template <unsigned n>
class POne {
  public:
    Lib l;

    int sum_until() {
      int desired_sum = 0;

      // Just run until we find what we're lookin' for
      for (unsigned int i = 0u; i < n; ++i) {
        if (l.multiple_of<int>(i, 3) || l.multiple_of<int>(i, 5)) {
          desired_sum += i;
        }
      }

      return desired_sum;
    }
};

int main(int argc, char** argv) {
  POne<1000> p1;
  std::cout << p1.sum_until() << std::endl;

  return 0;
}
