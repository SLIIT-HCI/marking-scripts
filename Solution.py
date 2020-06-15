def buildTree(p):
	global tree, count
	if p >= len(tree):
		return;
	else:
		buildTree((p+1)*2 - 1)
		buildTree((p+1)*2)
		tree[p] = count
		count+=1

def solution(h, input):
	global tree, count
	tree = [None] * ((2**h) - 1)
	count = 1
	buildTree(0)
	ans = []
	for x in input:
		if x in tree:
			p = tree.index(x)
			if p==0:
				ans.append(-1)
			else:
				ans.append(tree[(p-1)//2])
		else:
			ans.append(-1)
	return ans

print solution(5, [19,14,28])
print solution(3, [7,3,5,1])
print solution(3, [1,4,7])
