A = [' ა', ' ბ', ' გ', ' დ', ' ე', ' ვ', ' ზ']
f = ['97', '29', '43', '96', '91', '22', '51']


# given the list of characters and frequencies of each character
# build a huffman tree

# sort the list of characters by frequency
# build a tree from the lowest frequency characters
# repeat until there is only one tree left


def sort_list_and_frequency(characters, frequencies):
    """inplace sort characters and frequencies by frequency"""
    for i in range(len(frequencies)):
        for j in range(i, len(frequencies)):
            if frequencies[i] > frequencies[j]:
                frequencies[i], frequencies[j] = frequencies[j], frequencies[i]
                characters[i], characters[j] = characters[j], characters[i]


class Tree:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __le__(self, other):
        return self.frequency <= other.frequency

    def __ge__(self, other):
        return self.frequency >= other.frequency

    def __ne__(self, other):
        return self.frequency != other.frequency

    def __add__(self, other):
        new_tree = Tree(None, self.frequency + other.frequency)
        new_tree.left = self
        new_tree.right = other
        return new_tree

    def __radd__(self, other):
        new_tree = Tree(None, self.frequency + other.frequency)
        new_tree.left = other
        new_tree.right = self
        return new_tree

    def __iadd__(self, other):
        self.frequency += other.frequency
        self.left = self
        self.right = other
        return self

    def __isub__(self, other):
        self.frequency -= other.frequency
        return self

    def __sub__(self, other):
        new_tree = Tree(None, self.frequency - other.frequency)
        new_tree.left = self
        new_tree.right = other
        return new_tree

    def __rsub__(self, other):
        new_tree = Tree(None, self.frequency - other.frequency)
        new_tree.left = other
        new_tree.right = self
        return new_tree

    def __imul__(self, other):
        self.frequency *= other.frequency
        return self

    def __mul__(self, other):
        new_tree = Tree(None, self.frequency * other.frequency)
        new_tree.left = self
        new_tree.right = other
        return new_tree

    def __rmul__(self, other):
        new_tree = Tree(None, self.frequency * other.frequency)
        new_tree.left = other
        new_tree.right = self
        return new_tree

    def __idiv__(self, other):
        self.frequency /= other.frequency
        return self

def build_huffman_tree(characters, frequencies):
    # sort the list by frequency
    # create a list of trees
    # while there is more than one tree
    #   get the two trees with the lowest frequency
    #   create a new tree with those two trees as children
    #   add the new tree to the list of trees
    # return the list of trees
    sort_list_and_frequency(characters, frequencies)
    trees = []
    for i in range(len(characters)):
        trees.append(Tree(characters[i], frequencies[i]))



if __name__ == "__main__":
    sort_list_and_frequency(A, f)
    print(f"Sorted characters: {A}")
    print(f"Sorted frequencies: {f}")
