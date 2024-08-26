from datetime import time
class Package:
    def __init__(self, package_id, address, city, zipcode, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.delivery_time = None
        self.assigned_truck = 0
        self.truck_start_time = time(0,0,0)

# Hash table to hold packages
class PackageList:
    def __init__(self, buckets=10):
        self.buckets = buckets
        # create number of buckets equal to what you set it to
        self.table = [[] for bucket in range(self.buckets)]

    # simple hashing function
    def my_hash(self, key):
        return key % self.buckets
    
    # insert package into hash table: O(1)
    def insert_package(self, package):
        index = self.my_hash(package.package_id)
        self.table[index].append((package.package_id, package))

    # search to find a specific package: O(n)
    def find_package(self, package_id):
        index = self.my_hash(package_id)
        for key, package in self.table[index]:
            if key == package_id:
                return package
    
    # print all package statuses within a time range: O(n^2)
    def print_all(self, start_time=time(0,0,0), end_time=time(23,59,0)):
        for bucket in self.table:
            for key, package in bucket:
                self.get_package_status(package.package_id, start_time, end_time)

    # figure out where the package was at that time and display that to the user: O(1)
    def get_package_status(self, package_id, start_time=time(0,0,0), end_time=time(23,59,0)):
        package = self.find_package(package_id)
        # if package is delivered before end_time but after start_time, show delivery
        if start_time < package.delivery_time < end_time:
            print(f"Package ID: {package.package_id} | Address: {package.address} | City: {package.city} | Zipcode: {package.zipcode} | Deadline: {package.deadline} | Weight: {package.weight} | Status: Package delivered at: {package.delivery_time} | Truck: {package.assigned_truck}")
        # if package will be delivered after end time, and the truck start time is before the start time, it is at the hub
        elif package.delivery_time >= end_time and package.truck_start_time > end_time:
            print(f"Package ID: {package.package_id} | Address: {package.address} | City: {package.city} | Zipcode: {package.zipcode} | Deadline: {package.deadline} | Weight: {package.weight} | Status: Package at hub")
        else:
            if package_id == 9 and end_time < time(10,20,0):
                print(f"Package ID: {package.package_id} | Address: 300 State St | City: {package.city} | Zipcode: 84103 | Deadline: {package.deadline} | Weight: {package.weight} | Status: Package en route on Truck {package.assigned_truck} | Truck: {package.assigned_truck}")
            else:
                print(f"Package ID: {package.package_id} | Address: {package.address} | City: {package.city} | Zipcode: {package.zipcode} | Deadline: {package.deadline} | Weight: {package.weight} | Status: Package en route on Truck {package.assigned_truck} | Truck: {package.assigned_truck}")
