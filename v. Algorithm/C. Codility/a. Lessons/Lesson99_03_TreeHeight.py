# 100% https://app.codility.com/demo/results/trainingUQDZU6-GDJ/

from extratypes import Tree  # library with types used in the task

def get_height(sub_tree):
    if sub_tree == None:
        return 0
    else:
        return max(get_height(sub_tree.l), get_height(sub_tree.r)) + 1

def solution(T):
    return max(get_height(T.l), get_height(T.r))
