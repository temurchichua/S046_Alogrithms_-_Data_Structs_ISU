# Huffman Decoding Algorithm

# Write Python code that takes the Huffman code and encoded string as an input and gives the decoded word as an output.
# Hint: Steps of Huffman Decoding are:
class HuffmanNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


# Build the corresponding binary tree.
def build_tree(sorted_codes: tuple[list]) -> HuffmanNode:
    """
    Build the Huffman tree from the Huffman code
    :param sorted_codes: list of huffman code tuples (symbol, code)
    :return: Huffman tree
    """
    # create the root node
    root = HuffmanNode()

    for symbol, code in sorted_codes:
        node = root
        for bit in code:
            if bit == "0":
                if node.left is None:
                    node.left = HuffmanNode()
                node = node.left
            else:
                if node.right is None:
                    node.right = HuffmanNode()
                node = node.right
        node.data = symbol
    return root


def huffman_decoding(data: str, tree: HuffmanNode):
    """
    Decode the data using Huffman tree
    :param data: encoded data
    :param tree: Huffman tree
    :return: decoded data
    """
    decoded_data = ""
    node = tree
    for bit in data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.is_leaf():
            decoded_data += node.data
            node = tree
    return decoded_data


if __name__ == "__main__":
    # Input:
    huffman_code = {"a": "10100",
                    "b": "100",
                    "c": "1011",
                    "d": "11",
                    "e": "01",
                    "f": "10101",
                    "g": "00"}

    codeword = "1011101000001"
    # Output: cage

    # sort by frequencies
    sorted_codes = sorted(
        huffman_code.items(),
        key=lambda t: len(t[1])
    )

    huffman_tree = build_tree(sorted_codes)
    decoded = huffman_decoding(codeword, huffman_tree)
    print(decoded)
