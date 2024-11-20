class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index,path):
            if sum(path) == target:
                result.append(path[:])

            if sum(path)>target or index>len(candidates):
                return

            for i in range(index,len(candidates)):
                path.append(candidates[i])
                dfs(i,path)
                path.pop()

        dfs(0,[])
        return result
