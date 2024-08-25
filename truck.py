from datetime import datetime, timedelta, time

class Truck:
    def __init__(self, truck_id, start_time=time(0,0,0)):
        self.truck_id = truck_id
        self.distance = 0.0
        self.time = start_time
        self.packages = []
        self.current_location_index = 0
        self.start_time = start_time
    
    # takes a list of ids and the package hash map, finds packages and loads them onto the truck: O(n)
    def load_packages(self, packages_list, truck_package_ids):
        for id in truck_package_ids:
            package = packages_list.find_package(id)
            self.packages.append(package)
            # update fields on the package for searchability later
            package.assigned_truck = self.truck_id
            package.truck_start_time = self.start_time
            
    # find the next best (closest to current location) package and deliver it: O(n)
    def deliver_next_package(self, address_list, distance_list):
        # init some variables to find best package
        distance_to_next_stop = 100.0
        best_package = None

        # loop until we find the best package possible
        for package in self.packages:
            package_address_index = address_list.index(package.address)
            #print(package_address_index, self.current_location_index)
            if distance_list[self.current_location_index][package_address_index] < distance_to_next_stop:
                distance_to_next_stop = distance_list[self.current_location_index][package_address_index]
                best_package = package
            
        # deliver the package and set metadata for the truck
        self.distance = self.distance + distance_to_next_stop
        self.current_location_index = address_list.index(best_package.address)
        self.update_time(best_package, distance_to_next_stop)
        best_package.status = "Delivered"
        self.packages.pop(self.packages.index(best_package))
    
        return len(self.packages)
    
    # update the time on the truck, and the delivery time for the package: O(1)
    def update_time(self, package, distance):
        seconds = (distance/18) * 3600
        total_time = timedelta(seconds=seconds)
        current_datetime = datetime.combine(datetime.today(), self.time)
        updated_datetime = current_datetime + total_time   
        self.time = updated_datetime.time()
        package.delivery_time = self.time

    # was having some issues setting this manually for some reason so i made a setter
    def set_start_time(self, start_time):
        self.start_time = start_time