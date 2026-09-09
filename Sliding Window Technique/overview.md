# Sliding Window Technique

The **Sliding Window Technique** is used to efficiently solve problems involving a **contiguous subarray or substring**.

Instead of recalculating everything for every possible range, we maintain a **window** and move it through the array or string.

---

## 1. Basic Idea

Suppose:

```text
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

We want the maximum sum of any subarray of size `3`.

Possible windows:

```text
[2, 1, 5] → sum = 8
   [1, 5, 1] → sum = 7
      [5, 1, 3] → sum = 9
         [1, 3, 2] → sum = 6
```

Answer:

```text
9
```

The best window is:

```text
[5, 1, 3]
```

---

## 2. Brute Force Approach

A brute force solution calculates the sum of every window separately.

```python
def max_sum(nums, k):
    maximum = float("-inf")

    for i in range(len(nums) - k + 1):
        current_sum = 0

        for j in range(i, i + k):
            current_sum += nums[j]

        maximum = max(maximum, current_sum)

    return maximum
```

For each starting position, we calculate `k` elements again.

Time complexity:

```text
O(n × k)
```

---

## 3. Sliding Window Optimization

Instead of calculating every window again:

```text
[2, 1, 5]
```

when we move right:

```text
   [1, 5, 1]
```

we can:

```text
Remove 2
Add 1
```

So:

```text
new sum
=
old sum
- outgoing element
+ incoming element
```

This avoids repeated work.

---

## 4. Python Implementation

```python
def max_sum(nums, k):
    window_sum = sum(nums[:k])
    maximum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]

        maximum = max(maximum, window_sum)

    return maximum
```

---

## 5. Step-by-Step Example

```text
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

First window:

```text
[2, 1, 5]

sum = 8
```

So:

```text
window_sum = 8
maximum = 8
```

### Move Window Right

Old:

```text
[2, 1, 5]
```

New:

```text
   [1, 5, 1]
```

Remove:

```text
2
```

Add:

```text
1
```

Calculation:

```text
8 - 2 + 1 = 7
```

So:

```text
window_sum = 7
maximum = 8
```

### Move Again

Old:

```text
[1, 5, 1]
```

New:

```text
   [5, 1, 3]
```

Remove:

```text
1
```

Add:

```text
3
```

Calculation:

```text
7 - 1 + 3 = 9
```

Now:

```text
window_sum = 9
maximum = 9
```

### Move Again

Old:

```text
[5, 1, 3]
```

New:

```text
   [1, 3, 2]
```

Calculation:

```text
9 - 5 + 2 = 6
```

Final answer:

```text
9
```

---

## 6. Visual Idea

Think of the window as a box moving through the array.

```text
[2, 1, 5, 1, 3, 2]
 └─────┘

   ↓ move

[2, 1, 5, 1, 3, 2]
    └─────┘

   ↓ move

[2, 1, 5, 1, 3, 2]
       └─────┘
```

Instead of rebuilding the box every time, we only update what enters and leaves.

---

## 7. Two Types of Sliding Window

There are mainly two types:

```text
Sliding Window
     │
     ├── Fixed Size Window
     │
     └── Variable Size Window
```

---

## 8. Fixed Size Sliding Window

The window size remains constant.

Example:

```text
Find maximum sum of every subarray of size k
```

If:

```text
k = 3
```

then every window always contains exactly three elements.

```text
[1, 2, 3]
   [2, 3, 4]
      [3, 4, 5]
```

Typical structure:

```python
window_sum = sum(nums[:k])

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right - k]
```

---

## 9. Variable Size Sliding Window

The window size can grow or shrink.

Usually we use:

```text
left
right
```

Example:

> Find the longest substring without repeating characters.

The window might look like:

```text
abc
```

Then expand:

```text
abcd
```

If a duplicate appears:

```text
abcda
```

we shrink the left side until the window becomes valid again.

---

## 10. Variable Window Mental Model

```text
Expand right
     ↓
Is window valid?
     │
 ┌───┴───┐
 │       │
Yes      No
 │       │
Keep     Shrink left
going       ↓
         valid again
```

---

## 11. Example: Minimum Size Subarray Sum

Suppose:

```text
nums = [2, 3, 1, 2, 4, 3]
target = 7
```

We want the smallest contiguous subarray whose sum is at least `7`.

Start:

```text
[2]
```

Expand:

```text
[2, 3]
```

Sum:

```text
5
```

Expand:

```text
[2, 3, 1]
```

