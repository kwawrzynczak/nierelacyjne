from Child import Child
from ParentManager import ParentManager
from ReservationManager import ReservationManager
from SitterManager import SitterManager

pm = ParentManager()
sm = SitterManager()
rm = ReservationManager()

parent = pm.create_parent('Brajan', 'Sulejowska', '123123123', True, Child('Janusz', 49))
sitter = sm.create_sitter('sitters', 'Nielubi', 'Dzieci', 420)
reservation = rm.create_reservation('10/11/2022', 12, 14, sitter, parent, True)

for r in rm.find_all_reservations():
    print(r.get_reservation_info())