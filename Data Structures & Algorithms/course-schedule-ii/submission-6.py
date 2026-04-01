class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        visit, visit2 = set(), set()
        order = []
        def dfs(crs):
            if crs in visit:
                return False
            if crs in visit2:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            visit2.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order