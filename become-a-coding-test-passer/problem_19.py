def solution(string_list, query_list):
    m = 10000000007
    result_list = []
    def check_in_hash(char_v, d):
        hash_v, p_v  = 0, 1
        for chr_s in char_v:
            hash_v += ((ord(chr_s) - 96) * p_v ) % m 
            p_v *= 31
        hash_v = hash_v % m
        if hash_v in d:
            return True
        else:
            return False
    
    d = {}
    for c in string_list:
        hash_v, p_v  = 0, 1
        for chr_s in c:
            hash_v += ((ord(chr_s) - 96) * p_v ) % m 
            p_v *= 31
        d[hash_v] = 1
    
    for c in query_list:
        result_list.append(check_in_hash(c, d))
    
    return result_list

solution(['apple', 'banana', 'cherry'], ['banana', 'kiwi', 'melon', 'apple'])