from typing import Dict
from fastapi import APIRouter, Depends
from .depends import *

router = APIRouter()

@router.post('/solve-determinant')
async def solve_determinant(
            det: DeterminantRepository = Depends(get_determinant_repository),
            req: Dict = {}
        ):
    return await det.solve_determinant(req)