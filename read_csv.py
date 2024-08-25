import csv, re
from package import Package

def import_packages(packages_list):
    # read csv and add packages to hash table: O(n)
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

# read address csv and make a list: O(n)
def import_addresses():
    address_list = []
    # read address csv and make a list of addresses
    with open('./address.csv', mode='r') as file:
        address_csv = csv.reader(file)
        for row in address_csv:
            address_list.append(row[0])

    return address_list

# read distance matrix and create a 2D array to hold the information: O(n^2)
def import_distances():
    distance_matrix = []
    with open('./distances.csv', mode='r', encoding='utf-8-sig') as file:
        distance_csv = csv.reader(file)
        for row in distance_csv:
            temp = []
            for column in row:
                num = float(re.search(r"(-?\d*\.?\d+)", column).group(0) if re.search(r"(-?\d*\.?\d+)", column) else 0.0)
                temp.append(num)
            distance_matrix.append(temp)

    return distance_matrix


