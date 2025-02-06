from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.databse import get_db
from app.schemas import ItemCreate, ItemResponse
from app import crud
router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse)
async def create_items(item: ItemCreate, db: AsyncSession= Depends(get_db)):
    return await crud.create_item(db, item)


@router.get("/", response_model=list[ItemResponse])
async def read_items(db: AsyncSession = Depends(get_db)):
    return await crud.get_items(db)

@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: AsyncSession= Depends(get_db)):
    item= await crud.get_item(db, item_id)
    if item is None:
        return HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: int, db: AsyncSession= Depends(get_db)):
    item = await crud.delete_item(db, item_id)
    if item is None:
        return HTTPException(status_code=404, detail="Item not found")
    return item