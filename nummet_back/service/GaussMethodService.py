import numpy as np

class GaussMethod:
    def makeIdentity(self, matrix):
        for nrow in range(len(matrix)-1,0,-1):
            row = matrix[nrow]
            for upper_row in matrix[:nrow]:
                factor = upper_row[nrow]

                upper_row[-1] -= factor*row[-1]
                upper_row[nrow] = 0
        return matrix

    def makeTrianglePivot(self, matrix):
        for nrow in range(len(matrix)):
            pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
            if pivot != nrow:
                matrix[nrow], matrix[pivot] = matrix[pivot], np.copy(matrix[nrow])
            row = matrix[nrow]
            divider = row[nrow] 
            if abs(divider) < 1e-10: 
                raise ValueError("The matrix is incompatible")
            row /= divider 
            for lower_row in matrix[nrow+1:]:
                factor = lower_row[nrow] 
                lower_row -= factor*row 
        return matrix

    def gaussSolvePivot(self, A, b=None):
        shape = A.shape
        assert len(shape) == 2, ("The matrix is not two-dimensional", shape) 
        A = A.copy()
        if b is not None:
            assert shape[0] == shape[1], ("The matrix is not square", shape)
            assert b.shape == (shape[0],), ("The dimensionality of the free members does not correspond to the matrix", shape, b.shape)
            A = np.c_[A, b]
        else:
            assert shape[0]+1 == shape[1], ("Incorrect matrix format", shape)
        self.makeTrianglePivot(A)
        self.makeIdentity(A)
        return A[:,-1]

    def solve(self, matrix):
        return self.gaussSolvePivot(np.array(list(map(lambda row: list(map(float, row)), matrix))))
