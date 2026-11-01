from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, DateTime, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Specialist(Base):
    __tablename__ = 'specialists'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    login: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(500))
    email: Mapped[str] = mapped_column(String(100))
    registration_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    profile: Mapped[Optional['Profile']] = relationship(
        back_populates='specialist', uselist=False, cascade='all, delete-orphan'
    )

    publications: Mapped[List['Publication']] = relationship(
        back_populates='specialist', cascade='all, delete-orphan'
    )

    comments: Mapped[List['Comment']] = relationship(
        back_populates='specialist', cascade='all, delete-orphan'
    )

    grades: Mapped[List['Grade']] = relationship(
        back_populates='specialist', cascade='all, delete-orphan'
    )


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(50))
    specialisation: Mapped[str] = mapped_column(String(40))
    experience: Mapped[str] = mapped_column(String(100))
    information: Mapped[str] = mapped_column(String(500))

    specialist: Mapped['Specialist'] = relationship(back_populates='profile')


class Publication(Base):
    __tablename__ = 'publications'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(String(500))
    creation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    specialist: Mapped['Specialist'] = relationship(back_populates='publications')

    comments: Mapped[List['Comment']] = relationship(
        back_populates='publication', cascade='all, delete-orphan'
    )

    grades: Mapped[List['Grade']] = relationship(
        back_populates='publication', cascade='all, delete-orphan'
    )

    category: Mapped['Category'] = relationship(back_populates='publications')


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    text: Mapped[str] = mapped_column(String(500))
    creation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    specialist: Mapped['Specialist'] = relationship(back_populates='comments')

    publication: Mapped['Publication'] = relationship(back_populates='comments')


class Grade(Base):
    __tablename__ = 'grades'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    value: Mapped[int] = mapped_column(
        CheckConstraint('value >= 0 AND value <= 10'),
        nullable=False
    )

    specialist: Mapped['Specialist'] = relationship(back_populates='grades')

    publication: Mapped['Publication'] = relationship(back_populates='grades')


class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(30))

    publications: Mapped[List['Publication']] = relationship(
        back_populates='category', cascade='all, delete-orphan'
    )
