from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Item
from app.schemas import ItemCreate

async def create_item(db: AsyncSession, item: ItemCreate):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def get_items(db: AsyncSession):
    result = await db.execute(select(Item))
    return result.scalars().all()


async def get_item(db: AsyncSession, item_id: int):
    return await db.get(Item, item_id)

async def delete_item(db: AsyncSession, item_id: int):
    item = await get_item(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()
        return item
    return None