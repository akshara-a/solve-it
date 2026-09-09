# Brute Force Algorithm

**Brute Force** is a simple problem-solving approach where we try **all possible options** until we find the correct answer.

It does not use any advanced optimization.

The idea is:

> **Try every possibility and keep the best or correct result.**

---

## 1. Simple Example

Suppose we want to find two numbers whose sum is equal to a target.

```text
nums = [2, 7, 11, 15]
target = 9
```

A brute force approach checks every possible pair.

```text
2 + 7  = 9  ✅
2 + 11 = 13
2 + 15 = 17
7 + 11 = 18
7 + 15 = 22
11 + 15 = 26
```

We found:

```text
2 + 7 = 9
```

So the answer is:

```text
indexes = [0, 1]
```

---

# 2. Python Example

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []
```

Example:

```python
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
```

Output:

```text
[0, 1]
```

---

# 3. How Brute Force Works

Brute Force usually follows this pattern:

```text
Generate possible choices
        ↓
Check each choice
        ↓
Is it valid?
   ├── Yes → Save / Return
   └── No  → Try next
```

---

# 4. Why Is It Called Brute Force?

It is called **Brute Force** because the algorithm does not try to be clever.

It simply tries every possible solution.

For example:

```text
Possible answers:

Option 1
Option 2
Option 3
Option 4
Option 5

Check all of them.
```

---

# 5. Example: Finding Maximum Sum of Two Elements

Suppose:

```text
nums = [3, 8, 2, 6]
```

We want the maximum sum of any two elements.

Brute Force:

```text
3 + 8 = 11
3 + 2 = 5
3 + 6 = 9
8 + 2 = 10
8 + 6 = 14
2 + 6 = 8
```

Maximum:

```text
14
```

Python:

```python
def max_pair_sum(nums):
    maximum = float("-inf")

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            maximum = max(maximum, nums[i] + nums[j])

    return maximum
```

---

# 6. Time Complexity

Brute Force often uses nested loops.

Example:

```python
for i in range(n):
    for j in range(n):
        ...
```

This gives:

```text
O(n²)
```

If we use three nested loops:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            ...
```

Then:

```text
O(n³)
```

So Brute Force can become slow for large inputs.

---

# 7. Brute Force with One Loop

Not every brute force solution needs nested loops.

Example: finding an element using Linear Search.

```python
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1
```

This checks elements one by one.

Time complexity:

```text
O(n)
```

This can also be considered a simple brute force approach.

---

# 8. Brute Force vs Optimized Solution

Consider the Two Sum problem.

## Brute Force

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

Time:

```text
O(n²)
```

---

## Optimized Using Hash Map

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i
```

Time:

```text
O(n)
```

So:

```text
Brute Force
O(n²)

Optimized
O(n)
```

---

# 9. When Should You Use Brute Force?

Brute Force is useful when:

- The input size is small.
- You want to understand the problem first.
- You want a simple working solution.
- You want to compare against an optimized solution.
- There are only a small number of possibilities.
- You are solving a problem for the first time.

---

# 10. Brute Force in DSA

When solving DSA problems, a good strategy is:

```text
Understand Problem
      ↓
Create Brute Force Solution
      ↓
Find Bottleneck
      ↓
Optimize
      ↓
Use Better Data Structure / Algorithm
```

For example:

```text
Two Sum

Brute Force
    ↓
Two nested loops
    ↓
O(n²)
    ↓
Can we avoid searching again?
    ↓
Use Hash Map
    ↓
O(n)
```

---

# 11. Common Brute Force Patterns

## Pattern 1: Check Every Element

```python
for i in range(len(nums)):
    ...
```

Usually:

```text
O(n)
```

---

## Pattern 2: Check Every Pair

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        ...
```

Usually:

```text
O(n²)
```

---

## Pattern 3: Check Every Triplet

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            ...
```

Usually:

```text
O(n³)
```

---

## Pattern 4: Check Every Subarray

For an array:

```text
[1, 2, 3]
```

Possible subarrays include:

```text
[1]
[2]
[3]

[1, 2]
[2, 3]

[1, 2, 3]
```

A brute force solution may generate and check every subarray.

---

# 12. Example: Maximum Subarray Brute Force

Suppose:

```text
nums = [-2, 1, -3, 4, -1, 2, 1]
```

We want the maximum sum subarray.

A brute force approach tries every starting point and every ending point.

```python
def max_subarray(nums):
    maximum = float("-inf")

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum += nums[j]
            maximum = max(maximum, current_sum)

    return maximum
```

Time complexity:

```text
O(n²)
```

But Kadane's Algorithm solves the same problem in:

```text
O(n)
```

So:

```text
Brute Force      → O(n²)

Kadane Algorithm → O(n)
```

---

# 13. Why Learn Brute Force?

Brute Force is important because it helps you understand:

- What the problem is asking.
- What all possible answers look like.
- Where the repeated work happens.
- How an optimized solution improves the brute force version.

In interviews, it is often useful to first explain the brute force solution and then improve it.

---

# 14. Brute Force Does Not Mean Wrong

A brute force solution can still be completely correct.

The main issue is usually:

```text
Efficiency
```

For small input sizes:

```text
Brute Force may be completely acceptable.
```

For large input sizes:

```text
Brute Force may cause:

Time Limit Exceeded
```

---

# 15. Brute Force vs Greedy vs Dynamic Programming

| Approach | Main Idea |
|---|---|
| Brute Force | Try all possibilities |
| Greedy | Choose the best option at each step |
| Dynamic Programming | Store and reuse previous results |
| Binary Search | Reduce the search space by half |
| Kadane | Track the best contiguous sum efficiently |

---

# 16. Example Comparison

Suppose we want to find:

```text
Maximum Subarray Sum
```

Brute Force:

```text
Try every subarray
```

Complexity:

```text
O(n²)
```

Kadane:

```text
Track the best subarray ending at each position
```

Complexity:

```text
O(n)
```

---

# 17. Mental Model

Think of Brute Force as:

```text
Problem
   ↓
List all possibilities
   ↓
Try possibility 1
   ↓
Try possibility 2
   ↓
Try possibility 3
   ↓
...
   ↓
Find answer
```

---

# 18. Complexity Examples

| Brute Force Operation | Typical Complexity |
|---|---:|
| Check every element | `O(n)` |
| Check every pair | `O(n²)` |
| Check every triplet | `O(n³)` |
| Generate all subsets | `O(2ⁿ)` |
| Generate all permutations | `O(n!)` |

---

# 19. Important Interview Approach

When solving a new problem:

```text
1. Understand the problem

2. Think of the simplest solution

3. Write the Brute Force approach

4. Calculate its complexity

5. Identify repeated work

6. Optimize the solution
```

Example:

```text
Two Sum

Brute Force:
Check every pair
O(n²)

Problem:
Repeatedly searching for complement

Optimization:
Hash Map

Final:
O(n)
```

---

# 20. Final Summary

Brute Force means:

> **Try all possible options until you find the answer.**

It is usually:

- Easy to understand.
- Easy to implement.
- Useful as a starting solution.
- Less efficient for large inputs.

The general pattern is:

```text
Try Everything
      ↓
Check Validity
      ↓
Keep / Return Answer
```

Always ask:

```text
Can I remove repeated work?

Can I use a Hash Map?

Can I sort the data?

Can I use Binary Search?

Can I use Dynamic Programming?

Can I use a better algorithm?
```

That is how we move from:

```text
Brute Force
```

to:

```text
Optimized Solution
```
