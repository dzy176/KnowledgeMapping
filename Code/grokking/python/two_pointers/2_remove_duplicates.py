# coding=utf-8

# 左指针指向非重复元素
# 右指针进行遍历
# 左指针与右指针指向的数字不一样，则左指针向右推进，且保存当前右指针的数值

def remove_duplicates(arr):
    left = 0

    for right in range(len(arr)):
        if arr[left] != arr[right]:
            arr[left+1] = arr[right]
            left += 1
    return left+1

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()