class Train:
    def __init__(self, train_id, train_name, source, destination, departure_time, arrival_time):
        self.train_id = train_id
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

class RailwayManagementSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def remove_train(self, train_id):
        for train in self.trains:
            if train.train_id == train_id:
                self.trains.remove(train)
                print(f"Train {train_id} removed successfully.")
                return
        print(f"Train {train_id} not found.")

    def display_trains(self):
        for train in self.trains:
            print(f"Train ID: {train.train_id}, Train Name: {train.train_name}, Source: {train.source}, Destination: {train.destination}, Departure Time: {train.departure_time}, Arrival Time: {train.arrival_time}")

    def search_train(self, source, destination):
        for train in self.trains:
            if train.source == source and train.destination == destination:
                print(f"Train ID: {train.train_id}, Train Name: {train.train_name}, Departure Time: {train.departure_time}, Arrival Time: {train.arrival_time}")
                return
        print(f"No train found from {source} to {destination}.")

def main():
    railway_system = RailwayManagementSystem()

    while True:
        print("1. Add Train")
        print("2. Remove Train")
        print("3. Display Trains")
        print("4. Search Train")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            train_id = input("Enter train ID: ")
            train_name = input("Enter train name: ")
            source = input("Enter source station: ")
            destination = input("Enter destination station: ")
            departure ⬤
