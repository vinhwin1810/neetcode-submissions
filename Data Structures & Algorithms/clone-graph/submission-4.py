"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToCopy = {}
        if not node:
            return None

        def dfs(node):
            if not node:
                return
            if node not in nodeToCopy:
                new = Node(node.val)
                new.neighbors = []
                nodeToCopy[node] = new
                for nei in node.neighbors:
                    new_nei = dfs(nei)
                    if new_nei:
                        new.neighbors.append(new_nei)
                return new
            return nodeToCopy[node]
        return dfs(node)