#include <algorithm>
#include <cstdint>
#include <string>
#include <iostream>
#include <vector>

/**
 * This class takes a string and urlifies it in all of
 * the spaces
 */
class Urlify {
  public:
    std::string urlify(std::string& input) {
      // Remove end spaces
      if (input.at(input.length() - 1) == ' ') {
        for (int i = input.length() - 1; i > 0; --i) {
          if (input.at(i) == ' ') {
            input.erase(input.begin() + i);
            continue;
          }
          break;
        }
      }
      for (auto i = 0u; i < input.length(); ++i) {
        if (input.at(i) == ' ') {
          input.erase(input.begin() + i);
          input.insert(i, "%20");
        }
      }
      return input;
    }
};

int main(int argc, char** argv) {
  if (argc < 2) {
    std::cout << "usage: a.out string" << std::endl;
    return EXIT_FAILURE;
  }

  Urlify u;
  auto input = std::string(argv[1]);
  std::cout << u.urlify(input) << std::endl;

  return EXIT_SUCCESS;
}
