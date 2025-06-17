"""
첫 번째 인수 lst 를 이용하여 이진 탐색 트리를 생성.
두 번째 인수 search_lst 에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while curr: 
                if key < curr.key:
                    if not curr.left:
                        curr.left = Node(key)
                        break
                    else:
                        curr = curr.left
                else:
                    if not curr.right:
                        curr.right = Node(key)
                        break
                    else:
                        curr = curr.right
    
    def search(self, key):
        curr = self.root
        while curr:
            if curr.key == key:
                return True
            else:
                if key < curr.key:
                    curr = curr.left
                else:
                    curr = curr.right
        return False
                    
                
def solution(lst, search_lst):
    bst = BST()
    for v in lst:
        bst.insert(v)
    return [bst.search(v) for v in search_lst]

solution([1, 3, 5, 7, 9],
         [2, 4, 6, 8, 10])