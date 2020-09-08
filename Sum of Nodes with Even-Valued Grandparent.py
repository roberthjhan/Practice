"""
This is so ugly, dear lord, but I'm happy my brute-force attempt succeeded on my first
submission (millionth try at testcase). Results weren't too bad either, I beat almost
50% of submissions in runtime and almost 90% of submissions in memory. I think I
have an idea of how to optimize this but that will have to wait, I'm beat. We'll
see if I remember to come back to this.
"""

class Solution:
    def sumEvenGrandparent(self, root) -> int:
        if not root:
            return 0
        # Root is even
        if root.val % 2 == 0:
            # try to return sum of grandchild nodes + call function on children nodes
            try:  # root.right and root.left exist
                return self.sumRoots(root.left) + self.sumRoots(root.right) + self.sumEvenGrandparent(
                    root.left) + self.sumEvenGrandparent(root.right)
            except: # At least one child node is missing proceed with existing child if any
                if root.left:
                    return self.sumRoots(root.left) + self.sumEvenGrandparent(root.left)
                elif root.right:
                    return self.sumRoots(root.right) + self.sumEvenGrandparent(root.right)
                else:
                    return 0
        # Root is odd
        return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)

    def sumRoots(self, root):
        """Helper function gets sum of grandchild nodes"""
        ret = 0
        if root.right:
            ret += root.right.val
        if root.left:
            ret += root.left.val
        return ret