class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        sorted_people = sorted(people, reverse=True)
        first_index = 0
        last_index = len(people) - 1
        min_number_of_boats = 0
        while first_index <= last_index:
            if sorted_people[first_index] + sorted_people[last_index] <= limit:
                first_index += 1
                last_index -= 1
            elif sorted_people[first_index] + sorted_people[last_index] > limit:
                first_index += 1
            min_number_of_boats += 1
        return min_number_of_boats


s = Solution()
print(s.numRescueBoats([3, 1, 2], 3))
print(s.numRescueBoats([3, 2, 2, 1], 3))
print(s.numRescueBoats([3, 5, 3, 4], 5))