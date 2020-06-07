package binary_search

import "testing"

func missingNumber(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	// right需为长度-1, 否则会发生下标越界
	left, right := 0, len(nums)-1
	for left <= right {
		mid := (left + right) >> 1

		if nums[mid] == mid {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}

func TestMissingNumber(t *testing.T) {
	nums := []int{0}
	n := missingNumber(nums)
	if n != 3 {
		t.Fail()
	}
}
