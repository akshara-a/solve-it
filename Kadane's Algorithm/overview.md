# Kadane's Algorithm

Kadane’s Algorithm is used to find the **maximum sum of a contiguous subarray** in an array.

The important word is **contiguous**: the selected elements must be next to each other.

For example:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

One contiguous subarray is:

```text
[4, -1, 2, 1]
```

Its sum is:

```text
4 + (-1) + 2 + 1 = 6
```

So the maximum contiguous-subarray sum is:

```text
6
```

---

## 1. First Understand the Problem

Suppose you have:

```text
[2, -4, 3, 5, -1]
```

Possible contiguous subarrays include:

```text
[2]
[2, -4]
[2, -4, 3]
[-4]
[-4, 3]
[3]
[3, 5]
[3, 5, -1]
[5]
```

We want the subarray whose sum is the largest.

Here:

```text
[3, 5]
```

has:

```text
3 + 5 = 8
```

So the answer is:

```text
8
```

---

## 2. The Brute-Force Idea

A beginner might think:

```text
Start at every index.
Try every possible ending index.
Calculate each subarray sum.
Keep the maximum.
```

For example:

```text
[2, -4, 3, 5]
```

We could calculate:

```text
[2]             = 2
[2, -4]         = -2
[2, -4, 3]      = 1
[2, -4, 3, 5]   = 6

[-4]            = -4
[-4, 3]         = -1
[-4, 3, 5]      = 4

[3]             = 3
[3, 5]          = 8

[5]             = 5
```

Maximum:

```text
8
```

This works, but it does unnecessary work.

Kadane’s Algorithm finds the same answer in just **one pass**.

---

# 3. The Key Idea Behind Kadane's Algorithm

At every element, Kadane asks one simple question:

> Is it better to continue the previous subarray, or start a new subarray from the current element?

Suppose:

```text
currentSum = -3
```

and the next element is:

```text
5
```

We have two options.

Continue:

```text
-3 + 5 = 2
```

Start fresh:

```text
5
```

Clearly:

```text
5 > 2
```

So there is no benefit in carrying the negative sum forward.

We throw away the previous subarray and start from `5`.

That is the core idea.

---

# 4. The Two Important Variables

Kadane normally uses two variables:

```text
currentSum
maxSum
```

## `currentSum`

This means:

> What is the best possible subarray sum ending exactly at the current element?

## `maxSum`

This means:

> What is the largest subarray sum I have seen anywhere so far?

The main formula is:

```text
currentSum = max(
    currentElement,
    currentSum + currentElement
)
```

Then:

```text
maxSum = max(maxSum, currentSum)
```

---

# 5. Example

Consider:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Start with the first element:

```text
currentSum = -2
maxSum = -2
```

Now move through the array.

## Element = 1

Continue:

```text
-2 + 1 = -1
```

Start fresh:

```text
1
```

Choose:

```text
1
```

So:

```text
currentSum = 1
maxSum = 1
```

---

## Element = -3

Continue:

```text
1 + (-3) = -2
```

Start fresh:

```text
-3
```

Choose:

```text
-2
```

So:

```text
currentSum = -2
maxSum = 1
```

Notice that `currentSum` can become negative.

That is okay.

---

## Element = 4

Continue:

```text
-2 + 4 = 2
```

Start fresh:

```text
4
```

Starting fresh is better.

```text
currentSum = 4
maxSum = 4
```

The negative previous sum is abandoned.

---

## Element = -1

Continue:

```text
4 + (-1) = 3
```

Start fresh:

```text
-1
```

Continue.

```text
currentSum = 3
maxSum = 4
```

---

## Element = 2

Continue:

```text
3 + 2 = 5
```

Start fresh:

```text
2
```

Continue.

```text
currentSum = 5
maxSum = 5
```

---

## Element = 1

Continue:

```text
5 + 1 = 6
```

Start fresh:

```text
1
```

Continue.

```text
currentSum = 6
maxSum = 6
```

---

## Element = -5

Continue:

```text
6 - 5 = 1
```

Start fresh:

```text
-5
```

Continue.

```text
currentSum = 1
maxSum = 6
```

The sum decreased, but it is still useful for future elements.

---

## Element = 4

Continue:

```text
1 + 4 = 5
```

Start fresh:

```text
4
```

Continue.

```text
currentSum = 5
maxSum = 6
```

Final answer:

```text
6
```

The subarray is:

```text
[4, -1, 2, 1]
```

---

# 6. Full Dry-Run Table

| Element | Previous `currentSum` | Continue | Start Fresh | New `currentSum` | `maxSum` |
|---:|---:|---:|---:|---:|---:|
| -2 | - | - | -2 | -2 | -2 |
| 1 | -2 | -1 | 1 | 1 | 1 |
| -3 | 1 | -2 | -3 | -2 | 1 |
| 4 | -2 | 2 | 4 | 4 | 4 |
| -1 | 4 | 3 | -1 | 3 | 4 |
| 2 | 3 | 5 | 2 | 5 | 5 |
| 1 | 5 | 6 | 1 | 6 | **6** |
| -5 | 6 | 1 | -5 | 1 | 6 |
| 4 | 1 | 5 | 4 | 5 | 6 |

