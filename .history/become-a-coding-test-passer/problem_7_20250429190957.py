dirs = "ULURRDLLU"
def solution(dirs):
    answer = 0
    first_dir_dict ={}
    def check_dir(start_node, direction):
        start_x, start_y = start_node
        if direction == "U":
            next_x, next_y = start_x, start_y + 1
        elif direction == "D":
            next_x, next_y = start_x, start_y - 1
        elif direction == "R":
            next_x, next_y = start_x + 1, start_y
        else:
            next_x, next_y = start_x - 1, start_y
            
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            direction_arr = [(start_x, start_y), (next_x, next_y)]
            first_dir_dict[direction_arr] = True
            return (next_x, next_y)
        else:
            return (start_x, start_y)
    
    curr_node = (0, 0)
    for direction_str in dirs:
        curr_node = check_dir(start_node=curr_node, 
                               direction=direction_str)
        
            
            
            
            
    
    return answer