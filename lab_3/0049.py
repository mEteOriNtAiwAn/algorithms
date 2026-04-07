class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict_results = defaultdict(list)
        for string in strs:
            grid = [0 for i in range(97, 123)]
            for char in string:
                grid[ord(char)-97] += 1
            
            dict_results[tuple(grid)].append(string)

        return list(dict_results.values())