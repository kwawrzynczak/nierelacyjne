from ParentManager import ParentManager
from ReservationManager import ReservationManager
from SitterManager import SitterManager

pm = ParentManager()
sm = SitterManager()
rm = ReservationManager()

parent = pm.create_parent(
    'Brajan', 
    'Sulejowska', 
    '123123123', 
    True, 
    'Janusz',
    45
)

sitter = sm.create_sitter(
    'sitters', 
    'Adam', 
    'Malysz', 
    102
)

reservation = rm.create_reservation(
    '23/11/2022', 
    10, 
    14, 
    sitter, 
    parent, 
    True
)

for rsrv in rm.find_all_reservations():
    print(f'opiekunka: {rsrv.sitter.first_name} {rsrv.sitter.last_name}')
    print(f'rodzic: {rsrv.parent.get_parent_info()}')