class SortTree:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def insert_val(self, _value):
        if _value < self.value:
            if self.left is None:
                self.left = SortTree(_value)
            else:
                self.left.insert_val(_value)
        else:
            if self.right is None:
                self.right = SortTree(_value)
            else:
                self.right.insert_val(_value)


def display(_node):
    return list(filter(None, [i for b in [
        display(_node.left) if isinstance(_node.left, SortTree) else [getattr(_node.left, 'value', None)], [_node.value],
        display(_node.right) if isinstance(_node.right, SortTree) else [getattr(_node.right, 'value', None)]] for i in b]))



