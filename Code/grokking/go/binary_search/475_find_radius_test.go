package binary_search

import (
	"testing"
)

func findRadius(houses []int, heaters []int) int {
	return 0
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func TestFindRadius(t *testing.T) {
	//if findRadius([]int{1, 5}, []int{2}) != 3 {
	//	t.Fail()
	//}
	//
	//if findRadius([]int{1, 2, 3}, []int{2}) != 1 {
	//	t.Fail()
	//}

	//if findRadius([]int{1, 2, 3, 4}, []int{1, 4}) != 1 {
	//	t.Fail()
	//}

	if findRadius([]int{1}, []int{1, 2, 3, 4}) != 1 {
		t.Fail()
	}
	//
	//if findRadius([]int{1, 2, 3, 5, 15}, []int{2, 30}) != 13 {
	//	t.Fail()
	//}
}
