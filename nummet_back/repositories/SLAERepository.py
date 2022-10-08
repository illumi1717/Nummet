from service.GaussMethodService import GaussMethod

class SLAERepository:
    async def solve_slae(self, req):
        try: 
            resultMatrix = [x for x in GaussMethod().solve(req["matrix"])]
            return {
                "result": resultMatrix
            }
        except ValueError:
            return {
                "error": "The matrix is incompatible"
            }