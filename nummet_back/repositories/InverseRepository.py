from service.InverseService import InverseService

class InverseRepository:
    async def solve_inverse(self, req):
        print(req['matrix'])
        try: 
            return {
                "result": InverseService.inverse(req["matrix"])
            }
        except ValueError:
            return {
                "error": "Inverse matrix cannot be found, D(A) = 0"
            }