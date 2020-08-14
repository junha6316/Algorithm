
class Node(object):
    def __init__(self, key, count=0):
        self.key = key
        self.child ={}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] =True

    def search(self, word):
        cur= self.head
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
            if '*' in cur.child:
                return True




a = Trie()
a.insert('abc')


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children= {}

class Trie(object):
    def __init__(self):
        self.head =Node(key=None, data=None)

    def insert_string(self, input_string):
        cur_node = self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                cur_node.children[c]= Node(key=c)
            cur_node = cur_node.children[c]
        cur_node.data = input_string

    def

dic ={}
for word in words:
    for c in word:
        if not dic.get[c]:
            dic[c] = c.





