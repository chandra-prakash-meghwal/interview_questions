def bubble_sort(a):
    n = len(a)
    c = 0
    for i in range(n):
        c += 1
        swap_flag = False
        for j in range(1, n-i):
            # print(a[j], a[j-1])
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap_flag = True
        
        if not swap_flag:
            break
        print(c, a)
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
        print(a)
    return a


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        curr = a[i]
        prev = i-1
        while prev >= 0 and a[prev] > curr:
            a[prev+1] = a[prev]
            prev -= 1
        a[prev+1] = curr
        print(a)
    return a



def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    i,j = 0,0
    sorted_arr = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
    sorted_arr.extend(left_arr[i:])
    sorted_arr.extend(right_arr[j:])
    return sorted_arr



def quick_sort(arr, low, high):
    if low < high:
        p = arr[low]
        i = low+1
        j = high
        while True:
            while i<=j and arr[i]<p:
                i+=1
            while i<=j and arr[j]>p:
                j-=1
            if i<=j:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)


a = [4,5,1,2,6,3]
# print(bubble_sort(a))
# print(selection_sort(a))
# print(insertion_sort(a))
# print(merge_sort(a))
quick_sort(a, 0, len(a)-1)
print(a)
