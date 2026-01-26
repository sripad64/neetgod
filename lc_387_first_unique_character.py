"""
LeetCode 387 — First Unique Character in a String
Difficulty: Easy
Category: Hash Map / Counting

Problem:
Given a string s, find the first non-repeating character and return its index.
If it does not exist, return -1.

Example:
Input:  "leetcode"
Output: 0

Input:  "loveleetcode"
Output: 2

Key Idea:
- Count frequency of each character
- Iterate again from left to right
- First character with count == 1 is the answer

Why two passes?
- First pass builds frequency map
- Second pass preserves original order

Patterns:
- Hash Map
- Two Pass
- Frequency Count

Recognition:
- "first" → order matters
- "unique / non-repeating" → counting

Common Mistakes:
- Trying to solve in one pass
- Returning character instead of index

Time Complexity: O(n)
Space Complexity: O(1)  (since alphabet is fixed)
"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        # First pass: count characters
        for c in s:
            count[c] += 1

        # Second pass: find first unique character
        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
