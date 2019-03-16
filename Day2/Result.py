from Day2.InventorySystem import InventorySystem
from utils.FileReader import FileReader

list_of_ids = FileReader.read('../sources/day2.txt')

system = InventorySystem(list_of_ids)
print('Checksum       : ', system.checksum())
print('Common letters : ', system.find_boxes_common_letters())