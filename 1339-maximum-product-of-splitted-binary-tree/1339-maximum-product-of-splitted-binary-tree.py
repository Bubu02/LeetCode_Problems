# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=right):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # Array to store the sum of every possible subtree
        subtree_sums = []
        
        # Helper function to calculate the sum of a tree/subtree
        def calculate_sums(node):
            if not node:
                return 0
            
            # Post-order traversal: sum of current subtree = left + right + current val
            left_sum = calculate_sums(node.left)
            right_sum = calculate_sums(node.right)
            current_sum = left_sum + right_sum + node.val
            
            # Record this subtree sum
            subtree_sums.append(current_sum)
            return current_sum
        
        # Pass 1: Calculate the total sum of the tree and store all subtree sums
        total_sum = calculate_sums(root)
        
        # Pass 2: Find the maximum product
        max_prod = 0
        for s_sum in subtree_sums:
            # Calculate the product if we cut the edge above this subtree
            current_prod = s_sum * (total_sum - s_sum)
            if current_prod > max_prod:
                max_prod = current_prod
                
        # Return the maximum product modulo 10^9 + 7
        return max_prod % (10**9 + 7)