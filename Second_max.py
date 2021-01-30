''' 
Second highest value without sorting
Time complexity: O(n) 
'''

def second_max(list):
    if len(list) >= 2:
        max = list[0]
        max_2 = list[1]
        
        if max < max_2:
            max, max_2 = max_2, max
        
        for i in range(2, len(list)-1):            
            if list[i] > max:
                max_2 = max
                max = list[i]
            elif list[i] < max and list[i] > max_2:
                max_2 = list[i]
                
        return max_2
            
    return -1




def second_max_sort(list_data):
    list_data = set(list_data)
    list_data = list(list_data)
    list_data.sort()
    
    if len(list_data) >= 2 :
        return list_data[-2]        
    return -1
    
    
    
