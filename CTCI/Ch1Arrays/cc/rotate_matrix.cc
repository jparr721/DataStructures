#include <cstdlib>
#include <iostream>
#include <vector>

class RotateMatrix {
  public:
    void rotate_matrix(std::vector<std::vector<int>>& matrix) {
      for (auto i = 0u; i < 5; ++i) {
        for (auto j = 0u; j < 5; ++j) {
          auto temp = matrix[i][j];
          matrix[i][j] = matrix[4 - j][i];
          matrix[4 - j][i] = temp;
        }
      }
    }

    void print(const std::vector<std::vector<int>>& matrix) {
      for (auto i = 0u; i < matrix.size(); ++i) {
        for (auto j = 0u; j < matrix[i].size(); ++j) {
          std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
      }
    }
};


int main() {
  RotateMatrix rm;
  std::vector<std::vector<int>> matrix(5, std::vector<int>(5, 0));
  for (auto i = 0u; i < matrix.size(); ++i) {
    for (auto j = 0u; j < matrix[i].size(); ++j) {
      matrix[i][j] = rand() % 10;
    }
  }
  std::cout << "Before" << std::endl;
  rm.print(matrix);
  std::cout << "After" << std::endl;
  rm.rotate_matrix(matrix);
  rm.print(matrix);

  return EXIT_SUCCESS;
}
