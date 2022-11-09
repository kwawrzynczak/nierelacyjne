from Child import Child
from Parent import Parent
from Sitter import Sitter
from Repository import Repository
from Reservation import Reservation

repo = Repository()
child = Child('Franklin', 12)
parent = Parent('ojciec', 'matko bosko 26 mieszkania 5', '+48111222333', True, child)

repo.add(child)
repo.add(parent)

sitter = Sitter('aniela', 'rugosz', 16500)
repo.add(sitter)

reservation = Reservation('1 jan 1970', 16, 18, sitter, parent, False)

repo.add(reservation)