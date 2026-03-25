from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm.attributes import Mapped




class Base(DeclarativeBase): pass


class Users(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    email:Mapped[int] = mapped_column(String, unique=True)
    password:Mapped[int] = mapped_column(String)
class Trip(Base):
    __tablename__ = 'trips'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    from_city:Mapped[str] = mapped_column(String)
    to_city:Mapped[str] = mapped_column(String)
    price:Mapped[float] = mapped_column(Float)
class Booking(Base):
    __tablename__ = 'bookings'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    trip_id:Mapped[int] = mapped_column(ForeignKey('trips.id'))