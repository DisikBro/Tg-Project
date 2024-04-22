import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class IDs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'attraction_ids'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    attraction_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    yandex_code = sqlalchemy.Column(sqlalchemy.String, nullable=True)
