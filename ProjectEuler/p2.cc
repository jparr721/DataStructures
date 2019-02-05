#include <algorithm>
#include <iostream>
#include <vector>
#include "lib.h"

template <unsigned n>
class PTwo {
  public:
    Lib l;

    long fib_sum() {
      long sum = 0;
      long one = 1;
      long two = 2;
      std::vector<long> terms(n, 0);

      for (unsigned i = 0; i < n; ++i) {
        terms[i] = one + two;
        one = two;
        two = terms[i];
      }

      std::for_each(terms.begin(), terms.end(), [&sum, this](const long& value) {
        if (this->template l.multiple_of<int>(value, 2)) {
          sum += value;
        }
      });
    }
};
