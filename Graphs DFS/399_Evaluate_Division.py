from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        answer = []

        for start, end in queries:
            answer.append(dfs(start, end, set()))

        return answer