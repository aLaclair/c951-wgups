from datetime import datetime, timedelta, time

class Truck:
    def __init__(self, truck_id, start_time=time(0,0,0)):
        self.truck_id = truck_id
        self.distance = 0.0
        self.time = start_time
        self.packages = []
        self.current_location_index = 0
        self.start_time = start_time
    
    def load_packages(self, packages_list, truck_package_ids):
        for id in truck_package_ids:
            package = packages_list.find_package(id)
            self.packages.append(package)
            package.status = f"En Route by Truck {self.truck_id}"
            

    def deliver_next_package(self, address_list, distance_list):
        # init some variables to find best package
        distance_to_next_stop = 100.0
        best_package = None

        # loop until we find the best package possible
        for package in self.packages:
            package_address_index = address_list.index(package.address)
            if self.current_location_index > package_address_index:
                if distance_list[self.current_location_index][package_address_index] < distance_to_next_stop:
                    if package.package_id == 9 and self.time < time(10,20,0):
                        self.time = time(10,20,0)
                    distance_to_next_stop = distance_list[self.current_location_index][package_address_index]
                    best_package = package
            elif self.current_location_index < package_address_index:
                if distance_list[package_address_index][self.current_location_index] < distance_to_next_stop:
                    if package.package_id == 9 and self.time < time(10,20,0):
                        self.time = time(10,20,0)
                    distance_to_next_stop = distance_list[package_address_index][self.current_location_index]
                    best_package = package
            elif self.current_location_index == package_address_index:
                distance_to_next_stop = 0.0
                best_package = package
        
        # deliver the package
        self.distance = self.distance + distance_to_next_stop
        self.current_location_index = package_address_index
        self.update_time(best_package, distance_to_next_stop)
        best_package.status = "Delivered"
        print(best_package.package_id)
        self.packages.pop(self.packages.index(best_package))
    
        return len(self.packages)
    
    def update_time(self, package, distance):
        seconds = (distance/18) * 3600
        total_time = timedelta(seconds=seconds)
        current_datetime = datetime.combine(datetime.today(), self.time)
        updated_datetime = current_datetime + total_time   
        self.time = updated_datetime.time()
        package.delivery_time = self.time

    def set_start_time(self, start_time):
        self.start_time = start_time