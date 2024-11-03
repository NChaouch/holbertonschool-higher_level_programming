#!/usr/bin/python3

"""
import code
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String

Base = declarative_base()

"""
code
"""


class State(Base):

    """
    code class
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
