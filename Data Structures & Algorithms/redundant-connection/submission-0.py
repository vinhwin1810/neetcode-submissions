class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(1, len(edges)+ 1)}
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in graph[node]:
                if nei != prev and not dfs(nei, node):
                    return False
            return True
        # create edges. if that edge create a cycle => return
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            visit = set()
            if not dfs(u, -1):
                return [u, v]

        return []
        
            
