import webbrowser
# ----------------------------------- Class Implementation Section -------------------------------
class trie_node: # This is Trie base implementation

    def __init__(self):

        self.LastWordCharacter = False
        self.children = {}

class trie_tree: # This is an object of previous class

    def __init__(self):

        self.root = trie_node()

    def insert(self, word:str):

        current = self.root
        for char in word: # checks if word's character exist or not : if exists the current node will be changed to them, if not then we'll make a node for them and finally the LWC value will be True.
            if char not in current.children:
                current.children[char] = trie_node()
            else:
                current = current.children[char]
        current.LastWordCharacter = True
        print("OK")

    def remove(self, word:str):

        current = self.root
        for char in word:
            if char not in current.children:
                return False
            else:
                del(current.children[char])
        print("OK")
            
    def search(self, word:str):

        current = self.root
        for char in word: # if the first chars are not in tree, it'll return False directly. Else, it would return the word existence status.
            if char in current.children:
                current = current.children[char]
            else:
                print("False")
                return False
        print("True")
        return current.LastWordCharacter
    
    def startsWith(self, prefix:str):

        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                print("False")
                return False
        print("True")
        return True
    
# ----------------------------------- Test Section ---------------------------------------------

"""
add = Trie.insert(["salam"])
delete = Trie.remove
find = Trie.search
pre = Trie.prefix
exit = exit()
Trie.insert(["salam"])
Trie.insert(["salome"])
Trie.insert(["salane"])
Trie.insert(["salad"])
Trie.search(["salad"])
Trie.search(["salome"])
Trie.search(["salaneh"])
Trie.remove(["salad"])
Trie.search(["salad"])
Trie.search(["salam"])
"""

# ------------------------------------ Getting Input ------------------------------------------

Trie = trie_tree()
print("Hey, this is a simple words search program(based on Trie/Prefix tree) which you can 'add', 'search' and 'delete' your words to it!")
while True:

    x = "Please enter your command(s): \n"
    a, b = map(str, input(x).split())
    if a == "add":
        Trie.insert([b])
    elif a == "find":
        Trie.search([b])
    elif a == "delete":
        Trie.remove([b])
    elif a == "sw":
        Trie.startsWith([b])
    elif a == "exit":
        quit()
    elif a == "open":
        webbrowser.open('https://github.com/EbrahimING')
        quit()
    else:
        print("Wrong command")
