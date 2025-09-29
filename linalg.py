import math
import copy

class Vector:
    def __init__(self, data):
        self.data = list(data)
        self.size = len(data)

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.data))

    def __repr__(self):
        return f"Vector({self.data})"

class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            result = [[0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            return Matrix([[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)])
        else:
            raise ValueError("Unsupported multiplication.")

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant is defined only for square matrices.")
        return self._determinant_recursive(self.data)

    def _determinant_recursive(self, mat):
        n = len(mat)
        if n == 1:
            return mat[0][0]
        if n == 2:
            return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        det = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in mat[1:]]
            det += ((-1)**c) * mat[0][c] * self._determinant_recursive(minor)
        return det

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        n = self.rows
        cofactors = []
        for r in range(n):
            cofactor_row = []
            for c in range(n):
                minor = [row[:c] + row[c+1:] for i, row in enumerate(self.data) if i != r]
                cofactor = ((-1) ** (r + c)) * self._determinant_recursive(minor)
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
        cofactors = Matrix(cofactors).transpose()
        return cofactors * (1/det)

    def lu_decomposition(self):
        n = self.rows
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for k in range(i, n):
                sum_ = sum(L[i][j] * U[j][k] for j in range(i))
                U[i][k] = self.data[i][k] - sum_
            for k in range(i, n):
                if i == k:
                    L[i][i] = 1.0
                else:
                    sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                    L[k][i] = (self.data[k][i] - sum_) / U[i][i]
        return Matrix(L), Matrix(U)

    def __repr__(self):
        return f"Matrix({self.data})"

# Example usage:
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print("v1 + v2 =", v1 + v2)
    print("v1 . v2 =", v1.dot(v2))
    print("||v1|| =", v1.norm())

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("m1 + m2 =", m1 + m2)
    print("m1 * m2 =", m1 * m2)
    print("det(m1) =", m1.determinant())
    print("inv(m1) =", m1.inverse())
    L, U = m1.lu_decomposition()
    print("L =", L)
    print("U =", U)