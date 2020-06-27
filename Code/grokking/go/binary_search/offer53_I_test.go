package binary_search

import (
	"testing"
)

func search2(nums []int, target int) int {
	if 0 == len(nums) {
		return 0
	}
	left, mid, right := 0, 0, len(nums)-1
	for left+1 < right {
		mid = (left + right) >> 1
		if nums[mid] == target {
			right = mid
		} else if nums[mid] > target {
			right = mid
		} else {
			left = mid
		}
	}

	start := -1
	if nums[left] == target {
		start = left
	} else if nums[right] == target {
		start = right
	}
	if start == -1 {
		return 0
	}
	count := 1
	for start < len(nums)-1 {
		if nums[start] == nums[start+1] {
			start++
			count++
		} else {
			break
		}
	}
	return count
}

func TestSearch2(t *testing.T) {
	nums := []int{5}
	if 1 != search2(nums, 5) {
		t.Fail()
	}
}
