from typing import List, Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Time, Timestamp

class Base(DeclarativeBase):
    pass

class Songs(Base):
    __tablename__ = "song"

    song_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    duration: Mapped[str] = Column(Time, default="00:00:00")

class Artist(Base):
    __tablename__ = "artist"

    artist_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    artist: Mapped[str] = Column(String, default="Artist Name")

class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    genre: Mapped[str] = Column(String, default="Genre")

class Album(Base):
    __tablename__ = "album"

    album_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    album_title: Mapped[str] = Column(String, default="Album Title")
    release_date: Mapped[str] = Column(Timestamp, default="00:00:00")

class Playlist(Base):
    __tablename__ = "playlist"

    playlist_id: Mapped[int] = mapped_column(primary_key=true, index=True)
    playlist_name: Mapped[str] = Column(String, default="Playlist Name")
    playlist_owner_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    created_on: Mapped[str] = 