Answer:

```text
Maximum subarray sum = 6
```

---

# 7. C# Implementation

```csharp
public static int Kadane(int[] nums)
{
    int currentSum = nums[0];
    int maxSum = nums[0];

    for (int i = 1; i < nums.Length; i++)
    {
        currentSum = Math.Max(
            nums[i],
            currentSum + nums[i]
        );

        maxSum = Math.Max(
            maxSum,
            currentSum
        );
    }

    return maxSum;
}
```

Usage:

```csharp
int[] nums =
{
    -2, 1, -3, 4, -1, 2, 1, -5, 4
};

int result = Kadane(nums);

Console.WriteLine(result);
```

Output:

```text
6
```

---

# 8. Understanding the Most Important Line

The key line is:

```csharp
currentSum = Math.Max(nums[i], currentSum + nums[i]);
```

Suppose:

```text
currentSum = -4
nums[i] = 6
```

Start fresh:

```text
6
```

Continue:

```text
-4 + 6 = 2
```

We choose:

```text
6
```

So we start a new subarray.

Now suppose:

```text
currentSum = 5
nums[i] = 2
```

Start fresh:

```text
2
```

Continue:

```text
5 + 2 = 7
```

We choose:

```text
7
```

So we continue the existing subarray.

---

# 9. Another Way to Think About It

Imagine you are carrying a running score.

Suppose:

```text
Current score = 8
Next number = -3
```

You get:

```text
8 - 3 = 5
```

The result is still useful, so keep it.

But suppose:

```text
Current score = -8
Next number = 4
```

Continuing gives:

```text
-8 + 4 = -4
```

Starting fresh gives:

```text
4
```

The previous negative value only hurts you.

So throw it away and start from `4`.

Kadane's algorithm repeatedly makes this decision.

---

# 10. Why Don't We Restart Whenever We See a Negative Number?

This is an important beginner question.

Consider:

```text
[10, -2, 5]
```

When we encounter `-2`, we should **not** immediately restart.

Because:

```text
10 - 2 = 8
```

Then:

```text
8 + 5 = 13
```

The best subarray is:

```text
[10, -2, 5]
```

with:

```text
13
```

So negative elements are not automatically bad.

What matters is whether the **whole current running sum** is helping us.

---

# 11. What Happens With an All-Negative Array?

Consider:

```text
[-8, -3, -6, -2, -5]
```

The answer should be:

```text
-2
```

because:

```text
[-2]
```

is better than every other possible subarray.

This is why the safe implementation starts with:

```csharp
int currentSum = nums[0];
int maxSum = nums[0];
```

Do not blindly initialize:

```csharp
maxSum = 0;
```

because then an all-negative array would incorrectly return `0`.

---

# 12. Finding the Actual Subarray

Sometimes we don't just want the sum.

We also want the actual subarray.

For example:

```text
Maximum Sum = 6

Subarray = [4, -1, 2, 1]
```

We can track the start and end indices.

```csharp
public static void KadaneWithIndices(int[] nums)
{
    int currentSum = nums[0];
    int maxSum = nums[0];

    int currentStart = 0;

    int start = 0;
    int end = 0;

    for (int i = 1; i < nums.Length; i++)
    {
        if (nums[i] > currentSum + nums[i])
        {
            currentSum = nums[i];
            currentStart = i;
        }
        else
        {
            currentSum += nums[i];
        }

        if (currentSum > maxSum)
        {
            maxSum = currentSum;
            start = currentStart;
            end = i;
        }
    }

    Console.WriteLine($"Maximum Sum: {maxSum}");
    Console.WriteLine($"Start Index: {start}");
    Console.WriteLine($"End Index: {end}");
}
```

For:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

we get:

```text
Maximum Sum = 6

Start Index = 3
End Index = 6
```

which corresponds to:

```text
[4, -1, 2, 1]
```

---

# 13. Time and Space Complexity

Kadane processes each element exactly once.

Therefore:

```text
Time Complexity = O(n)
```

It only stores a few variables.

Therefore:

```text
Space Complexity = O(1)
```

That makes Kadane's Algorithm extremely efficient.

---

# 14. The Intuition You Should Remember

Do not memorize only the code.

Remember this decision:

```text
For every number:

Should I:

1. Continue my previous subarray?

or

2. Start a new subarray here?
```

Mathematically:

```text
currentSum =
max(
    currentElement,
    currentSum + currentElement
)
```

Then:

```text
maxSum =
max(
    maxSum,
    currentSum
)
```

A useful mental model is:

```text
              Current Element
                    |
                    v
        +---------------------+
        | Continue previous?  |
        |                     |
        | currentSum + value  |
        +----------+----------+
                   |
              compare with
                   |
        +----------v----------+
        | Start fresh?        |
        |                     |
        | value               |
        +----------+----------+
                   |
                   v
          Choose the larger
                   |
                   v
             currentSum
                   |
                   v
        Compare with maxSum
```

Once this idea is clear, Kadane’s Algorithm becomes much easier to remember than simply memorizing the code.
