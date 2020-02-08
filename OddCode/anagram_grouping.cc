#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

int sum_string(const std::string input) {
  int sum = 0;

  for (const char letter : input) {
    sum += letter;
  }

  return sum;
}

std::vector<std::string>
pq_to_vec(std::priority_queue<std::pair<int, std::string>> &max_heap) {
  std::vector<std::string> max_heap_attrs;

  while (!max_heap.empty()) {
    max_heap_attrs.push_back(max_heap.top().second);
    max_heap.pop();
  }

  return max_heap_attrs;
}

std::vector<std::string>
GroupAnagrams(const std::vector<std::string> &ungrouped_anagrams) {
  std::priority_queue<std::pair<int, std::string>> max_heap;

  for (const std::string anagram : ungrouped_anagrams) {
    max_heap.push(std::pair<int, std::string>(sum_string(anagram), anagram));
  }

  return pq_to_vec(max_heap);
}

void p_vec(const std::vector<std::string> &input) {
  for (const auto &val : input) {
    std::cout << val << std::endl;
  }
}

int main() {
  const std::vector<std::string> anagrams{"abc", "test", "vac", "bac", "london",
                                          "cba", "cav",  "lon", "pst"};

  std::vector<std::string> grouped_anagrams = GroupAnagrams(anagrams);

  p_vec(grouped_anagrams);
}