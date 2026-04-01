class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def evaluate(x, y, visit):
            if not (x in adj and y in adj):
                return -1
            if x == y:
                return 1
            visit.add(x)
            for nei, val in adj[x]:
                if nei not in visit:
                    weight = evaluate(nei, y, visit)
                    if weight != -1:
                        res = val * weight
                        return res
            return -1
        ans = []
        for q in queries:
            ans.append(evaluate(q[0], q[1], set()))
        return ans