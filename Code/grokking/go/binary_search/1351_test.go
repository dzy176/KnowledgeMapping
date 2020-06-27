package binary_search

import (
	"fmt"
	"testing"
)

func countNegatives(grid [][]int) int {
	var res int
	for i, v := range grid {
		if v[0] < 0 {
			res += len(v) * (len(grid) - i)
			return res
		} else {
			if v[len(v)-1] >= 0 {
				continue
			} else {
				res += binarySearch1351(v)
			}
		}
	}
	return res
}

func binarySearch1351(nums1 []int) int {
	left, right := 0, len(nums1)-1
	for left+1 < right {
		mid := (right-left)>>1 + left
		if nums1[mid] > 0 {
			left = mid
		} else if nums1[mid] < 0 {
			right = mid
		} else {
			left = mid
		}
	}
	if nums1[right] >= 0 {
		return 0
	} else {
		if nums1[left] < 0 {
			return len(nums1) - left
		} else {
			return len(nums1) - (left + 1)
		}
	}
}

func TestCountNegatives(t *testing.T) {
	var grid [][]int
	grid = [][]int{
		{4, 3, 2, -1},
		{3, 2, 1, -1},
		{1, 1, -1, -2},
		{-1, -1, -2, -3},
	}
	if countNegatives(grid) != 8 {
		fmt.Println(countNegatives(grid))
		t.Fail()
	}
}
