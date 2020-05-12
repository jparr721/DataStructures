from __future__ import annotations
from typing import List


class Node(object):
    def __init__(self, value: str, children: List[Node], is_word: bool):
        self.is_word = is_word
        self.value = value
        self.children = children

    def __repr__(self):
        return (
            f"value: {self.value}\n"
            + f"children: {self.children}\n"
            + f"is_word: {self.is_word}\n"
        )


class Trie:
    def __init__(self, root: Node):
        self.root = root

    def insert(self, word: str) -> bool:
        word = word.lower()

        # Start at root and see if the prefix exists
        current_node = self.root

        for i, char in enumerate(word):
            if i == 0:
                for j, node in enumerate(current_node.children):
                    if node.value == char:
                        current_node = current_node.children[j]
                        break
                else:
                    # If we are at the end of the word is_word is true
                    is_word = True if i == len(word) - 1 else False
                    current_node.children.append(Node(char, [], is_word))
                    current_node = current_node.children[-1]
            if i > 0:
                # If it exists, check the next etc..
                if char == current_node.value:
                    continue

                if char != current_node.value:
                    for j, node in enumerate(current_node.children):
                        if node.value == char:
                            current_node = current_node.children[j]
                            break
                    else:
                        # If we are at the end of the word is_word is true
                        is_word = True if i == len(word) - 1 else False
                        current_node.children.append(Node(char, [], is_word))
                        current_node = current_node.children[-1]

    def search(self, word: str) -> bool:
        word = word.lower()

        current_node = self.root

        for i, char in enumerate(word):
            if i == 0:
                for j, node in enumerate(current_node.children):
                    if node.value == char:
                        current_node = current_node.children[j]
                        break
                else:
                    return False
            if i > 0:
                # If it exists, check the next etc..
                if char == current_node.value:
                    continue

                if char != current_node.value:
                    for j, node in enumerate(current_node.children):
                        if node.value == char:
                            current_node = current_node.children[j]
                            break
                    else:
                        return False

        return current_node.is_word


if __name__ == "__main__":
    root = Node("", [], False)
    trie = Trie(root)
    trie.insert("dap")
    trie.insert("data")
    print(trie.search("dap"))
    print(trie.search("pad"))
    trie.insert("pad")
    print(trie.search("pady"))

    print(root.children[0].children[0].children)
