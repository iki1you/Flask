import sqlalchemy

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.String)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.Integer)
    is_finished = sqlalchemy.Column(sqlalchemy.BOOLEAN)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)