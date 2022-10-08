class InverseService:

    @staticmethod
    def eliminate(r1, r2, col, target=0):
        fac = (r2[col]-target) / r1[col]
        for i in range(len(r2)):
            r2[i] -= fac * r1[i]

    @staticmethod
    def gauss(a):
        for i in range(len(a)):
            if a[i][i] == 0:
                for j in range(i+1, len(a)):
                    if a[i][j] != 0:
                        a[i], a[j] = a[j], a[i]
                        break
                else:
                    raise ValueError("Matrix is not invertible")
            for j in range(i+1, len(a)):
                InverseService.eliminate(a[i], a[j], i)
        for i in range(len(a)-1, -1, -1):
            for j in range(i-1, -1, -1):
                InverseService.eliminate(a[i], a[j], i)
        for i in range(len(a)):
            InverseService.eliminate(a[i], a[i], i, target=1)
        return a

    @staticmethod
    def inverse(a):
        tmp = [[] for _ in a]
        for i,row in enumerate(a):
            assert len(row) == len(a)
            tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
        InverseService.gauss(tmp)
        ret = []
        for i in range(len(tmp)):
            ret.append(tmp[i][len(tmp[i])//2:])
        return ret
