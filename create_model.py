from DatabaseSession import DatabaseSession

from sqlalchemy import MetaData, Table, Column, Integer, Float, Boolean, String, ForeignKey, false, true, Date
from sqlalchemy.sql import func

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
    Column('max_age', Integer)
)

reservations = Table(
    'reservations', meta,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('date', Date, server_default=func.now()),
    Column('start_hour', Integer),
    Column('end_hour', Integer),
    Column('sitter_id', ForeignKey('sitters.id'), nullable=False),
    Column('parent_id', ForeignKey('parents.id'), nullable=False),
    Column('can_teach', Boolean, default=false)
)

meta.create_all(ds.engine)