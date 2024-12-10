from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Book
from app.schemas import BookCreate

async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_books(db: AsyncSession):
    result = await db.execute(select(Book))
    return result.scalars().all()

async def get_book(db: AsyncSession, book_id: int):
    return await db.get(Book, book_id)

async def update_book(db: AsyncSession, book_id: int, book: BookCreate):
    db_book = await db.get(Book, book_id)
    if not db_book:
        return None
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    await db.commit()
    return db_book

async def delete_book(db: AsyncSession, book_id: int):
    db_book = await db.get(Book, book_id)
    if db_book:
        await db.delete(db_book)
        await db.commit()
        return True
    return False
