from DatabaseSession import DatabaseSession

from sqlalchemy import MetaData, Table, Column, Integer, Float, Boolean, String, ForeignKey, false, true

ds = DatabaseSession()
db = ds.create_new_session()
meta = MetaData()

children = Table(
    'children', meta,
    Column('child_id', Integer, autoincrement=True, primary_key=True),
    Column('child_name', String(50), nullable=False),
    Column('child_age', Integer, nullable=False)
)

parents = Table(
    'parents', meta,
    Column('parent_id', Integer, autoincrement=True, primary_key=True),
    Column('parent_name', String(50), nullable=False),
    Column('address', String(255)),
    Column('phone_number', String(12), nullable=False),
    Column('is_teaching_required', Boolean, default=false),
    Column('child_id', ForeignKey('children.child_id'))
)

sitters = Table(
    'sitters', meta,
    Column('sitter_id', Integer, autoincrement=True, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50), nullable=False),
    Column('base_price', Float, nullable=False),
    Column('is_available', Boolean, default=true)
)

housekeepers = Table(
    'housekeepers', meta,
    Column('housekeeper_id', Integer, autoincrement=True, primary_key=True),
    Column('sitter_id', ForeignKey('sitters.sitter_id'))
)

academic_sitters = Table(
    'academic_sitters', meta,
    Column('academic_sitter_id', Integer, autoincrement=True, primary_key=True),
    Column('sitter_id', ForeignKey('sitters.sitter_id')),
    Column('bonus', Float),
    Column('max_age', Integer)
)

meta.create_all(ds.engine)