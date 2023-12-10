from dataclasses import dataclass
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@dataclass
class Request:
    sha_id: str
    element_id: str


def token_aware(func):
    def wrap_func(request, **kwargs):
        func(request=request, token=kwargs.__getitem__('token'))

    return wrap_func


@router.post("/token-propagation")
async def token_propagation(request: Request, token: Annotated[str, Depends(oauth2_scheme)]):
    processor(request=request, token=token)


@token_aware
def processor(request: Request, token: str) -> None:
    print(request, token)
