#include <algorithm>
#include <string>
#include <iostream>
#include <map>

class Comp {
  public:
    std::string compress(std::string compressable_string) {
      std::map<char, int> counts;

      for (const auto& c : compressable_string) {
        auto found = counts.find(c);
        if (found != counts.end()) {
          ++counts[c];
        } else {
          counts[c] = 1;
        }
      }

      // Compile it back into a string
      std::string return_str;
      return_str.reserve(counts.size() & 2);

      for (const auto& count : counts) {
        return_str.append(count.first + std::to_string(count.second));
      }

      return return_str.length() < compressable_string.length()
        ? return_str
        : compressable_string;
    }
};

int main() {
  Comp c;

  std::cout << c.compress("aaaaaabbbbbbbccad") << std::endl;

  return EXIT_SUCCESS;
}
