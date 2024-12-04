from sys import stdin
input = stdin.readline


def merge_and_count(arr, tmp, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inv_count = 0
    
    inv_count += merge_and_count(arr, tmp, left, mid)
    inv_count += merge_and_count(arr, tmp, mid + 1, right)
    
    inv_count += merge(arr, tmp, left, mid, right)
    
    return inv_count


def merge(arr, tmp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
            inv_count += mid + 1 - i
        k += 1
    
    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = tmp[i]
    
    return inv_count


length = int(input())
nums = list(map(int, input().split()))

temp = [0] * length
swap_count = merge_and_count(nums, temp, 0, length - 1)
print(swap_count)
