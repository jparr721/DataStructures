#include <algorithm>
#include <string>
#include <iostream>
#include <unordered_map>

class PalindromePermutation {
  public:
    bool palindrome_permutation(std::string input) {
      std::transform(input.begin(), input.end(), input.begin(), ::tolower);
      std::unordered_map<char, int> letter_counts;

      for (const auto& letter : input) {
        auto found = letter_counts.find(letter);
        if (found == letter_counts.end()) {
          letter_counts[letter] = 1;
        } else { letter_counts[letter]++; }
      }

      int singles = 0;
      for (const auto& count : letter_counts) {
        if (count.second == 1) {
          singles++;
        }
      }

      return singles < 2;
    }
};


int main(int argc, char** argv) {
  std::string input(argv[1]);
  PalindromePermutation pp;

  std::cout << pp.palindrome_permutation(input) << std::endl;
}
