from repositories.DeterminantRepository import DeterminantRepository
from repositories.SLAERepository import SLAERepository
from repositories.InverseRepository import InverseRepository

def get_slae_repository() -> SLAERepository:
    return SLAERepository()

def get_determinant_repository() -> DeterminantRepository:
    return DeterminantRepository()

def get_inverse_repository() -> InverseRepository:
    return InverseRepository()