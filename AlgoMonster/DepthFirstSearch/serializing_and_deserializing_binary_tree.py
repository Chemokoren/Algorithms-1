"""
Serializing and Deserializing Binary Tree

Given a binary tree, write a serialize function that converts the tree into a string and 
a deserialize function that converts a string to a binary tree. You may serialize the tree 
into any string representation you want as long as it can be deseralized.

Explanation

To serialize, we can simply do a DFS and append the node value to the string. We need to encode
null nodes too since otherwise we wouldn't be able to tell if we have reached leaf nodes when 
we deserialize. We use x here as a placeholder for the null node.

To deserialize, we split the string into tokens and consume them. For each token we create a 
new node using token value. When we see an x we know we reached the leaf and return.

Serialize

"""

class Node:

    def __init__(self, val, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right


def serialize(root):

    res = []

    def dfs(root):

        if not root:

            res.append('x')

            return

        res.append(root.val)

        dfs(root.left)

        dfs(root.right)

    dfs(root)

    return ' '.join(res)


def deserialize(s):

    def dfs(nodes):

        val = next(nodes)

        if val == 'x': return

        cur = Node(int(val))

        cur.left = dfs(nodes)

        cur.right = dfs(nodes)

        return cur

    # create an iterator that returns a token each time we call `next`

    return dfs(iter(s.split()))


if __name__ =="__main__":

    # driver code, do not modify

    def build_tree(nodes):

        val = next(nodes)

        if not val or val == 'x': return

        cur = Node(val)

        cur.left = build_tree(nodes)

        cur.right = build_tree(nodes)

        return cur

    def print_tree(root):

        if not root: 

            yield "x"

            return

        yield str(root.val)

        yield from print_tree(root.left)

        yield from print_tree(root.right)

    root = build_tree(iter(input().split()))

    new_root = deserialize(serialize(root))

    print(' '.join(print_tree(new_root)))