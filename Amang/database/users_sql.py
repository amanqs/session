from env import DATABASE_URL

from sqlalchemy import Column, BigInteger, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(DATABASE_URL)
BASE = declarative_base(bind=engine)
SESSION = scoped_session(sessionmaker(bind=engine))


class Users(BASE):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True)

    def init(self, user_id, channels=None):
        if DATABASE_URL == "":
            return
        self.user_id = user_id
        self.channels = channels

    # def repr(self):
    #     return "".format(self.thumbnail, self.thumbnail_status, self.video_to, self.user_id)


if DATABASE_URL != "":
    Users.table.create(checkfirst=True)


async def num_users():
    if DATABASE_URL != "":
        try:
            return SESSION.query(Users).count()
        finally:
            SESSION.close()
