class TrieNode:
    def __init__(self):
        self.children = {}  # Diccionario de hijos
        self.count=0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            # Incrementa el conteo en cada nodo visitado
            current_node.count += 1  

    def count(self, word):
        # retorna el valor de count acumulado de cada prefijo de word
        current_node = self.root
        total_count=0
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
                total_count+=current_node.count
            else:
                break
        return total_count
        

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        # Imprimir el valor del nodo
        if node.value:
            print(' ' * level + node.value, node.count)
        # Recorrer los hijos
        for child in node.children.values():
            self.display(child, level + 1)

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.count(word) for word in words]
        
sol=Solution()
words=["qtcqcmwcin","vkjotbrbzn","eoorlyfche","eoorlyhn","eoorlyfcxk","qfnmjilcom","eoorlyfche","qtcqcmwcnl","qtcqcrpjr"]
print(sol.sumPrefixScores(words))
