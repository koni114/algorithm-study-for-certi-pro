"""
- 첫 번째 인수 lst 를 이용하여 이진 탐색 트리를 생성.
- 두 번째 인수 search_lst 에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인하여 True/False 를 담은 리스트 result 반환.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# 이진 탐색 트리 클래스
class BST:
    # 초기에 아무 노드도 없는 상태
    def __init__(self):
        self.root = None
    
    # root node 부터 시작해서 이진 탐색 트리 규칙에 맞는 위치에 새 노드 삽입.
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                if key < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break
    
    # 이진 탐색 규칙에 따라 특정값이 있는지 확인(루트 노드부터 시작)
    def search(self, key):
        curr = self.root
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                # 찾으려는 값이 현재 노드의 값보다 큰 경우 오른쪽 자식 노드로 이동
                curr = curr.right
        return curr
    

def solution(lst, search_list):
    bst = BST()
    for key in lst:
        bst.insert(key)
    
    result = []
    
    for search_val in search_list:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)
    return result

solution(
    lst=[5, 3, 8, 4, 2, 1, 7, 10],
    search_list=[1, 2, 5, 6]
)
        
        
solution(
    lst=[1, 3, 5, 7, 9],
    search_list=[2, 4, 6, 8, 10]
)