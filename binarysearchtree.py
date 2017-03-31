# Lab 5
class Node:
    def __init__(self, key, val):
        self._key = key
        self._val = val
        self._left = None
        self._right = None

    def set_children(self, l, r):
        self._left = l
        self._right = r

    def data(self):
        return self._key, self._val

    def left_child(self):
        return self._left

    def right_child(self):
        return self._right
    

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        '''
        Public interface method to insert a key and value to the search tree.
        '''
        self.root = self.__insert(self.root, key, val)

    def __insert(self, v, key, val):
        '''
        Internal method to recursively decide where to insert a new node.
        Warning! This method has a bug, it does not behave according to specification!
        '''
        if v:
            v_key, x = v.data() # Ignoring x actually
            left = v.left_child()
            right = v.right_child()
            if key < v_key:
                left = self.__insert(left, key, val)
            else:
                right = self.__insert(right, key, val)
            v.set_children(left, right)
            return v
        else:
            return Node(key, val)

    def find(self, key):
        pass                    # To be implemented

    def remove(self, key):
        pass                    # To be implemented

    def size(self):
        pass                    # To be implemented

    def __str__(self):
        return str(self.root)

def main():
    credits = BinarySearchTree()
    credits.insert('DA3018', 7.5)
    credits.insert('DA2004', 7.5)
    credits.insert('DA2003', 6)
    print(credits)
    n = credits.size()          # n = 3
    hp = credits.find('DA3018') # set hp to 7.5
    credits.remove('DA2003')
    m = credits.size()          # m = 2

if __name__ == '__main__':
    main()    
