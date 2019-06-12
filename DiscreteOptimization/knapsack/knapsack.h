#include <iostream>
#include <utility>
#include <vector>

struct node {
  node(int value, int weight);
  bool selected;
  int value;
  int weight;
  int optimistic_evaluation;
  node* left;
  node* right;
};

class Knapsack {
  public:
    Knapsack(const std::vector<std::pair<int, int>>& inputs) : inputs_(inputs) {};

    void solve();

  private:
    std::vector<std::pair<int, int>> inputs_;
    std::vector<node> graph;

    int calculate_optimistic_evaluation(const std::vector<int>& on, int start, int end);
    int calculate_weight(const std::vector<std::pair<int, int>>& weights);
    std::vector<std::pair<int, int>> select_from_on(const std::vector<int>& on);
};
