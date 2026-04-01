class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        visit = set()
        order = []
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                if crs not in order:
                    order.append(crs)
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order