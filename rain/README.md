```
# Rain

This project involves solving the problem of calculating the amount of rainwater retained after it rains, given a list of non-negative integers representing the heights of walls with unit width 1.

## Problem Statement

You are given a list of non-negative integers `walls`, which represents the heights of walls in a relief map. Each integer represents the height of a wall at a specific position, as if viewing the cross-section of the relief map. Your task is to calculate the total amount of rainwater that will be retained between the walls after it rains.

Implement the following function:

```python
def rain(walls) -> int:
    pass
```

**Input:**

- `walls`: A list of non-negative integers representing the heights of the walls.
  - The list can be empty.
  - The ends of the list (before index 0 and after index `walls[-1]`) are not walls and will not retain water.

**Output:**

- An integer indicating the total amount of rainwater retained.

**Constraints:**

- The length of the `walls` list will be at most 10^5.
- Each height value in the `walls` list will be a non-negative integer.

## Examples

Example 1:

```python
walls = [0, 1, 0, 2, 0, 3, 0, 4]
result = rain(walls)
print(result)
# Output: 6
```

Visual representation of the walls: `[0, 1, 0, 2, 0, 3, 0, 4]`

Example 2:

```python
walls = [2, 0, 0, 4, 0, 0, 1, 0]
result = rain(walls)
print(result)
# Output: 6
```

Visual representation of the walls: `[2, 0, 0, 4, 0, 0, 1, 0]`

