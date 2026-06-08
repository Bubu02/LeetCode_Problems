from collections import defaultdict

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build an adjacency list where we track the neighbor and 
        # whether the original edge matches the traversal direction.
        # 1 means original direction (u -> v), 0 means reversed direction (v -> u)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
            
        ans = [0] * n
        
        # Step 1: Calculate the cost for root node 0 using a bottom-up DFS
        def dfs1(node, parent):
            total_reversals = 0
            for neighbor, is_original in graph[node]:
                if neighbor != parent:
                    # If the edge is reversed (0), we need 1 reversal to go node -> neighbor
                    cost = 0 if is_original == 1 else 1
                    total_reversals += cost + dfs1(neighbor, node)
            return total_reversals

        ans[0] = dfs1(0, -1)
        
        # Step 2: Reroot the tree top-down to compute answers for all other nodes
        def dfs2(node, parent):
            for neighbor, is_original in graph[node]:
                if neighbor != parent:
                    if is_original == 1:
                        # Edge is node -> neighbor. If 'neighbor' becomes the root,
                        # it needs to reverse this edge to point back to 'node'. (+1 reversal)
                        ans[neighbor] = ans[node] + 1
                    else:
                        # Edge is neighbor -> node. If 'neighbor' becomes the root,
                        # it already points toward 'node'. (-1 reversal)
                        ans[neighbor] = ans[node] - 1
                        
                    dfs2(neighbor, node)
                    
        dfs2(0, -1)
        return ans