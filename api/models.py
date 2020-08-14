from sqlalchemy import Column, String, Integer, Date
from api.database import Base


class Smartphone(Base):
    __tablename__ = 'smartphones'
    id = Column('id', Integer, primary_key=True)
    brand = Column('brand', String)
    model = Column('model', String)
    specs = Column('specs', String)
    release_date = Column('release_date', Date)

    def __repr__(self):
        return "<Smartphone('%s','%s')>" % (self.brand, self.model)
