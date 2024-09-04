from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        frequencies = Counter(word)
        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
        
        total_pushes = 0
        block_count = 1

        for i in range(len(sorted_frequencies)):
            if i % 8 == 0 and i != 0:
                block_count += 1
            letter, freq = sorted_frequencies[i]
            total_pushes += freq * block_count

        return total_pushes

sol=Solution()
# print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))
print(sol.minimumPushes("xyzxyzxyzxyz")) 