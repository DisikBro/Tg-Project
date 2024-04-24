import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Names(SqlAlchemyBase):
    __tablename__ = 'names'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

