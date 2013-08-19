import sqlalchemy
from sqlalchemy import create_engine
print sqlalchemy.__version__ 
engine = create_engine('sqlite:///:memory:', echo=True)
print engine.execute("select 1").scalar()

print
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.password)


print repr(User.__table__)
u1 = User('Jack', '1234')
print repr(u1.__table__)
print u1.id, u1


from sqlalchemy.orm import sessionmaker
#Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
s1 = Session()
s1.add(u1)
s1.commit()
print u1.id, u1

