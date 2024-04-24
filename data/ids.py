import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Ids(SqlAlchemyBase):
    __tablename__ = 'ids'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    attraction_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
