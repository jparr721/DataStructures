#include <algorithm>
#include <string>
#include <iostream>

/**
 * This class checks if one string is a permuation
 * of another one
 */
class CheckPermutation {
  public:
    bool is_permutation(std::string one, std::string two) {
      std::sort(one.begin(), one.end());
      std::sort(two.begin(), two.end());

      return one == two;
    }
};

int main(int argc, char** argv) {
  CheckPermutation cp;
  std::cout << cp.is_permutation("racecar", "caracer") << std::endl;
  std::cout << cp.is_permutation("nylon", "lyonn") << std::endl;
  std::cout << cp.is_permutation("Orange", "dolphin") << std::endl;
}
