import math


# Bubble sort
arr = [2,5,1,3,18,20,9]

def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                flag = True 
                arr[i],arr[i+1] = arr[i+1], arr[i]
    return arr

# Merge sort
arr = [2,5,1,3,18,20,9,13,4]

def merge(a1, a2):
    i = 0
    j = 0
    result = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1

    while i < len(a1):
        result.append(a1[i])
        i += 1

    while j < len(a2):
        result.append(a2[j])
        j += 1

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2

    a1 = merge_sort(arr[:mid])
    a2 = merge_sort(arr[mid:])

    arr = merge(a1, a2)

    return arr

# Quick Sort
arr = [2,5,1,3,18,20,9,13,4]

def quicksort(arr, low, high):
    if len(arr)==1:
        return arr

    pivot = arr[(low+high)//2]

    i = low
    j = high
    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if j > low:
        quicksort(arr, low, j)

    if high > i:
        quicksort(arr, i+1, high)

    return arr

quicksort(arr, 0, len(arr)-1)

# Solution Leetcode 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False

        new_s = sorted(s)
        new_t = sorted(t)

        for i in range(len(new_s)):
            if new_s[i] != new_t[i]:
                return False

        return True
    
    def maxCoins(self, piles: list[int]) -> int:
        num_triplet = len(piles)//3
        bob_indx = len(piles) - num_triplet
        new_piles = sorted(piles,reverse=True)[:bob_indx]
        value = 0

        for index in range(len(new_piles)):
            if (index%2 != 0):
                print("Your index {}".format(index))
                value += new_piles[index]

        return value
                
s = "anagram" 
t = "nagaram" 
a = Solution()           
a.isAnagram(s,t)
a.maxCoins([9,8,7,6,5,1,2,3,4])

        

