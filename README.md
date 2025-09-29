Vector and Matrix Operations in Python

A Python implementation of basic vector and matrix operations, including addition, subtraction, multiplication, transpose, determinant, inverse, and LU decomposition.

Features
Vector Operations

Addition: v1 + v2

Subtraction: v1 - v2

Dot product: v1.dot(v2)

Norm (magnitude): v1.norm()

String representation: repr(v1)

Matrix Operations

Addition: m1 + m2

Subtraction: m1 - m2

Multiplication:

Matrix × Matrix

Matrix × Scalar

Transpose: m.transpose()

Determinant: m.determinant()

Inverse: m.inverse()

LU Decomposition: m.lu_decomposition() (returns L and U matrices)

String representation: repr(m)

Installation

No external libraries are required except Python's standard math module. Compatible with Python 3.6+.

Usage Example
from vector_matrix import Vector, Matrix

# Vector operations
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print("v1 + v2 =", v1 + v2)
print("v1 . v2 =", v1.dot(v2))
print("||v1|| =", v1.norm())

# Matrix operations
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("m1 + m2 =", m1 + m2)
print("m1 * m2 =", m1 * m2)
print("det(m1) =", m1.determinant())
print("inv(m1) =", m1.inverse())

L, U = m1.lu_decomposition()
print("L =", L)
print("U =", U)

Implementation Details

Vector: Supports basic linear algebra operations.

Matrix:

Determinant uses a recursive cofactor expansion (suitable for small matrices).

Inverse uses the cofactor and adjugate method.

LU decomposition uses Doolittle’s algorithm (L has unit diagonal).

⚠️ Note: For large matrices, determinant and inverse computations may be slow due to recursive algorithms. LU decomposition is recommended for efficiency.

License

MIT License
