#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

std::string p_vec(const std::vector<std::string> &input) {
  std::ostringstream ret;

  for (const auto val : input) {
    ret << val;
    ret << ", ";
  }

  return ret.str();
}

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
      grouping.push_back(word.str());
      word.str("");
      word.clear();

      parsed.insert(std::make_pair(current_parsed_index, grouping));
      grouping.clear();
      ++current_parsed_index;

      if (i + 1 < expand_string.length() && expand_string[i + 1] != '{') {
        const int index = expand_string.find('{', i + 1);

        std::ostringstream delimeter;
        if (index == std::string::npos) {
          for (size_t j = i + 1; j < (expand_string.length() - (i + 1)); ++j) {
            delimeter << expand_string[j];
          }
          parsed.insert(std::make_pair(
              current_parsed_index, std::vector<std::string>{delimeter.str()}));
          ++current_parsed_index;
          break;
        }

        for (size_t j = i + 1; j < index; ++j) {
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

std::vector<std::string> AppendSubgroup(
    int i, const std::string &leading_value,
    const std::unordered_map<int, std::vector<std::string>> &parsed) {
  const auto can_go_deeper = parsed.find(i + 1);
  if (can_go_deeper != parsed.end()) {
    const auto val = parsed.at(i);
    for (const auto sub : val) {
      AppendSubgroup(i + 1, sub, parsed);
    }
  }

  std::vector<std::string> ret;
  const auto v = parsed.at(i);

  for (const std::string value : v) {
    ret.push_back(leading_value + value);
  }

  return ret;
}

std::vector<std::vector<std::string>> BraceExpansion(
    const std::unordered_map<int, std::vector<std::string>> &parsed) {
  const auto zero_index = parsed.find(0);
  std::string prefix = "";
  if (zero_index != parsed.end()) {
    prefix = parsed.at(0)[0];
  }

  auto starter = parsed.at(1);
  std::vector<std::vector<std::string>> ret;
  for (const auto subval : starter) {
    if (prefix != "") {
      ret.push_back(std::vector<std::string>{prefix + subval});
    } else {
      ret.push_back(std::vector<std::string>{subval});
    }
  }

  for (size_t i = 2; i < parsed.size(); ++i) {
    const auto values = parsed.at(i);

    for (const auto value : values) {
      for (size_t j = 0; j < ret.size(); ++j) {
        ret[j][0] = ret[j][0] + value;
      }
    }
  }

  return ret;
}

int main() {
  const std::string expand_string = "-------{1,2,3}-{4,5,6}-{7,8,9}";
  const std::unordered_map<int, std::vector<std::string>> parsed =
      ParseParameters(expand_string);

  const auto out = BraceExpansion(parsed);

  for (const auto vec : out) {
    std::cout << p_vec(vec) << std::endl;
  }
}