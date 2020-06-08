package binary_search

import (
	"fmt"
	"testing"
)

func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}

	left, right := 0, len(nums)-1
	for left <= right {
		mid := (left + right) >> 1
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			return mid
		}
	}
	return -1
}

func TestSearch(t *testing.T) {
	nums := []int{-1, 0, 3, 5, 9, 12}
	res := search(nums, 9)
	fmt.Println(res)
	if res != 4 {
		t.Fail()
	}
}
