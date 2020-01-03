# Merge sort exercise

counter = 0
def merge(left, right):
    i, j = 0,0
    merged_array = []
    global counter
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
            counter += 1
    while i < len(left):
        merged_array.append(left[i])
        i += 1
            
    while j < len(right):
        merged_array.append(right[j])
        j += 1
        
    return merged_array
    
def merge_sort(array):
    if len(array) <= 1:
        return array
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    return merge(left, right)
    

    
n = int(input())
array = list(map(int, input().split(' ')))
merge_sort(array)
print(counter)
