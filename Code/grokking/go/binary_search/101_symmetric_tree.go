package binary_search

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return judge(root.Left, root.Right)
}

func judge(t1, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	} else if t1 == nil && t2 != nil || t1 != nil && t2 == nil {
		return false
	} else {
		return t1.Val == t2.Val && judge(t1.Left, t2.Right) && judge(t1.Right, t2.Left)
	}
}
