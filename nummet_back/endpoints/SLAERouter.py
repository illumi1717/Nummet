from typing import Dict
from fastapi import APIRouter, Depends
from .depends import *

router = APIRouter()

@router.post('/solve-slae')
async def solve_slae(
            slae: SLAERepository = Depends(get_slae_repository),
            req: Dict = {}
        ):
    return await slae.solve_slae(req)