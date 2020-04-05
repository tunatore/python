class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S is None:
            return None

        partition_label_list = []
        last_index_locations = [-1] * 26

        for index in range(0, len(S)):
            last_index_locations[ord(S[index]) - ord('a')] = index

        i = 0
        while i < len(S):
            end_index = last_index_locations[ord(S[i]) - ord('a')]
            j = i
            while j < end_index:
                end_index = max(last_index_locations[ord(S[j]) - ord('a')], end_index)
                j += 1

            partition_label_list.append(end_index + 1 - i)
            i = j + 1

        return partition_label_list


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))