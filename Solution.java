import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
	static int count = 0;
	static int[] tree = null;

	public static int[] solution(int h, int[] input) {
		count = 1;
		tree = new int[(int)Math.pow(2, h)-1];
		buildTree(0);

		List<Integer> list = Arrays.stream(tree).boxed().collect(Collectors.toList());
		int[] ans = new int[input.length];
		int c = 0;

		for (int x: input) {
			int p = list.indexOf(x);
			if (p<=0) {
				ans[c++]=-1;
			}
			else {
				ans[c++]=tree[(p-1)/2];
			}
		}

		return ans;
	}

	public static void buildTree(int p) {
		if (p >= tree.length) {
			return;
		}
		else {
			buildTree( (p+1)*2-1 );
			buildTree( (p+1)*2 );
			tree[p]=count++;
		}
	}

	public static void main(String args[]) {
		System.out.println(Arrays.toString(solution(5, new int[] {19,14,28}))); // 21, 15, 29
		System.out.println(Arrays.toString(solution(3, new int[] {7,3,5,1}))); // -1, 7, 6, 3
		System.out.println(Arrays.toString(solution(3, new int[] {1,4,7}))); // 3, 6, -1
	}
}
