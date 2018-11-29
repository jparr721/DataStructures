#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <iterator>
#include <vector>

class ReverseWords {
  public:
    void reverseWords(std::string &s) {
      std::istringstream iss(s);
      std::vector<std::string> words{std::istream_iterator<std::string>{iss},
                                     std::istream_iterator<std::string>{}};
      std::reverse(words.begin(), words.end());
      std::ostringstream oss;
      int len = words.size();
      for (int i = 0; i < len - 1; ++i) {
          oss << words[i] << " ";
      }
      oss << words[len - 1];
      s = oss.str();
      std::cout << s << std::endl;
    }

   int test(int argc, char** argv) {
    std::string words = argv[1];
    reverseWords(words);
    std::cout << words << std::endl;

    return EXIT_SUCCESS;
   }
};

int main(int argc, char** argv) {
  if (argc < 2) {
    std::cerr << "usage: ./a.out <string>" << std::endl;
  }

  ReverseWords rw;
  return rw.test(argc, argv);
}
