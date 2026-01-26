"""
LeetCode 49 — Group Anagrams
Difficulty: Medium
Category: Hash Map / String

Problem:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example:
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Key Idea:
- Anagrams have identical character frequencies
- Represent each string by its character count
- Use this count as a hash key to group strings

Why not sorting?
- Sorting each string costs O(n log n)
- Character counting gives linear time

Approach:
- Use a hashmap:
    key   → character frequency pattern
    value → list of strings with that pattern
- Convert frequency list to tuple so it can be used as a key

Patterns:
- Hash Map
- Frequency Count
- Grouping
- Fixed-size array (26 letters)

Recognition:
- "anagram" → same character counts
- "group" → hashmap buckets
- lowercase letters → fixed 26-size array

Common Mistakes:
- Using list as dictionary key (not hashable)
- Forgetting to convert count array to tuple
- Sorting when not required
- Returning dictionary instead of values

Time Complexity:
O(m * n)
where m = number of strings, n = average string length

Space Complexity:
O(m * n)
(for storing grouped strings)
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())
    
    