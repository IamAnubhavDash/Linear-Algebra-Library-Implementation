Vector and Matrix Operations in Python

A simple Python implementation of vector and matrix operations: addition, subtraction, multiplication, transpose, determinant, inverse, and LU decomposition.

Features
Vector Operations
-


Addition: v1 + v2 → element-wise addition

Subtraction: v1 - v2 → element-wise subtraction

Dot Product: v1.dot(v2) → computes the dot product

Norm: v1.norm() → Euclidean magnitude of the vector

Representation: repr(v1) → readable vector format

Matrix Operations

Addition: m1 + m2 → element-wise addition

Subtraction: m1 - m2 → element-wise subtraction

Multiplication: m1 * m2 → matrix × matrix or matrix × scalar

Transpose: m.transpose() → returns transposed matrix

Determinant: m.determinant() → only for square matrices

Inverse: m.inverse() → only for square, non-singular matrices

LU Decomposition: L, U = m.lu_decomposition() → returns L (lower) and U (upper) matrices

Representation: repr(m) → readable matrix format

Installation

No external dependencies, only Python’s standard math module.
Compatible with Python 3.6+.
from vector_matrix import Vector, Matrix

# Vector examples
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print("v1 + v2 =", v1 + v2)
print("v1 . v2 =", v1.dot(v2))
print("||v1|| =", v1.norm())

# Matrix examples
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("m1 + m2 =", m1 + m2)
print("m1 * m2 =", m1 * m2)
print("det(m1) =", m1.determinant())
print("inv(m1) =", m1.inverse())

L, U = m1.lu_decomposition()
print("L =", L)
print("U =", U)

Notes
-

1)Determinant and inverse are computed via recursive cofactor expansion — slow for large matrices.

2)LU decomposition uses Doolittle’s method, more efficient for larger matrices.

3)Ideal for learning and small-to-medium matrix operations.

License

MIT License
