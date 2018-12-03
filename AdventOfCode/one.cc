#include <fstream>
#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

class Frequencies {
  public:
    int frequency_mapper(std::string infile) {
      std::unordered_map<int, int> counts;
      std::ifstream in(infile);
      std::vector<int> the_goods;

      for (std::string goodies; std::getline(in, goodies);) {
        if (goodies.substr(0, 1) == "+") {
          the_goods.push_back(std::stoi(goodies.substr(1)));
        } else {
          the_goods.push_back(std::stoi(goodies));
        }
      }

      int freq = 0;
      for (;;) {

        for (const int& value : the_goods) {
          freq += value;
          if (counts.count(freq) < 1) {
            counts[freq]++;
          } else {
            std::cout << "Duplicate found " << freq << std::endl;
            return freq;
            break;
          }
        }
      }
    }
};

int main(int argc, char** argv) {
  Frequencies f;

  int oh_yeah = f.frequency_mapper("data1.txt");

  std::cout << oh_yeah << std::endl;

  return EXIT_SUCCESS;
}