Sum:

```text
6
```

Expand:

```text
[2, 3, 1, 2]
```

Sum:

```text
8
```

Now the window satisfies:

```text
sum >= 7
```

So shrink from the left.

Remove `2`:

```text
[3, 1, 2]
```

Sum:

```text
6
```

No longer valid.

Continue expanding later.

Eventually:

```text
[4, 3]
```

has:

```text
sum = 7
length = 2
```

Answer:

```text
2
```

---

## 12. Python Example: Variable Window

```python
def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    minimum = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            minimum = min(minimum, right - left + 1)

            current_sum -= nums[left]
            left += 1

    return 0 if minimum == float("inf") else minimum
```

---

## 13. Why Sliding Window Is Useful

Without Sliding Window, we may repeatedly process the same elements.

For example:

```text
Window 1:
[1, 2, 3]

Window 2:
   [2, 3, 4]
```

The values:

```text
2, 3
```

appear in both windows.

Brute Force may calculate them again.

Sliding Window reuses the previous result.

---

## 14. Time Complexity

For many Sliding Window problems:

```text
Time Complexity = O(n)
```

Why?

Because each element is usually:

```text
added once
removed once
```

Even with a nested `while` loop in variable Sliding Window, the overall complexity can still be:

```text
O(n)
```

because the `left` pointer only moves forward.

---

## 15. Space Complexity

This depends on the problem.

For a simple sum window:

```text
O(1)
```

For string problems using a set or dictionary:

```text
O(k)
```

where `k` is the number of elements or characters stored.

---

## 16. Sliding Window vs Two Pointers

They are closely related.

### Two Pointers

Usually:

```text
left
right
```

move based on some comparison or condition.

Example:

```text
Two Sum in sorted array
```

### Sliding Window

Also often uses:

```text
left
right
```

but they represent a **contiguous range**.

```text
[left ... right]
```

So Sliding Window can be thought of as a special Two Pointer pattern.

---

## 17. How to Recognize Sliding Window Problems

Look for phrases like:

```text
subarray
substring
contiguous
longest
shortest
maximum
minimum
at most
at least
exactly k
```

Examples:

```text
Maximum sum subarray of size k

Longest substring without repeating characters

Minimum length subarray with sum >= target

Longest substring with at most k distinct characters
```

These are strong Sliding Window signals.

---

## 18. Common Fixed Window Template

```python
left = 0

for right in range(len(nums)):
    # add nums[right]

    if right - left + 1 == k:
        # calculate answer

        # remove nums[left]
        left += 1
```

---

## 19. Common Variable Window Template

```python
left = 0

for right in range(len(nums)):

    # include nums[right]

    while window_is_invalid:
        # remove nums[left]
        left += 1

    # update answer
```

The main pattern is:

```text
Expand → Check → Shrink → Update
```

---

## 20. Important LeetCode Problems

Good Sliding Window problems to practice:

| LeetCode | Problem | Type |
|---|---|---|
| **643** | Maximum Average Subarray I | Fixed Window |
| **209** | Minimum Size Subarray Sum | Variable Window |
| **3** | Longest Substring Without Repeating Characters | Variable Window |
| **567** | Permutation in String | Fixed Window |
| **438** | Find All Anagrams in a String | Fixed Window |
| **1004** | Max Consecutive Ones III | Variable Window |
| **424** | Longest Repeating Character Replacement | Variable Window |
| **904** | Fruit Into Baskets | Variable Window |

---

## 21. Recommended Learning Order

```text
643 Maximum Average Subarray I
        ↓
209 Minimum Size Subarray Sum
        ↓
3 Longest Substring Without Repeating Characters
        ↓
567 Permutation in String
        ↓
438 Find All Anagrams in a String
        ↓
1004 Max Consecutive Ones III
        ↓
424 Longest Repeating Character Replacement
```

---

## 22. Final Summary

Sliding Window means:

> **Maintain a contiguous range and update it efficiently instead of recalculating everything.**

Remember:

```text
Fixed Window
-------------
Window size stays constant

Remove left
Add right
```

and:

```text
Variable Window
---------------
Expand right

If condition fails:
    shrink left
```

Complexity is often:

```text
Time  : O(n)
Space : O(1) or O(k)
```

The easiest mental model is:

```text
          SLIDING WINDOW

Array
  ↓
Create Window
  ↓
Move Right
  ↓
Add New Element
  ↓
Remove / Shrink Left
  ↓
Update Answer
```
