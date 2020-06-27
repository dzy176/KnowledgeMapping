package binary_search

import (
	"fmt"
	"testing"
)

func findMagicIndex(nums []int) int {
	return helper(nums, 0, len(nums)-1)
}

func helper(nums []int, l, r int) int {
	if l == r {
		if nums[l] != l {
			return -1
		} else {
			return l
		}
	}
	m := (l + r) >> 1
	fmt.Println(nums, l, m, r)
	if nums[m] == m {
		ret := helper(nums, l, m)
		if ret != -1 {
			return ret
		} else {
			return m
		}
	} else {
		ret := helper(nums, l, m)
		if ret != -1 {
			return ret
		} else {
			return helper(nums, m+1, r)
		}
	}
}

func TestFindMagicIndex(t *testing.T) {
	if 1 != findMagicIndex([]int{1, 1, 1}) {
		t.Fail()
	}
}
