# coding=utf-8

# 为0,left与middle交换，右移； 为1，middle右移； 为2，right左移

def dutch_flag_sort(arr):
    left, middle, right = 0, 0, len(arr)-1
    while middle <= right:
        if arr[middle] == 0:
            arr[middle], arr[left] = arr[left], arr[middle]
            left += 1
            middle += 1
        elif arr[middle] == 1:
            middle += 1
        else:
            arr[middle], arr[right] = arr[right], arr[middle]
            right -= 1

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)

main()