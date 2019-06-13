#include <iostream>
#include <utility>
#include <vector>

struct node {
  // Where it is in the tree
  int level;
  // Value of the node
  int value;
  // Weight up to this point
  int weight;
  // Max value
  int bound;
};

class Knapsack {
  public:
    Knapsack(const std::vector<std::pair<int, int>>& inputs) : inputs_(inputs) {};

    std::pair<std::vector<int>, int> solve(int n, int k);

  private:
    // <0> - value, <1> - weight
    std::vector<std::pair<int, int>> inputs_;
    std::vector<node> graph;

    int calculate_optimistic_evaluation(int level);
    int calculate_bound(const node& v, int n, int k);
    std::vector<std::pair<int, int>> select_from_on(const std::vector<int>& on);
};
