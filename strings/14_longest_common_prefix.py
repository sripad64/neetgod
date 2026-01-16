Perfect choice of problem to **lock this template in**.
Below is a **GitHub-ready solution file**, exactly in the structure you want, optimized for **future interview recall**.

You can copy-paste this directly.

---

# LeetCode 14 — Longest Common Prefix

## 1) Comments (High-Level, Interview Friendly)

* Goal: Find the **longest prefix shared by all strings**
* Strategy: Start with the **first string as the candidate prefix**, shrink it until all words match
* Key invariant: `prefix` is **always valid for all strings processed so far**
* Time Complexity: **O(n × m)** where

  * `n` = number of strings
  * `m` = length of the shortest string
* Space Complexity: **O(1)** (ignoring input)

---

## 2) Basic Idea (Plain English)

Start by assuming the **entire first string** is the common prefix.
Then, compare it with each subsequent word.
If a word doesn’t start with the current prefix, **shorten the prefix** until it does.
If the prefix ever becomes empty, no common prefix exists.

This works because **the common prefix cannot be longer than the shortest mismatch found**.

---

## 3) 🚨 Dead-Giveaway Pattern Trigger (Train Your Brain)

**The SECOND you see:**

* “Longest common prefix”
* “Common starting characters”
* “All strings must share something from the beginning”

👉 **Think immediately:**

> “Shrink a candidate prefix until everyone agrees”

This is a **prefix-validation problem**, not sorting, not hashing, not DP.

---

## 4) Mental Model / Framework

### Think in terms of **prefix survival**

* Start with a **maximum possible prefix**
* Each string acts like a **filter**
* Characters get **eliminated from the right**
* The prefix only ever **shrinks**, never grows

### Questions to ask yourself:

* What is the **maximum possible prefix**? → first string
* When does it fail? → when a word doesn’t start with it
* How do I fix failure? → remove last character

---

## 5) Pseudocode / Algorithm

```
if input list is empty:
    return empty string

set prefix = first string

for each word after the first:
    while word does not start with prefix:
        remove last character from prefix
        if prefix becomes empty:
            return empty string

return prefix
```

---

## 6) Actual Code (Python)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
```

---

## 🧠 Interview Recall Shortcut (One-Line Memory Hook)

> **“Take the first string → keep chopping until everyone agrees.”**

If you want, next we can:

* Add a **1-line brute force alternative** (vertical scanning)
* Compare this with **sorting-based solutions**
* Build a **pattern index entry** for this problem

Drop the next LeetCode when ready.
