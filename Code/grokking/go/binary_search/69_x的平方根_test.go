package binary_search

import "testing"

func mySqrt(x int) int {
	left, right := 0, x
	for left+1 < right {
		mid := (left + right) >> 1
		if mid*mid < x {
			if (mid+1)*(mid+1) == x {
				return mid + 1
			}
			if (mid+1)*(mid+1) > x {
				return mid
			}
			left = mid
		} else {
			right = mid
		}
	}
	if left*left >= x {
		return left
	} else {
		if right*right == x {
			return right
		} else {
			return left
		}
	}
}

func TestMySqrt(t *testing.T) {
	if 2 != mySqrt(4) {
		t.Fail()
	}
	if 2 != mySqrt(8) {
		t.Fail()
	}
}
