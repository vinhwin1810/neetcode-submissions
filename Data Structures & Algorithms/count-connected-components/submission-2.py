class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        treeMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            treeMap[n1].append(n2)
            treeMap[n2].append(n1)
        visited, count = set(), 0

        def connected(node):
            if node in visited:
                return
            visited.add(node)
            for n in treeMap[node]:
                connected(n)

        for node in range(n):
            if node not in visited:
                connected(node)
                count += 1
        return count