package binary_search

func arrangeCoins(n int) int {
	left := 0
	right := n
	for left <= right {
		mid := (left + right) >> 1
		sum := mid * (mid + 1) / 2
		if sum > n {
			right = mid - 1
		} else if sum < n {
			left = mid + 1
		} else {
			return mid
		}
	}
	return left - 1
}
