from datetime import time

from package import PackageList
from truck import Truck
from read_csv import import_packages, import_addresses, import_distances

# init variables
packages_list = PackageList()
truck_1 = Truck(1, time(8,0,0))
truck_2 = Truck(2, time(9,5,0))
truck_1_package_ids = [1,9,13,14,15,16,19,20,26,30,31,34,37,40,2,4,35]
truck_2_package_ids = [3,6,18,25,28,29,32,33,36,]
truck_3_package_ids = [5,7,8,10,11,12,17,21,22,23,24,27,38,39]

# import package, address, and distance data
import_packages(packages_list)
address_list = import_addresses()
distances = import_distances()

truck_1.load_packages(packages_list, truck_1_package_ids)
truck_2.load_packages(packages_list, truck_2_package_ids)

for i in range(len(truck_1_package_ids)):
    truck_1.deliver_next_package(address_list, distances)
for i in range(len(truck_2_package_ids)):
    truck_2.deliver_next_package(address_list, distances)

truck_3 = Truck(3, truck_1.time if truck_1.time < truck_2.time else truck_2.time)
truck_3.load_packages(packages_list, truck_3_package_ids)

for i in range(len(truck_3_package_ids)):
    truck_3.deliver_next_package(address_list, distances)
    
print(truck_2.time)
#print(truck_3.distance + truck_2.distance + truck_1.distance)
print(packages_list.find_package(37).delivery_time)