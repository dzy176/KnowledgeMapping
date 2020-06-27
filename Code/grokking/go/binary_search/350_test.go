package binary_search

func intersect(nums1 []int, nums2 []int) []int {
	m := map[int]int{}
	var res []int
	for _, v := range nums1 {
		_, ok := m[v]
		if ok {
			m[v] += 1
		} else {
			m[v] = 1
		}
	}
	for _, v := range nums2 {
		count, ok := m[v]
		if ok && count != 0 {
			res = append(res, v)
			m[v] -= 1
		}
	}
	return res
}
