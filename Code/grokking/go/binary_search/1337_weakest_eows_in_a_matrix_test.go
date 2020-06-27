package binary_search

import (
	"reflect"
	"testing"
)

func kWeakestRows(mat [][]int, k int) []int {
	var res []int
	m := len(mat)
	n := len(mat[0])
	tmp := make([]int, m)

	// 计算每一层的和
	index := 0
	for index < m {
		s := count(mat[index])
		tmp[index] = s
		index++
	}

	// 依次寻找和为0， 1， 2， 3...的下标，直到找到前k个，返回
	i := 0
	for i <= n {
		j := 0
		for j < m {
			if tmp[j] == i {
				if k != 0 {
					res = append(res, j)
					k--
				} else {
					return res
				}
			}
			j++
		}
		i++
	}
	return res
}

// 二分法实现计数
func count(s []int) (res int) {
	if s[len(s)-1] == 1 {
		return len(s)
	}
	if s[0] == 0 {
		return 0
	}

	left, right := 0, len(s)-1
	for left <= right {
		mid := (left + right) >> 1
		if s[mid] == 1 {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}

func TestKWeakestRows(t *testing.T) {
	mat := [][]int{
		[]int{1, 1, 0, 0, 0},
		[]int{1, 1, 1, 1, 0},
		[]int{1, 0, 0, 0, 0},
		[]int{1, 1, 0, 0, 0},
		[]int{1, 1, 1, 1, 1},
	}
	res := kWeakestRows(mat, 3)
	if !reflect.DeepEqual(res, []int{2, 0, 3}) {
		t.Fail()
	}

	mat = [][]int{
		[]int{1, 1, 1, 1, 1},
		[]int{1, 1, 1, 1, 1},
		[]int{1, 1, 1, 1, 1},
	}
	res = kWeakestRows(mat, 1)
	if !reflect.DeepEqual(res, []int{0}) {
		t.Fail()
	}
}
