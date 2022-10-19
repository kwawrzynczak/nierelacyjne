from DatabaseSession import DatabaseSession
from Child import Child
from Parent import Parent
from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter

from sqlalchemy import MetaData, Table, Column, Integer, Float, Boolean, String, ForeignKey, false, true
from sqlalchemy.orm import registry
mapper_registry = registry()

ds = DatabaseSession()
db = ds.create_new_session()
meta = MetaData()

children = Table(
    'children', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('child_name', String(50), nullable=False),
    Column('child_age', Integer, nullable=False)
)

parents = Table(
    'parents', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('parent_name', String(50), nullable=False),
    Column('address', String(255)),
    Column('phone_number', String(12), nullable=False),
    Column('is_teaching_required', Boolean, default=false),
    Column('child_id', ForeignKey('children.id'))
)

sitters = Table(
    'sitters', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50), nullable=False),
    Column('base_price', Float, nullable=False),
    Column('is_available', Boolean, default=true)
)

housekeepers = Table(
    'housekeepers', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('sitter_id', ForeignKey('sitters.id'))
)

academic_sitters = Table(
    'academic_sitters', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('sitter_id', ForeignKey('sitters.id')),
    Column('bonus', Float),
    Column('max_age', Integer)
)

mapper_registry.map_imperatively(Child, children)
mapper_registry.map_imperatively(Parent, parents)
mapper_registry.map_imperatively(Sitter, sitters)
mapper_registry.map_imperatively(Housekeeper, housekeepers)
mapper_registry.map_imperatively(AcademicSitter, academic_sitters)

meta.create_all(ds.engine)