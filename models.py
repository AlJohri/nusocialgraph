# http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.orm import aliased, load_only

from pprint import pprint as pp

LOCAL_DATABASE_URL = 'postgresql:///nusocialgraph'

engine = create_engine(LOCAL_DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

from socialscraper.adapters import adapter_sqlalchemy

class BaseModel(object):
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    def __init__(self,created_at,updated_at):
        self.created_at = created_at
        self.updated_at = updated_at

base_classes = (Base, BaseModel,)
fbmodels = adapter_sqlalchemy.make_models(Base, base_classes)

FacebookUser = fbmodels['FacebookUser']
FacebookPage = fbmodels['FacebookPage']
FacebookPagesUsers = fbmodels['FacebookPagesUsers']
FacebookFriend = fbmodels['FacebookFriend']
FacebookGroup = fbmodels['FacebookGroup']
FacebookGroupsUsers = fbmodels['FacebookGroupsUsers']

class SuperGroup(Base):
    __tablename__ = 'supergroups'
    __attrs__ = ['name', 'id']

    id = Column(Integer, primary_key=True)
    name = Column(String)
    inheritance = Column(String)

    def mkchild(self, group):
        if not self.is_child(group):
            self.friends.append(group)
            return self

    def rmchild(self, group):
        if self.is_child(group):
            self.children.remove(group)
            return self

    def is_child(self, group):
        return self.children.filter(SuperGroupJointTable.__table__.c.child_id == group.id).count() > 0

    def is_parent(self, group):
        return self.children.filter(SuperGroupJointTable.__table__.c.child_id == group.id).count() > 0

ParentSuperGroup = aliased(SuperGroup, name='parent_supergroup')

class SuperGroupJointTable(Base):
    __tablename__ = 'supergroupsgroups'
    __attrs__ = ['parent_id', 'child_id']

    parent_id = Column(Integer, ForeignKey("supergroups.id"), primary_key=True, unique=False)
    child_id = Column(Integer, ForeignKey("supergroups.id"), primary_key=True, unique=False)

SuperGroup.children = relationship('SuperGroup',
    secondary = SuperGroupJointTable.__table__, 
    primaryjoin = (SuperGroupJointTable.__table__.c.parent_id == SuperGroup.id),
    secondaryjoin = (SuperGroupJointTable.__table__.c.child_id == SuperGroup.id),
    backref = 'parents', 
    lazy = 'dynamic'
)

__all__ = ['Session', 'FacebookPage', 'FacebookUser', 'FacebookPagesUsers', 'FacebookFriend', 'FacebookGroup', 'FacebookGroupsUsers']

if __name__ == '__main__':
    session = Session()
    from lib import status_users
    from functools import partial
    status_users = partial(status_users, session)
