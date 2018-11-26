#include "./base.cc"

#include <iostream>
#include <set>
#include <vector>

class RemoveDuplicates : public LinkedList {
  void remove_duplicates() {
    LinkedList ll;
    auto temp(ll.head);
    std::set<int> values;
    while (temp) {
      values.insert(temp->_data);
      this->remove(temp->_data);
      temp = temp->_next;
    }

    for (const auto& it : values) {
      ll.insert(it);
    }
  }
};
