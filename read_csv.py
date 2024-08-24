import csv, re
from package import Package

def import_packages(packages_list):
    # read csv and add packages to hash table
    with open('./package_file.csv', mode='r') as file:
        packages_csv = csv.reader(file)
        for row in packages_csv:
            package_id = int(re.search(r'\d+', row[0]).group())
            address = row[1]
            city = row[2]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]

            # create package object, and insert to table
            package = Package(package_id, address, city, zipcode, deadline, weight)
            
            packages_list.insert_package(package)

def import_addresses():
    address_list = []
    # read address csv and make a list of addresses
    with open('./address.csv', mode='r') as file:
        address_csv = csv.reader(file)
        for row in address_csv:
            address_list.append(row[0])

    return address_list

def import_distances():
    distance_matrix = []
    with open('./distances.csv', mode='r', encoding='utf-8-sig') as file:
        distance_csv = csv.reader(file)
        for row in distance_csv:
            distance_matrix.append([float(re.search(r'\d+', row[0]).group()) for distance in row])

    return distance_matrix
