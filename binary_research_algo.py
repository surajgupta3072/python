def num_search(search_num, arr, start, end):
    while start<=end:
        middle = int((start + end)/2)
        if arr[middle]==search_num:
            return middle
        elif arr[middle]>search_num:
            end=int(middle-1)
        else:
            start= int(middle+1)
        
        


n = int(input("Enter number of elements of array: "))
arr=[]
for i in range(0,n):
    element_arr = int(input(f"The {i+1}st element in array in sorted manner is: "))
    arr.append(element_arr)


search_num = int(input("Which number do you want to search: "))

  
print(num_search(search_num, arr, 0, n))
   
