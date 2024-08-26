# Austin LaClair, 001680934
from datetime import time

from package import PackageList
from truck import Truck
from read_csv import import_packages, import_addresses, import_distances

# init package list
packages_list = PackageList()
# init trucks with their start times and package ids
truck_1 = Truck(1, time(8,0,0))
truck_2 = Truck(2, time(9,5,0))
truck_1_package_ids = [1,13,14,15,16,19,20,26,30,31,34,37,40,2,4,35]
truck_2_package_ids = [3,6,9,18,25,28,29,32,33,36]
truck_3_package_ids = [5,7,8,10,11,12,17,21,22,23,24,27,38,39]

# import package, address, and distance data
import_packages(packages_list)
address_list = import_addresses()
distances = import_distances()

# load the first two trucks
truck_1.load_packages(packages_list, truck_1_package_ids)
truck_2.load_packages(packages_list, truck_2_package_ids)

# loop through the packages and deliver until there are no more to deliver: O(n^2)
for i in range(len(truck_1_package_ids)):
    truck_1.deliver_next_package(address_list, distances)
for i in range(len(truck_2_package_ids)):
    truck_2.deliver_next_package(address_list, distances)

# ensure that one of the trucks has come back before sending the third (aka driver switching)
truck_3 = Truck(3, truck_1.time if truck_1.time < truck_2.time else truck_2.time)
truck_3.load_packages(packages_list, truck_3_package_ids)

# loop and deliver truck 3s packages: O(n^2)
for i in range(len(truck_3_package_ids)):
    truck_3.deliver_next_package(address_list, distances)

print(f"Total Distance: {truck_1.distance + truck_2.distance + truck_3.distance} miles")

# start of UI
print("""Hello! Welcome to WGUPS. What would you like to do?\n
      1. See all packages at a specific time
      2. See a single package at a specific time
      3. Exit
      """)

# keep in the "menu" until you press 3, it also validates choice input
while True:
    choice = input("Enter a number 1, 2, 3: ")
    # find all packages in a date range or by a certain date
    if choice == "1":
        date = input("Great. Enter a time in the format HH:mm:ss using 24 hour format: ")
        date_string = date.split(":")
        print("\n\n\n")
        packages_list.print_all(end_time=time(int(date_string[0]), int(date_string[1]), int(date_string[2])))
        print("\n\n\n Please enter another number to take another action")
    # find a specific package by date and package id
    elif choice == "2":
        date = input("Great. Enter a time in the format HH:mm:ss using 24 hour format: ")
        package_id = input("What is the id of the package you are looking for? ")
        date_string = date.split(":")
        print("\n\n\n")
        packages_list.get_package_status(int(package_id), end_time=time(int(date_string[0]), int(date_string[1]), int(date_string[2])))
        print("\n\n\n Please enter another number 1to take another action")
    # exit
    elif choice == "3":
        break
    # validation
    else:
        print("Please enter 1, 2, or 3: ")

