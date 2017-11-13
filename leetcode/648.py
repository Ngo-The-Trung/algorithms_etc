# https://leetcode.com/problems/replace-words/description/
# 648. Replace Words
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


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)

        result = []
        for word in sentence.split(" "):
            cursor = trie.node
            found = False
            for i in range(len(word)):
                c = word[i]
                if c not in cursor.chars:
                    break
                cursor = cursor.chars[c]
                if cursor.terminal:
                    result.append(word[:i + 1])
                    found = True
                    break
            if not found:
                result.append(word)
        # import pdb; pdb.set_trace()
        return " ".join(result)

s = Solution()
print s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
