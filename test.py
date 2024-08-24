import csv, re
from package import Package, PackageList

# init hash table
packages_list = PackageList()

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

