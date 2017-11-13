# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# 208. Implement Trie (Prefix Tree)
# status=done

class Node(object):
    def __init__(self, value, terminal=False):
        self.value = value
        self.chars = {}
        self.terminal = terminal

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cursor = self.node
        for c in word:
            if c not in cursor.chars:
                node = Node(c)
                cursor.chars[c] = node
            cursor = cursor.chars[c]
        cursor.terminal = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cursor = self.node
        for c in word:
            if c not in cursor.chars:
                return False
            cursor = cursor.chars[c]

        return cursor.terminal

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cursor = self.node
        for c in prefix:
            if c not in cursor.chars:
                return False
            cursor = cursor.chars[c]

        return True


def run_suite(commands, args):
    obj = Trie()

    return [
        getattr(obj, cmd)(arg) for cmd, arg in zip(commands, args)
    ]


print(run_suite(
    ["insert","search","search","insert","search","insert","search"],
    [["abc"],["abc"],["ab"],["ab"],["ab"],["ab"],["ab"]]
))
