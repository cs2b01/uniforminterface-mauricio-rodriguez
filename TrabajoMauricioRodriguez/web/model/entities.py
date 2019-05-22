from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'Users'
    Users_id = Column(Integer, Sequence('Users_id_seq'), primary_key=True)
    Codigo = Column(Integer)
    Nombre = Column(String(50))
    Apellido = Column(String(20))
    Password = Column(String(20))
