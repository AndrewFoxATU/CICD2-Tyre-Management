from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from passlib.hash import bcrypt

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)  # admin or employee
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)
