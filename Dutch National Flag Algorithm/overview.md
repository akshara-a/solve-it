# Dutch National Flag Algorithm

The **Dutch National Flag Algorithm** is used to sort an array containing **three distinct values** in a single pass.

A common example is:

```text
0, 1, 2
```

This is exactly the idea behind **LeetCode 75 — Sort Colors**.

---

## 1. Example

Suppose:

```text
nums = [2, 0, 2, 1, 1, 0]
```

We want:

```text
[0, 0, 1, 1, 2, 2]
```

Instead of using a normal sorting algorithm, we maintain three pointers:

```text
low
mid
high
```

---

## 2. What Do the Three Pointers Mean?

```text
0 ... low-1
    → all 0s

low ... mid-1
    → all 1s

mid ... high
    → unknown / not processed

high+1 ... end
    → all 2s
```

Visual:

```text
[ 0s ][ 1s ][ unknown ][ 2s ]
       ↑      ↑       ↑
      low    mid     high
```

---

## 3. Main Rules

We inspect:

```python
nums[mid]
```

There are only three possibilities.

### Case 1: `nums[mid] == 0`

`0` belongs on the left.

So:

```python
nums[low], nums[mid] = nums[mid], nums[low]

low += 1
mid += 1
```

---

### Case 2: `nums[mid] == 1`

`1` already belongs in the middle.

So:

```python
mid += 1
```

No swap is needed.

---

### Case 3: `nums[mid] == 2`

`2` belongs on the right.

So:

```python
nums[mid], nums[high] = nums[high], nums[mid]

high -= 1
```

Notice:

```text
mid does NOT move
```

because the element swapped from `high` has not been checked yet.

---

## 4. Python Implementation

```python
class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## 5. Step-by-Step Example

Start with:

```text
nums = [2, 0, 2, 1, 1, 0]

low  = 0
mid  = 0
high = 5
```

So:

```text
[2, 0, 2, 1, 1, 0]
 ↑              ↑
low/mid        high
```

### Step 1

```text
nums[mid] = 2
```

A `2` belongs at the end.

Swap:

```text
nums[mid] ↔ nums[high]
```

Before:

```text
[2, 0, 2, 1, 1, 0]
```

After:

```text
[0, 0, 2, 1, 1, 2]
```

Update:

```text
high = 4
```

Do **not** increment `mid`.

Why?

Because the new element at `mid` is `0`, and we have not processed it yet.

---

### Step 2

Now:

```text
nums[mid] = 0
```

Swap `low` and `mid`.

They are currently the same index, so nothing visibly changes:

```text
[0, 0, 2, 1, 1, 2]
```

Update:

```text
low = 1
mid = 1
```

---

### Step 3

Now:

```text
nums[mid] = 0
```

Swap:

```text
nums[low] ↔ nums[mid]
```

Again they are the same position.

Update:

```text
low = 2
mid = 2
```

---

### Step 4

Now:

```text
nums[mid] = 2
```

Swap with `high`.

Before:

```text
[0, 0, 2, 1, 1, 2]
       ↑     ↑
      mid   high
```

After:

```text
[0, 0, 1, 1, 2, 2]
```

Update:

```text
high = 3
```

Again:

```text
mid stays 2
```

---

### Step 5

Now:

```text
nums[mid] = 1
```

`1` belongs in the middle.

So:

```text
mid += 1
```

Now:

```text
mid = 3
```

---

### Step 6

Again:

```text
nums[mid] = 1
```

So:

```text
mid += 1
```

Now:

```text
mid = 4
high = 3
```

Condition:

```text
mid <= high
```

is false.

Stop.

Final result:

```text
[0, 0, 1, 1, 2, 2]
```

---

## 6. Why Doesn't `mid` Increase When We Find `2`?

This is one of the most important parts.

Suppose:

```text
[1, 2, 0]
    ↑  ↑
   mid high
```

We swap `2` and `0`:

```text
[1, 0, 2]
    ↑
   mid
```

Now the new value at `mid` is:

```text
0
```

We have not processed that `0` yet.

If we incremented `mid`, we would skip it.

Therefore:

```python
high -= 1
```

but:

```python
# do not do mid += 1
```

---

## 7. Why Can We Increase `mid` After Swapping a `0`?

Suppose:

```text
[1, 0, ...]
 ↑  ↑
low mid
```

Everything before `mid` has already been processed.

When we swap:

```text
[0, 1, ...]
 ↑  ↑
low mid
```

the value moved into `mid` comes from the already-processed area.

Therefore it is safe to move:

```text
low += 1
mid += 1
```

---

## 8. Pointer Movement Summary

| Current Value | Action | `low` | `mid` | `high` |
|---|---|---:|---:|---:|
| `0` | Swap `low`, `mid` | +1 | +1 | Same |
| `1` | Do nothing | Same | +1 | Same |
| `2` | Swap `mid`, `high` | Same | Same | -1 |

This table is the easiest way to remember the algorithm.

---

## 9. Mental Model

Think:

```text
0 → LEFT
1 → MIDDLE
2 → RIGHT
```

So:

```text
nums[mid] == 0
      ↓
Send LEFT


nums[mid] == 1
      ↓
Leave it


nums[mid] == 2
      ↓
Send RIGHT
```

---

## 10. Why Is It Called the Dutch National Flag Algorithm?

The algorithm was proposed by **Edsger W. Dijkstra**.

The Dutch flag has three colors:

```text
Red
White
Blue
```

The original problem was about arranging three types of elements into three groups.

In programming problems, we commonly represent those three groups as:

```text
0
1
2
```

---

## 11. Time Complexity

Every element is processed at most a small constant number of times.

Therefore:

```text
Time Complexity = O(n)
```

---

## 12. Space Complexity

Only three pointers are used:

```text
low
mid
high
```

So:

```text
Space Complexity = O(1)
```

The sorting is done **in place**.

---

## 13. Brute Force vs Sorting vs Dutch National Flag

| Approach | Time | Space | Notes |
|---|---:|---:|---|
| General sorting | `O(n log n)` | Depends | Works but unnecessary |
| Counting `0,1,2` | `O(n)` | `O(1)` | Often requires two passes |
| Dutch National Flag | `O(n)` | `O(1)` | One-pass solution |

---

## 14. LeetCode Problem

The main problem to practice is:

**LeetCode 75 — Sort Colors**

Example:

```text
Input:

[2, 0, 2, 1, 1, 0]

Output:

[0, 0, 1, 1, 2, 2]
```

---

## 15. Code Template to Remember

```python
low = 0
mid = 0
high = len(nums) - 1

while mid <= high:

    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1

    elif nums[mid] == 1:
        mid += 1

    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
```

The simplest memory trick is:

```text
0 → swap left  → low++, mid++

1 → move mid   → mid++

2 → swap right → high--
                  DO NOT move mid
```

---

## 16. Final Summary

```text
Algorithm:
Dutch National Flag

Purpose:
Partition three distinct values into three groups

Pointers:
low
mid
high

0:
Swap with low
low++, mid++

1:
mid++

2:
Swap with high
high--

Time:
O(n)

Space:
O(1)
```
