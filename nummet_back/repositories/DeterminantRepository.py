from service.DeterminantService import Determinant

class DeterminantRepository:
    async def solve_determinant(self, req):
        try: 
            return {
                "result": Determinant.determinant_recursive(req["matrix"])
            }
        except ValueError:
            return {
                "error": "Something went wrong..."
            }