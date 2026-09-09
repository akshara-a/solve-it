# Binary Search

Binary Search is an efficient searching algorithm used to find an element in a **sorted array**.

---

## 1. Basic Idea

Suppose we have:

```text
nums = [1, 3, 5, 7, 9, 11, 13]
target = 9
```

Instead of checking every element one by one, Binary Search checks the **middle element**.

```text
[1, 3, 5, 7, 9, 11, 13]
          ↑
        middle
```

The middle element is:

```text
7
```

Since:

```text
9 > 7
```

we know the target cannot be on the left side.

So we discard:

```text
[1, 3, 5, 7]
```

and continue searching in:

```text
[9, 11, 13]
```

---

# 2. Core Rule

At every step:

```text
nums[mid] == target
        ↓
      FOUND
```

If:

```text
nums[mid] < target
```

search the **right half**.

```text
        mid
         ↓
[1, 3, 5, 7, 9, 11]
            └───────→ Search here
```

If:

```text
nums[mid] > target
```

search the **left half**.

```text
←────────┐
[1, 3, 5, 7, 9, 11]
            ↑
           mid
```

---

# 3. Python Implementation

```python
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
```

---

# 4. Understanding the Variables

We maintain three important variables:

```python
left
right
mid
```

### `left`

Index where the current search range starts.

```python
left = 0
```

---

### `right`

Index where the current search range ends.

```python
right = len(nums) - 1
```

For:

```text
nums = [1, 3, 5, 7, 9]
```

the indexes are:

```text
Index:  0  1  2  3  4
Value: [1, 3, 5, 7, 9]
```

Therefore:

```text
left = 0
right = 4
```

---

### `mid`

The middle index.

```python
mid = (left + right) // 2
```

Example:

```text
left = 0
right = 4
```

Then:

```text
mid = (0 + 4) // 2

mid = 2
```

So:

```text
nums[2] = 5
```

---

# 5. Step-by-Step Example

Consider:

```text
nums = [1, 3, 5, 7, 9]
target = 9
```

Indexes:

```text
Index:  0  1  2  3  4
Value: [1, 3, 5, 7, 9]
```

Initially:

```text
left = 0
right = 4
```

---

## Iteration 1

Calculate:

```text
mid = (0 + 4) // 2

mid = 2
```

So:

```text
nums[mid] = nums[2]

nums[2] = 5
```

Compare:

```text
5 < 9
```

Therefore, the target must be on the right side.

Update:

```python
left = mid + 1
```

So:

```text
left = 3
right = 4
```

---

## Iteration 2

Now the search area is:

```text
Index:           3  4
Value:           7  9
                 ↑  ↑
               left right
```

Calculate:

```text
mid = (3 + 4) // 2

mid = 3
```

So:

```text
nums[3] = 7
```

Compare:

```text
7 < 9
```

Move right again:

```python
left = mid + 1
```

Now:

```text
left = 4
right = 4
```

---

## Iteration 3

Calculate:

```text
mid = (4 + 4) // 2

mid = 4
```

Now:

```text
nums[4] = 9
```

Compare:

```text
9 == 9
```

Target found.

Return:

```text
4
```

---

# 6. Why Do We Use `left <= right`?

The loop condition is:

```python
while left <= right:
```

because even when:

```text
left == right
```

there is still **one element remaining to check**.

Example:

```text
left = 4
right = 4
```

There is still:

```text
nums[4]
```

to check.

---

# 7. Why `mid + 1`?

Suppose:

```text
nums[mid] < target
```

We already checked `mid`.

Therefore, we do not need to check it again.

Instead of:

```python
left = mid
```

we use:

```python
left = mid + 1
```

---

# 8. Why `mid - 1`?

Similarly, if:

```text
nums[mid] > target
```

we already know that `mid` is not the answer.

Therefore:

```python
right = mid - 1
```

---

# 9. When Target Is Not Present

Example:

```text
nums = [1, 3, 5, 7, 9]
target = 6
```

Eventually:

```text
left > right
```

This means there are no elements remaining to search.

So we return:

```python
return -1
```

---

# 10. Time Complexity

Binary Search removes approximately half of the remaining elements after every comparison.

Suppose we have:

```text
16 elements
```

The search space becomes:

```text
16
↓
8
↓
4
↓
2
↓
1
```

Therefore:

```text
Time Complexity = O(log n)
```

---

# 11. Space Complexity

The iterative Binary Search only uses:

```text
left
right
mid
```

Therefore:

```text
Space Complexity = O(1)
```

---

# 12. Binary Search vs Linear Search

| Feature                      | Linear Search  | Binary Search       |
| ---------------------------- | -------------- | ------------------- |
| Requires sorted array        | No             | Yes                 |
| Checks elements              | One by one     | Divides search area |
| Time Complexity              | O(n)           | O(log n)            |
| Space Complexity             | O(1)           | O(1)                |
| Good for large sorted arrays | Less efficient | Very efficient      |

---

# 13. Important Requirement

Basic Binary Search requires the array to be:

```text
SORTED
```

Example:

```text
[1, 3, 5, 7, 9]
```

Binary Search works correctly.

But:

```text
[7, 1, 9, 3, 5]
```

Basic Binary Search cannot be directly applied.

---

# 14. Binary Search Template

A useful template to remember:

```python
left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

return -1
```

---

# 15. Mental Model

Think of Binary Search as repeatedly asking:

```text
Is the target in the:

LEFT HALF

or

RIGHT HALF?
```

Example:

```text
[1, 3, 5, 7, 9, 11, 13]
          ↑
        Check 7

Target = 11

11 > 7

Discard left half
                ↓
            [9, 11, 13]
```

Every step removes approximately half of the possibilities.

---

# 16. Common Mistakes

## Mistake 1: Using Binary Search on an Unsorted Array

Wrong:

```text
[5, 1, 8, 3, 9]
```

Binary Search expects sorted data.

---

## Mistake 2: Using `left < right`

For the standard template, use:

```python
while left <= right:
```

because when:

```text
left == right
```

there is still one element remaining.

---

## Mistake 3: Writing

```python
left = mid
```

This can cause an infinite loop.

Use:

```python
left = mid + 1
```

---

## Mistake 4: Writing

```python
right = mid
```

For this version of Binary Search, use:

```python
right = mid - 1
```

---

# 17. Example LeetCode Problem

A good first Binary Search problem is:

**LeetCode 704 — Binary Search**

Example:

```text
Input:

nums = [-1, 0, 3, 5, 9, 12]
target = 9

Output:

4
```

Because:

```text
nums[4] = 9
```

---

# 18. Final Summary

Binary Search works by repeatedly cutting the search space into half.

```text
Sorted Array
     ↓
Find Middle
     ↓
Compare with Target
     ↓
 ┌───────────────┐
 ↓               ↓
Smaller         Larger
 ↓               ↓
Search Left     Search Right
```

Remember:

```text
Target == nums[mid]
→ Found

Target > nums[mid]
→ Move left to mid + 1

Target < nums[mid]
→ Move right to mid - 1
```

Complexity:

```text
Time  : O(log n)
Space : O(1)
```

The key idea is:

> **Do not search every element. Eliminate half of the remaining search space after every comparison.**
