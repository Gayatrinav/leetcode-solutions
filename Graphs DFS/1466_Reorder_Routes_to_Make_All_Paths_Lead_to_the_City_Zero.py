class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            # Original direction: a -> b
            graph[a].append((b, 1))

            # Reverse direction for traversal: b -> a
            graph[b].append((a, 0))

        def dfs(city, parent):
            changes = 0

            for neighbor, cost in graph[city]:
                if neighbor == parent:
                    continue

                changes += cost
                changes += dfs(neighbor, city)

            return changes

        return dfs(0, -1) 