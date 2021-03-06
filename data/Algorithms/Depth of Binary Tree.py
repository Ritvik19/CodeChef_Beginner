from BinaryTree import Node

def depthBinaryTree(root):
    if root is None:
        return 0
    return max(depthBinaryTree(root.left), depthBinaryTree(root.right)) + 1

if __name__ == "__main__":
    root = Node(27)
    root.left = Node(14)
    root.right = Node(35)
    root.left.left = Node(10)
    root.left.right = Node(19)
    root.right.left = Node(31)
    root.right.right = Node(42)
    root.left.left.left = Node(45)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    print(f"Depth: {depthBinaryTree(root)}")
