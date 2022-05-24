# "Calculating Distance in Higher Dimensional Space"

- What does that even mean?
- Blow off trying to visualize it (to reduce cognitive overhead)
- Consider the following dataframe. Are some rows closer than others? Which rows have zero distance? Which rows have the highest distance from eachother?

```
x, y, z, a, b, c
1, 1, 1, 1, 0, 1
1, 1, 1, 1, 0, 1
1, 0, 1, 1, 0, 1
0, 0, 0, 0, 1, 0
0, 0, 0, 0, 1, 0
0, 0, 0, 0, 1, 1
```

## Pythagorean Theorum is the distance between two points produced by two dimensions, two variables. We can compute the length of the hypotenuse as the distance between two points.
c^2 = a^2 + b^2

# Euclidean distance is like the Pythagorean Theorum with more than 2 variables.
a^2 = x^2 + y^2 + z^2 + ... + n^2
