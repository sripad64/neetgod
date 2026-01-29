"""
LeetCode 217 — Contains Duplicate
Difficulty: Easy
Category: Hash Set

Problem:
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element is distinct.

Example:
Input:  [1,2,3,1]
Output: True

Input:  [1,2,3,4]
Output: False

Key Idea:
- Use a hash set to track seen numbers
- If a number is already in the set, it is a duplicate

Why this works:
- Sets provide O(1) average lookup
- The first repeated element can be detected immediately

Patterns:
- Hash Set
- Duplicate Detection
- Early Exit

Recognition:
- "contains duplicate"
- "appears at least twice"
- "distinct elements"

Common Mistakes:
- Using nested loops (O(n²))
- Sorting unnecessarily
- Forgetting early return optimization

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
