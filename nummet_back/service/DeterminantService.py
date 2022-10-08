class Determinant:
    @staticmethod
    def zeros_matrix(rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)

        return M

    @staticmethod
    def copy_matrix(M):
        rows = len(M)
        cols = len(M[0])

        MC = Determinant.zeros_matrix(rows, cols)

        for i in range(rows):
            for j in range(cols):
                MC[i][j] = M[i][j]

        return MC

    @staticmethod
    def determinant_recursive(A, total = 0):
        indices = list(range(len(A)))
        
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val

        for fc in indices:
            As = Determinant.copy_matrix(A)
            As = As[1:]
            height = len(As) 
    
            for i in range(height): 
                As[i] = As[i][0:fc] + As[i][fc+1:] 
    
            sign = (-1) ** (fc % 2)
            sub_det = Determinant.determinant_recursive(As)
            total += sign * A[0][fc] * sub_det 
    
        return total