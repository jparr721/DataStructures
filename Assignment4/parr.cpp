#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main() {
    std::ifstream inFile;
    std::ofstream outFile;
    std::string word;
    inFile.open("input.txt");
    outFile.open("output.txt");
    std::string s[word.length()];
    int counter = 0;
    while (inFile >> word) {
        outFile << word << " ";
        std::cout << word << std::endl;
        for (int i = 0; i < 23; ++i) {
            s[i] = word;
        }
    }
    for (int i = 0; i < 23; ++i) {
        std::cout << s[i] << " " << std::flush;
    }
    inFile.close();
    outFile.close();
    return 0;
}

