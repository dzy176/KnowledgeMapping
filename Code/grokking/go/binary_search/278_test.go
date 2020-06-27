package binary_search

func firstBadVersion(n int) int {
	left, right := 1, n
	for left+1 < right {
		mid := (left + right) >> 1
		if isBadVersion(mid) {
			right = mid
		} else {
			left = mid
		}
	}
	if isBadVersion(left) {
		return left
	}
	if isBadVersion(right) {
		return right
	}
	return n
}

func isBadVersion(int) bool {
	return true
}
