#include <iostream>
#include <memory>
#include <vector>

/**
 * Mostly bulletproof singly linked list
 * with built in memory safety for use with
 * chapter 2 problems
 */
class Node {
  public:
    int _data;
    std::shared_ptr<Node> _next;

    explicit Node(int data) : _data(data), _next(nullptr) {}
};

class LinkedList {
  public:
    std::shared_ptr<Node> head;

    LinkedList() : head(nullptr) {}

    void print() const {
      std::shared_ptr<Node> temp(head);
      while (temp) {
        std::cout << temp->_data << std::endl;
        temp = temp->_next;
      }
    }

    void insert(int data) {
      std::shared_ptr<Node> n(new Node(data));
      if (head == nullptr) {
        head = n;
      } else {
        n->_next = head;
        head = n;
      }
    }

    void remove(const int value) {
      auto temp(head);
      while (temp) {
        if (temp->_data == value) {
          temp->_next = temp->_next->_next;
          break;
        }
        temp = temp->_next;
      }
    }
};
