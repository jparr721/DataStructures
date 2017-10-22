#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

template <class KTy, class Ty>
void PrintMap(std::map<KTy, Ty> map) {

    for (auto it = map.cbegin(); it != map.cend(); ++it)
        std::cout << it->first << ": " << it->second << std::endl;
}

int main(void) {
    static const char* fileName= "input.txt";

    std::map<std::string, unsigned int> wordCount; {
        std::ifstream inFile;
        inFile.open(fileName);

        // Should be open, but ya know...
        if (inFile.is_open()) {
            while (inFile.good()) {
                std::string word;
                inFile >> word;

                // Exclude some words
//                if (ispunct(wordCount[word]))
//                    wordCount.erase(word);

                if (strcmp(wordCount[word], "@"))
                    wordCount.erase(word);

                // check if word is already there
                if (wordCount.find(word) == wordCount.end()) {
                    wordCount[word] = 1;
                } else {
                    wordCount[word]++;
                }
            }
        }
        else {
            std::cerr << "Couldn't open file" << std::endl;
        }
        PrintMap(wordCount);
    }
}