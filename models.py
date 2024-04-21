import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Guild(Base):
    __tablename__ = 'Guilds'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    spotify_user = db.Column(db.String(255), default="test")
    enabled = db.Column(db.Boolean(), default=True)
    playlist_name = db.Column(db.String(255), nullable=False)
    playlist_id = db.Column(db.String(255), nullable=False)