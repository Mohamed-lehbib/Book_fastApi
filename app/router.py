from fastapi import APIRouter, HTTPException, Path, Depends
from .config import sessionLocal
from sqlalchemy.orm import Session
from .schemas import BookSchema, RequestBook, Response
from . import crud

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create_book(request:RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(code=200, status="ok", message="Book created successfully").dict(exclude_none=True)

@router.get('/')
async def get(db:Session=Depends(get_db)):
    _book = crud.get_book(db)
    return Response(code=200, status="ok", message="Successfully fetched all data", result=_book).dict(exclude_none=True)

@router.post('/{id}')
async def get_by_id(id:int, db:Session=Depends(get_db)):
    _book = crud.get_book_by_id(db, book_id=id)
    return Response(code=200, status="ok", message="Successfully fetched book", result=_book).dict(exclude_none=True)

@router.post('/{id}')
async def update_book(request:RequestBook, db:Session=Depends(get_db)):
    _book = crud.update_book(db, book_id=request.parameter.id, title=request.parameter.title, description=request.parameter.description)
    return Response(code=200, status="ok", message="Successfully updated the data", result=_book).dict(exclude_none=True)

@router.delete('/{id}')
async def delete_book(id:int, db:Session=Depends(get_db)):
    _book = crud.remove_book(db, book_id=id)
    return Response(code=200, status="ok", message="Successfully deleted data").dict(exclude_none=True)
