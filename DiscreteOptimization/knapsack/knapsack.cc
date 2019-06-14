#include "knapsack.h"
#include <algorithm>
#include <fstream>
#include <memory>
#include <numeric>
#include <queue>

std::pair<std::vector<int>, int> Knapsack::solve(int n, int k) {
  // Sort by best ratio
  std::sort(inputs_.begin(), inputs_.end(),
      [&](const std::pair<int, int> a, const std::pair<int, int> b) {
        auto ratio_1 = std::get<0>(a) / std::get<1>(a);
        auto ratio_2 = std::get<0>(b) / std::get<1>(b);

        return ratio_1 < ratio_2;
      });

  int best_optimistic_evaluation = 0;
  std::queue<node> q;

  node dummy_node, v;
  dummy_node.weight = 0;
  dummy_node.value = 0;
  dummy_node.level = -1;

  // Fill our mirror list with values of 0
  std::vector<int> mirror_list(0, n);

  // Add our dummy node to the queue
  q.push(dummy_node);

  for (;!q.empty();) {
    // Get our value from the queue
    node u = q.front();
    q.pop();

    if (u.level == -1) {
      v.level = 0;
    }

    // Nowhere to go
    if (dummy_node.level == n - 1) {
      continue;
    }

    // Calculate now for the next layer
    v.level = dummy_node.level + 1;

    // Compute optimistic evaluation
    v.weight = dummy_node.weight + std::get<1>(inputs_[v.level]);
    v.value = dummy_node.value + std::get<0>(inputs_[v.level]);

    // Check weight and value
    if (v.value > best_optimistic_evaluation && v.weight <= k) {
      best_optimistic_evaluation = v.value;
    }

    // Check largest possible value
    v.bound = calculate_bound(v, n, k);

    // If we potentially can find a better solution,
    // add it to the queue
    if (v.bound > best_optimistic_evaluation) {
      q.push(v);
      mirror_list[v.level] = 1;
    }

    // Otherwise, use it without taking it
    v.weight = dummy_node.weight;
    v.value = dummy_node.value;

    // Now, bound as if it's zero
    v.bound = calculate_bound(v, n, k);

    // If it still manages to work, take it
    if (v.bound > best_optimistic_evaluation) {
      q.push(v);
      mirror_list[v.level] = 1;
    }
  }

  return std::make_pair(mirror_list, best_optimistic_evaluation);
}

int Knapsack::calculate_bound(const node& v, int n, int k) {
  if (v.weight >= k) {
    return 0;
  }

  int total_value = v.value;
  int total_weight = v.weight;

  int i = v.level + 1;

  while ((i < n) && (total_weight < k)) {
    // Get value and weight so we know the max
    total_weight += std::get<0>(inputs_[i]);
    total_value += std::get<1>(inputs_[i]);
    ++i;
  }

  // If weight goes over but we have levels left
  if (i < n) {
    total_value += (k - total_weight * (std::get<0>(inputs_[i]) / std::get<1>(inputs_[i])));
  }

  return total_value;
}

std::vector<std::string> split_string(std::string& str) {
  std::string word = "";
  std::vector<std::string> separated;

  for (const auto& s : str) {
    if (s == ' ') {
      separated.push_back(word);
      word = "";
    } else {
      word += s;
    }
  }

  return separated;
}

void read_file(const std::string& filename, int& n, int& k, std::vector<std::pair<int, int>>& vals) {
  int i = 0;
  std::ifstream file(filename);

  for (std::string line; getline(file, line); ++i) {
    std::vector<std::string> values = split_string(line);
    vals.push_back(std::make_pair(std::stoi(values[0]), std::stoi(values[1])));
  }
}

int main(int argc, char** argv) {
  std::shared_ptr<Knapsack> knapsack;

  std::vector<std::pair<int, int>> values;
  int n = 0;
  int k = 0;

  read_file(std::string(argv[1]), n, k, values);

  auto output = knapsack->solve(n, k);

  auto selected = std::get<0>(output);
  auto max_value = std::get<1>(output);

  for (const auto& v : selected) {
    std::cout << v << " ";
  }

  std::cout << std::endl;

  std::cout << max_value;

  return EXIT_SUCCESS;
}
