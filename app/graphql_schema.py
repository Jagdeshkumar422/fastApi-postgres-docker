import strawberry
from sqlalchemy.future import select
from app.models import User
from app.databse import AsyncSessionLocal
from typing import List, Optional

@strawberry.type
class UserType:
    id: int
    name: str
    email: str


@strawberry.type
class Query:
    @strawberry.field
    async def get_users(self)->List[UserType]:
        async with AsyncSessionLocal() as session:
            result =  await session.execute(select(User))
            users = result.scalars().all()
            return [UserType(id=user.id, name=user.name, email=user.email ) for user in users]

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, name: str, email: str) -> UserType:
        async with AsyncSessionLocal() as session:
            user = User(name=name, email=email)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return UserType(id=user.id, name=user.name, email=user.email)
        
    @strawberry.mutation
    async def update_user(self, id: int, name: Optional[str]=None, email: Optional[str]=None)-> Optional[UserType]:
        async with AsyncSessionLocal() as session:
            user = await session.get(User, id)
            if user:
                if name:
                    user.name= name
                if email:
                    user.email= email
                await session.commit()
                await session.refresh()
                return UserType(id= user.id, name= user.name, email=user.email)
            return None
    
    @strawberry.mutation
    async def delete_user(self, id: int)-> bool:
        async with AsyncSessionLocal() as session:
            user =  await session.get(User, id)
            if user:
                await session.delete(user)
                await session.commit()
                return True
            return False
        


schema = strawberry.Schema(query=Query,mutation=Mutation)