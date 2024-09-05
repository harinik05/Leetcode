from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        EMPTY = float('inf')
        GATE = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if not rooms:
            return
        
        m = len(rooms)
        n = len(rooms[0])
        queue = deque()

        # Add all gates to the queue
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    queue.append((row, col))
        
        # Perform BFS
        while queue:
            row, col = queue.popleft()
            current_distance = rooms[row][col]
            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and rooms[r][c] == 2147483647:
                    rooms[r][c] = current_distance + 1
                    queue.append((r, c))
