package binary_search

import (
	"reflect"
	"sort"
	"testing"
)

func intersection(nums1 []int, nums2 []int) []int {
	var res []int
	sort.Ints(nums1)
	sort.Ints(nums2)
	if binarySearch(nums1, nums2[0]) {
		res = append(res, nums2[0])
	}
	for i := 1; i < len(nums2); i++ {
		if nums2[i] == nums2[i-1] {
			continue
		}
		if binarySearch(nums1, nums2[i]) {
			res = append(res, nums2[i])
		}
	}
	return res
}

func binarySearch(nums1 []int, target int) bool {
	left, right := 0, len(nums1)-1
	for left+1 < right {
		mid := (right-left)>>1 + left
		if nums1[mid] > target {
			right = mid
		} else {
			left = mid
		}
	}
	if nums1[left] == target || nums1[right] == target {
		return true
	}
	return false
}

func TestIntersection(t *testing.T) {
	var nums1, nums2 []int
	nums1 = []int{1, 2, 2, 1}
	nums2 = []int{2, 2}
	if !reflect.DeepEqual([]int{2}, intersection(nums1, nums2)) {
		t.Fail()
	}

	nums1 = []int{4, 9, 5}
	nums2 = []int{9, 4, 9, 8, 4}
	if !reflect.DeepEqual([]int{4, 9}, intersection(nums1, nums2)) {
		t.Fail()
	}
}
