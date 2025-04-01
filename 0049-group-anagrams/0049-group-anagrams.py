class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Solution 1 
                # Time complexity o(m.nlogn)
                # m: number of elements in the array, n: avg length of each string in the array, nlogn: time taken to sort the string 
        # result=defaultdict(list)
        # for s in strs:
        #     sortedS=''.join(sorted(s))
        #     result[sortedS].append(s)
        # return list(result.values())

        # Solution 2
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # as strs[i] consists of lowercase English letters.
            for c in s:
                count[ord(c) - ord('a')] +=1
            result[tuple(count)].append(s)
        return list(result.values())