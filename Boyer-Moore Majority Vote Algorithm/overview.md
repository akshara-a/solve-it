# Boyer–Moore Majority Vote Algorithm

The **Boyer–Moore Majority Vote Algorithm** is used to find the **majority element** in an array.

A majority element is an element that appears **more than `n / 2` times**.

---

## 1. Example

```text
nums = [2, 2, 1, 1, 1, 2, 2]
```

Array length:

```text
n = 7
```

A majority element must appear more than:

```text
7 / 2 = 3.5
```

So it must appear at least:

```text
4 times
```

Here:

```text
2 appears 4 times
```

Therefore:

```text
Answer = 2
```

---

## 2. Main Idea

The algorithm maintains two variables:

```text
candidate
count
```

Think of the algorithm like a voting process.

- If the current number is the same as the candidate → increase the count.
- If the current number is different → decrease the count.
- If the count becomes `0` → choose a new candidate.

The key intuition is:

> The majority element appears so often that all other elements combined cannot completely cancel it out.

---

## 3. Python Implementation

```python
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```

---

## 4. Step-by-Step Example

Consider:

```text
nums = [2, 2, 1, 1, 1, 2, 2]
```

Initially:

```text
candidate = None
count = 0
```

### Step 1

Current number:

```text
2
```

Since `count == 0`, choose `2` as the candidate.

```text
candidate = 2
count = 1
```

### Step 2

Current number:

```text
2
```

Same as candidate:

```text
count = 2
```

### Step 3

Current number:

```text
1
```

Different from candidate:

```text
count = 1
```

### Step 4

Current number:

```text
1
```

Different again:

```text
count = 0
```

### Step 5

Current number:

```text
1
```

Since `count == 0`, choose a new candidate:

```text
candidate = 1
count = 1
```

### Step 6

Current number:

```text
2
```

Different:

```text
count = 0
```

### Step 7

Current number:

```text
2
```

Choose a new candidate:

```text
candidate = 2
count = 1
```

Final result:

```text
candidate = 2
```

So:

```text
Answer = 2
```

---

## 5. Visual Representation

```text
nums = [2, 2, 1, 1, 1, 2, 2]

Current     Candidate     Count

2              2           1
2              2           2
1              2           1
1              2           0
1              1           1
2              1           0
2              2           1

Final Candidate = 2
```

---

## 6. Why Does It Work?

Suppose the majority element is:

```text
M
```

Every occurrence of `M` contributes:

```text
+1
```

Every different element can cancel one occurrence:

```text
-1
```

Because the majority element occurs more than half the time:

```text
count(M) > count(all other elements combined)
```

it cannot be completely cancelled.

Therefore, after all cancellations, the majority element remains as the candidate.

---

## 7. Time Complexity

The array is traversed only once.

```text
Time Complexity = O(n)
```

---

## 8. Space Complexity

Only two variables are required:

```text
candidate
count
```

Therefore:

```text
Space Complexity = O(1)
```

---

## 9. Brute Force vs Hash Map vs Boyer–Moore

| Approach | Time Complexity | Space Complexity |
|---|---:|---:|
| Brute Force | `O(n²)` | `O(1)` |
| Hash Map | `O(n)` | `O(n)` |
| Boyer–Moore | `O(n)` | `O(1)` |

Boyer–Moore is especially useful because it achieves:

```text
O(n) time
O(1) space
```

---

## 10. Important Condition

The standard Boyer–Moore algorithm assumes that a majority element **is guaranteed to exist**.

For example:

```text
LeetCode 169 — Majority Element
```

guarantees that a majority element exists.

If a majority element is **not guaranteed**, verify the final candidate.

---

## 11. Version with Verification

```python
def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    if nums.count(candidate) > len(nums) // 2:
        return candidate

    return None
```

---

## 12. Mental Model

```text
count == 0
    ↓
Choose Candidate
    ↓
Compare Current Number
    ↓
Same as Candidate?
 ┌───────────────┐
 ↓               ↓
Yes              No
 ↓               ↓
+1               -1
```

Or more simply:

```text
Same      → Vote for candidate
Different → Cancel one vote
Zero      → Pick a new candidate
```

---

## 13. Key Idea

> **Different elements cancel each other, while the true majority survives the cancellation.**

---

## 14. LeetCode Practice

```text
LeetCode 169 — Majority Element
```

This is the standard problem for learning the Boyer–Moore Majority Vote Algorithm.

---

## 15. Final Summary

```text
Algorithm:
Boyer–Moore Majority Vote

Purpose:
Find an element appearing more than n / 2 times

Variables:
candidate
count

Same candidate:
count += 1

Different value:
count -= 1

count == 0:
Choose a new candidate

Time:
O(n)

Space:
O(1)
```
