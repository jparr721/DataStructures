#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>


class SmallestDifference {
  public:
    int smallest_difference(std::vector<int> v1, std::vector<int> v2) {
      int64_t smallest = 1000000000;
      for (const auto v : v1) {
        for (const auto vv : v2) {
          if (abs(v - vv) < smallest) {
            smallest = abs(v - vv);
          }
        }
      }

      return smallest;
    }
};

int main(int argc, char** argv) {
  SmallestDifference sm;
  std::vector<int> v1 = { 4, 1, 2, 19, 29, 292 };
  std::vector<int> v2 = { 10, 2, 18, 107, 466, 45 };
}
