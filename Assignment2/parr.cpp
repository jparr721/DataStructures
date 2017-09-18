#include<iostream>
#include<vector>
#include"MyStack.h"

template <typename Object>
void MyStack::push(const Object & obj) {
    MyStack::elements.push_back(obj);
}

void MyStack::pop() {
    MyStack::elements.pop_back();
}

template <typename Object>
Object MyStack::top() const {
    MyStack::elements.front();
}

bool MyStack::empty() const {
    return MyStack::elements.size() >= 1;
}

int MyStack::GetSize() const {
    return MyStack::elements.size();
}

