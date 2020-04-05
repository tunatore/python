class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        room_to_visit = []
        room_to_visit.append(0)
        keys = []
        for room in room_to_visit:
            for i in range(0, len(rooms[room])):
                key = rooms[room][i]
                if key not in keys:
                    keys.append(key)
                    if key not in room_to_visit:
                        room_to_visit.append(key)

        return len(rooms) == len(room_to_visit)


s = Solution()
print(s.canVisitAllRooms([[1], [2], [3], []]))
print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
