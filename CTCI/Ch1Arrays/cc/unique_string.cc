#include <string>
#include <iostream>
#include <unordered_map>

/**
 * This checks if a string has all unique characters
 */
class UniqueString {
  public:
    bool is_unique(std::string input) {
      std::unordered_map<char, int> occur;

      for (const auto& s : input) {
        auto found = occur.find(s);
        if (found == occur.end()) {
          occur[s] = 1;
        } else { return false; }
      }

      return true;
    }

    bool unique_no_structures(std::string input) {
      for (int i = 0; i < input.length(); ++i) {
        for (int j = i + 1; j < input.length(); ++j) {
          if (input.at(i) == input.at(j)) {
            return false;
          }
        }
      }

      return true;
    }
};

int main() {
  UniqueString us;
  auto out = us.is_unique("abababa");
  auto out2 = us.is_unique("aple");
  auto out3 = us.unique_no_structures("abbaba");
  auto out4 = us.unique_no_structures("Forest");

  std::cout << "tests" << std::endl;
  // False cases
  std::cout << out << std::endl;
  std::cout << out3 << std::endl;

  // True cases
  std::cout << out2 << std::endl;
  std::cout << out4 << std::endl;

  return EXIT_SUCCESS;
}
