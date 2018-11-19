#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>


class WordFrequencies {
  public:
    std::vector<std::string> split(const std::string &in, char token) {
      std::vector<std::string> split_values;
      std::stringstream ss(in);
      std::string delim;

      while (std::getline(ss, delim, token )) {
        split_values.push_back(delim);
      }

      return split_values;
    }

    void strip_punctuation(std::string& in) {
      const std::vector<char> punctuation = { '.', '?', '"', ':', ';', '!' };
      for (const char p : punctuation) {
        if (in.find(p) != std::string::npos) {
          in = split(in, p)[0];
        }
      }

      return;
    }

    // Find word frequencies and print them in a hash map
    std::unordered_map<std::string, int> frequency_finder(std::string book) {
      // Get our vector of indiv. words
      std::vector<std::string> words = split(book, ' ');
      std::unordered_map<std::string, int> frequencies;

      for (auto w : words) {
        strip_punctuation(w);
        auto f = frequencies.find(w);
        if (f != frequencies.end()) {
          frequencies[w]++;
        }
        frequencies[w] = 0;
      }

      return frequencies;
    }
};

int main(int argc, char** argv) {
  WordFrequencies wf;
  std::string words = "Hello my name is jarred, and I love to write a lot of code. Do you?";

  std::unordered_map<std::string, int> freq = wf.frequency_finder(words);
  for (auto it = freq.begin(); it != freq.end(); ++it) {
    std::cout << "Word: " << it->first << " Count: " << it->second << std::endl;
  }

  return EXIT_SUCCESS;
}
