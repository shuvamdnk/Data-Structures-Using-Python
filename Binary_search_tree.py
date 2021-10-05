class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def min_ele(self):
        r = self.left
        while r.left is not None:
            r = r.left

        return r.data

    def max_ele(self):
        r = self.right
        while r.right is not None:
            r = r.right

        return r.data

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val = self.right.min_ele()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))

    numbers_tree = build_tree([17, 4, 1, 20, 17, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",
          numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:",
          numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:",
          numbers_tree.post_order_traversal())
    print("Sweden is in the list? ", numbers_tree.search(17))
    print("Min element : ", numbers_tree.min_ele())
    print("Max element : ", numbers_tree.max_ele())
    numbers_tree.delete(23)

    print("In order traversal gives this sorted list:",
          numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:",
          numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:",
          numbers_tree.post_order_traversal())
