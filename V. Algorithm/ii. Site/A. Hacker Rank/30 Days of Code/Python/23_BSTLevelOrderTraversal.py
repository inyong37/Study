# Author      : inyong1020@gmail.com
# Date        : 2020-06-24-Wed.
# Description : Hacker Rank; 30 Days of code; Day 23: BST Level-Order Traversal.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -
# Reference   : https://www.hackerrank.com/challenges/30-binary-trees/forum
# Reference   : https://www.python.org/dev/peps/pep-0008/#pet-peeves
"""
Objective
Today, we're going further with Binary Search Trees. Check out the Tutorial tab for learning materials and an instructional video!

Task
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, , pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a BST:
The first line contains an integer,  (the number of test cases).
The  subsequent lines each contain an integer, , denoting the value of an element that must be added to the BST.

Output Format

Print the  value of each node in the tree's level-order traversal as a single line of  space-separated integers.

Sample Input

6
3
5
4
7
2
1
Sample Output

3 2 5 1 4 7
Explanation

The input forms the following binary search tree:
BST.png

We traverse each level of the tree from the root downward, and we process the nodes at each level from left to right. The resulting level-order traversal is , and we print these data values as a single line of space-separated integers.
"""
import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        queue = [root] if root else []
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
