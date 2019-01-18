#include <algorithm>
#include <cstdlib>
#include <string>
#include <iostream>
#include <unordered_map>

class OneAway {
  public:
    bool one_away(std::string input_one, std::string input_two) {
      if (abs(input_one.length() - input_two.length()) > 1) {
        return false;
      }

      for (const auto& value : input_one) {
        auto pos = input_two.find(value);
        if (pos != std::string::npos) {
          input_two.erase(pos);
        }
      }

      return input_two.length() < 2;
    }
};

int main(int argc, char** argv) {
  OneAway oa;
  std::string one(argv[1]);
  std::string two(argv[2]);

  std::cout << oa.one_away(one, two) << std::endl;

  return 0;
}
