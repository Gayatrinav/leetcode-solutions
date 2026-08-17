from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))

        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, steps = queue.popleft()

            # Check all 4 directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries and open cell
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':

                    # Check if this is an exit
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1

                    # Mark visited
                    maze[nr][nc] = '+'

                    queue.append((nr, nc, steps + 1))

        return -1