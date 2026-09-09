# Linear Search

**Linear Search** is the simplest searching algorithm.

It checks each element **one by one from the beginning** until the target is found.

Unlike Binary Search, the array **does not need to be sorted**.

---

## 1. Example

Suppose:

```text
nums = [7, 2, 9, 4, 6]
target = 4
```

Linear Search works like this:

```text
[7, 2, 9, 4, 6]
 ↑
7 == 4 ? ❌

[7, 2, 9, 4, 6]
    ↑
2 == 4 ? ❌

[7, 2, 9, 4, 6]
       ↑
9 == 4 ? ❌

[7, 2, 9, 4, 6]
          ↑
4 == 4 ? ✅
```

So the target is found at:

```text
index = 3
```

---

## 2. Python Implementation

```python
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1
```

Example:

```python
nums = [7, 2, 9, 4, 6]

print(linear_search(nums, 4))
```

Output:

```text
3
```

---

## 3. Understanding the Code

The loop:

```python
for i in range(len(nums)):
```

goes through every index.

For:

```text
nums = [7, 2, 9, 4, 6]
```

the indexes are:

```text
Index:  0  1  2  3  4
Value: [7, 2, 9, 4, 6]
```

Then:

```python
if nums[i] == target:
```

checks whether the current element is the target.

If it is:

```python
return i
```

returns its index.

If we finish the entire loop without finding the target:

```python
return -1
```

means:

```text
Target not found
```

---

## 4. Another Simple Version

You can also directly iterate through the values:

```python
def linear_search(nums, target):
    for num in nums:
        if num == target:
            return True

    return False
```

This returns:

```text
True  → target exists
False → target does not exist
```

If you need the **index**, use:

```python
for i in range(len(nums)):
```

---

## 5. Time Complexity

Suppose there are `n` elements.

### Best Case

The target is the first element.

```text
target = 4

[4, 7, 9, 2]
 ↑
```

Only one comparison is required.

```text
O(1)
```

### Worst Case

The target is the last element or is not present.

```text
target = 4

[7, 9, 2, 6, 4]
             ↑
```

We may have to check every element.

```text
O(n)
```

### Average Case

```text
O(n)
```

---

## 6. Space Complexity

Linear Search does not create another array or large data structure.

```text
Space Complexity = O(1)
```

---

## 7. Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|---|---|---|
| Array must be sorted | No | Yes |
| Searching method | One by one | Divide in half |
| Worst-case time | `O(n)` | `O(log n)` |
| Space | `O(1)` | `O(1)` |
| Implementation | Very simple | Slightly more complex |
| Works on unsorted array | Yes | Not directly |

Example:

```text
Linear Search

[2, 8, 1, 9, 4, 7]
 ↑
 ↓
Check every element
```

Binary Search:

```text
[1, 2, 4, 7, 8, 9]
       ↑
      mid

Discard half
```

---

## 8. When Should You Use Linear Search?

Use Linear Search when:

- The data is **unsorted**.
- The array is small.
- You only need to search occasionally.
- Sorting the array first would be unnecessary.

---

## 9. Core Idea

The main idea is:

> **Linear Search checks elements one by one until it finds the target.**

```text
Start
  ↓
Check element
  ↓
Target?
 ├── Yes → Return
 │
 └── No
      ↓
   Next element
      ↓
   Repeat
```

---

## 10. Complexity Summary

```text
Best Case Time   : O(1)
Average Time     : O(n)
Worst Case Time  : O(n)
Space Complexity : O(1)
```
