# https://leetcode.com/problems/all-paths-from-source-to-target/description/


def allPathsSourceTarget(self, graph):
        # find all paths from 0 to n-1 using BFS
        # Traverse the path and append it to ans array when last node is visited

        n = len(graph)
        ans = []
        queue = [[0]]
        
        while queue:
            current_path = queue.pop(0)
            u = current_path[-1]
            if u == n-1:
                ans.append(current_path)
            else:
                for v in graph[u]:
                    queue.append(current_path + [v])

        return ans
