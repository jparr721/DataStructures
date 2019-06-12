#include "knapsack.h"
#include <stack>
#include <numeric>

node::node(int value, int weight) {
  value = value;
  weight = weight;
  left = nullptr;
  right = nullptr;
  selected = false;
}

void Knapsack::solve() {
  int best_optimistic_evaluation = 0;

  // Get our k and n values
  auto n = std::get<0>(inputs_[0]);
  auto k = std::get<1>(inputs_[0]);

  // Remove the top layer so we don't have to deal with it
  inputs_.erase(inputs_.begin());

  // Our mirror array to select/deselect values
  std::vector<int> on(inputs_.size(), 1);

  // Our split
  bool take = true;

  // Now, iterate through our inputs
  for (int i = 0; i < n - 1; ++i) {
    for (int j = 0; j <= 1; ++j) {
      take = j;

      // Go left
      if (take) {

        // Get our optimistic evaluation
        int optimistic_evaluation = calculate_optimistic_evaluation(on, i, n);

        // Get our vector of selected values
        auto relevant_values = select_from_on(on);

        // Calculate our total weight if we take this one
        int weight = calculate_weight(relevant_values);

        if (weight > k) {
          // If weight too heigh, exclude this value
          on[i] = 0;
        }

        // Discard this branch if optim value too low
        if (optimistic_evaluation < best_optimistic_evaluation) {
          // Flip the value in on just in case
          on[i] = !on[i];
        }

      } else { // Go right
        on[i] = 0;
      }
    }
  }
}

/// Calculate optimistic evaluation with relaxed value of k
int Knapsack::calculate_optimistic_evaluation(const std::vector<int>& on, int start, int end) {
  int sum;

  for (auto i = 0u; i < on.size(); ++i) {
    sum += std::get<0>(inputs_[i]);
  }

  return sum;
}

std::vector<std::pair<int, int>> Knapsack::select_from_on(const std::vector<int>& on) {
  std::vector<std::pair<int, int>> the_chosen_ones;
  for (auto i = 0u; i < on.size(); ++i) {
    if (on[i]) {
      the_chosen_ones[i] = inputs_[i];
    }
  }

  return the_chosen_ones;
}

/// Calculate the weight of a vector of pairs
int Knapsack::calculate_weight(const std::vector<std::pair<int, int>>& weights) {
  int sum = 0;

  for (const auto& weight : weights) {
    auto actual_weight = std::get<1>(weight);

    sum += actual_weight;
  }

  return sum;
}
