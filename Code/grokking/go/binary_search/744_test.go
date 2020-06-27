package binary_search

import (
	"testing"
)

func nextGreatestLetter(letters []byte, target byte) byte {
	left, right := 0, len(letters)-1
	var mid int
	for left+1 < right {
		mid = (right-left)>>1 + left
		if letters[mid] > target {
			right = mid
		} else if letters[mid] > target {
			left = mid
		} else {
			left = mid
		}
	}
	if letters[left] > target {
		return letters[left]
	} else {
		if letters[right] > target {
			return letters[right]
		} else {
			return letters[(right+1)%len(letters)]
		}
	}
}

func TestNextGreatestLetter(t *testing.T) {
	//letters, target := []byte{'c', 'f', 'j'}, byte('a')
	//if nextGreatestLetter(letters, target) != byte('c') {
	//	t.Fail()
	//}
	//
	//letters, target = []byte{'c', 'f', 'j'}, byte('c')
	//if nextGreatestLetter(letters, target) != byte('f') {
	//	t.Fail()
	//}

	letters, target := []byte{'e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 'n'}, byte('e')
	if nextGreatestLetter(letters, target) != byte('n') {
		t.Fail()
	}
}
