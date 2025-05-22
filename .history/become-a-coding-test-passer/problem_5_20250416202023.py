def solution(arr1, arr2):
    def cal_matrix(arr1, arr2):
        return sum([arr1[i] * arr2[i] for i in range(len(arr1))])
    chg_arr2 = [pair for pair in zip(* arr2)]
    answer = []
    for i in range(len(arr1)):
        inner_arr = []
        for j in range(len(chg_arr2)):
            inner_arr.append(cal_matrix(arr1[i], chg_arr2[j]))
        answer.append(inner_arr)
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
solution(arr1, arr2)

def solution(arr1, arr2)