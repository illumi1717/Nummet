from typing import Dict
from fastapi import APIRouter, Depends
from .depends import *

router = APIRouter()

@router.post('/solve-inverse')
async def solve_inverse(
            inv: InverseRepository = Depends(get_inverse_repository),
            req: Dict = {}
        ):
    return await inv.solve_inverse(req)