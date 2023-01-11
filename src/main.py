from Child import Child
from ParentManager import ParentManager
from SitterManager import SitterManager
from ReservationManager import ReservationManager

pm = ParentManager()
sm = SitterManager()
rm = ReservationManager()

pid = pm.create_parent('Pain', 'Life Starts Now', 'One-X', True, Child('Three Days Grace', 2023 - 2003))
sid = sm.create_sitter('academic', 'Break', 'The Good Life', 2009, 1.25, 16)
rid = rm.create_reservation(
    '03/03/2020', 
    10, 
    12,
    sm.get_sitter(sid),
    pm.get_parent(pid),
    True
)

pid2 = pm.create_parent('Gone forever', 'Riot', 'Get Out Alive', False, Child('One-X', 2023 - 2006))

for parent in pm.find_all_parents():
    print(parent.get_parent_info())
