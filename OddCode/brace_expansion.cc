#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

std::unordered_map<int, std::vector<std::string>>
ParseParameters(const std::string &expand_string) {
  std::unordered_map<int, std::vector<std::string>> parsed;
  std::string prefix_delimeter = "";

  if (expand_string.at(0) != '{') {
    const int index = expand_string.find('{');
    if (index == std::string::npos) {
      return std::unordered_map<int, std::vector<std::string>>{};
    }

    std::ostringstream oss;
    for (size_t i = 0; i < index; ++i) {
      oss << expand_string[i];
    }

    prefix_delimeter = oss.str();

    parsed.insert(
        std::make_pair(0, std::vector<std::string>{prefix_delimeter}));
  }

  int start = 0;
  if (prefix_delimeter != "") {
    start = prefix_delimeter.length();
  }

  int current_parsed_index = 1;

  std::ostringstream word;
  std::vector<std::string> grouping;
  const char delim = ',';

  for (size_t i = start; i < expand_string.length(); ++i) {
    if (expand_string[i] == '{')
      continue;
    if (expand_string[i] == '}') {
      parsed.insert(std::make_pair(current_parsed_index, grouping));
      grouping.clear();
      ++current_parsed_index;

      if (i + 1 < expand_string.length() && expand_string[i + 1] != '{') {
        const int index = expand_string.find('{', i + 1);

        std::ostringstream delimeter;
        if (index == std::string::npos) {
          for (size_t j = i; j < (expand_string.length() - (i + 1)); ++j) {
            delimeter << expand_string[j];
          }
          parsed.insert(std::make_pair(
              current_parsed_index, std::vector<std::string>{delimeter.str()}));
          ++current_parsed_index;
          break;
        }

        for (size_t j = i; j < index; ++j) {
          delimeter << expand_string[j];
        }

        parsed.insert(std::make_pair(
            current_parsed_index, std::vector<std::string>{delimeter.str()}));
        ++current_parsed_index;

        i = index;
      }

      continue;
    }

    if (expand_string[i] == ',') {
      grouping.push_back(word.str());
      word.str("");
      word.clear();
      continue;
    }

    word << expand_string[i];
  }

  return parsed;
}

void BraceExpansion(const std::string &expand_string) {}

void p_vec(const std::vector<std::string> &input) {
  std::cout << "vector: ";
  for (const auto &val : input) {
    std::cout << val << std::endl;
  }
}

int main() {
  const std::string expand_string = "{1,2,3}-{4,5,6}";
  const std::unordered_map<int, std::vector<std::string>> parsed =
      ParseParameters(expand_string);

  for (const auto p : parsed) {
    std::cout << p.first << " " << std::endl;
    p_vec(p.second);
  }
}