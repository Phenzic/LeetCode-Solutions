class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack=[0]

        while stack:
            room = stack.pop()
            visited.add(room)
            for keys in rooms[room]:
                if keys not in visited:
                    stack.append(keys)
        return len(visited) == len(rooms)    