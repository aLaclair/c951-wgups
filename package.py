class Package:
    def __init__(self, package_id, address, city, zipcode, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = "At the hub"
        self.delivery_time = None

class PackageList:
    def __init__(self, buckets=10):
        self.buckets = buckets
        self.table = [[] for bucket in range(self.buckets)]

    def my_hash(self, key):
        return key % self.buckets
    
    def insert_package(self, package):
        index = self.my_hash(package.package_id)
        self.table[index].append(package)

    def find_package(self, package_id):
        index = self.my_hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package