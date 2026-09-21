# LeetCode 221 - Maximal Square

## Problem Description

Given an `m x n` binary matrix filled with `0` and `1`, find the largest square containing only `1`s and return its area.

### Example

**Input:**

```text
matrix =
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

**Output:**

```text
4
```

The largest square has a side length of `2`, so its area is `2 × 2 = 4`.

## Approach

Dynamic Programming is used to find the largest square ending at each cell.

For every cell containing `1`:

```text
dp[j] = min(top, left, diagonal) + 1
```

The maximum side length found is then squared to get the answer.

## Algorithm

1. Create a DP array to store the largest square side ending at each column.
2. Traverse the matrix row by row.
3. If the current cell is `1`, calculate the minimum of:

   * Top cell
   * Left cell
   * Diagonal cell
4. Add `1` to this minimum.
5. Keep track of the maximum square side.
6. Return `max_side × max_side`.

## Time Complexity

`O(m × n)`

## Space Complexity

`O(n)`

## Key Concepts

* Dynamic Programming
* Matrix Traversal
* Space Optimization

## Author

T.nandhini
