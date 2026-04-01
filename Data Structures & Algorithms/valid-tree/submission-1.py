class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        treeMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            treeMap[n1].append(n2)
            treeMap[n2].append(n1)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for n in treeMap[node]:
                if n != prev and not dfs(n, node):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)