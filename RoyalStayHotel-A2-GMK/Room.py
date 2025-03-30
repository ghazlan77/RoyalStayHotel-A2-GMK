from datetime import datetime


# define the Room class to represent a hotel room

class Room:
    # constructor method to initialize room attributes
    def __init__(self, room_number, room_type, price_per_night, availability_status, amenities):
        try:
            if price_per_night <= 0:  # Check if price is valid (it has to be greater than 0)
                raise ValueError("Price per night must be greater than zero.")  # Raise error if the price is invalid
            self._price_per_night = price_per_night  # Store the price per night for the room
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if the price is invalid
            self._price_per_night = 0  # Default value if error occurs

        try:
            if not isinstance(availability_status, bool):  # Check if availability status is a boolean
                raise TypeError(
                    "Availability status must be a boolean value.")  # Raise an error if status is not boolean
            self._availability_status = availability_status  # Store the availability status whether True or False
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if the status is not boolean
            self._availability_status = False  # Default value if error occurs

        self._room_number = room_number  # Store the room number (private attribute)
        self._room_type = room_type  # Store the type of the room ( Single, Double)
        self._amenities = amenities  # Store a list of amenities for the room (Wi-Fi, TV)

    # Getter method to retrieve the room number
    def get_room_number(self):
        return self._room_number  # Return the room number

    # Setter method to set the room number
    def set_room_number(self, room_number):
        self._room_number = room_number  # Update the room number attribute

    # Getter method to retrieve the room type (Single, Double)
    def get_room_type(self):
        return self._room_type  # Return the room type

    # Setter method to set the room type
    def set_room_type(self, room_type):
        self._room_type = room_type  # Update the room type attribute

    # Getter method to retrieve the price per night
    def get_price_per_night(self):
        return self._price_per_night  # Return the price per night for the room

    # Setter method to set the price per night
    def set_price_per_night(self, price):
        try:
            if price <= 0:  # Ensure the price is valid (it has to be greater than 0)
                raise ValueError("Price must be greater than zero.")  # Raise ValueError if price is invalid
            self._price_per_night = price  # Update the price per night attribute
        except ValueError as e:  # Catch ValueError exception
            print(f"Error: {e}")  # Prints an error message if price is invalid

    # Getter method to retrieve the availability status
    def get_availability_status(self):
        return self._availability_status  # Return the room's availability status

    # Setter method to set the availability status
    def set_availability_status(self, status):
        try:
            if not isinstance(status, bool):  # Ensure the status is boolean
                raise TypeError(
                    "Availability status must be a boolean value.")  # Raise a TypeError if status is not boolean
            self._availability_status = status  # Update the availability status attribute
        except TypeError as e:  # Catch TypeError exception
            print(f"Error: {e}")  # Prints error message if status is not boolean

    # Getter method to retrieve the room's amenities
    def get_amenities(self):
        return self._amenities  # Return the list of amenities for the room

    # Setter method to set the room's amenities
    def set_amenities(self, amenities):
        self._amenities = amenities  # Update the amenities attribute

    # Method to return a string representation of the Room object
    def __str__(self):
        # The string shows the room's number, type, price per night, and availability status
        return f"Room Number: {self._room_number}, Type: {self._room_type}, Price per night: {self._price_per_night}, Availability: {self._availability_status}"




# Test Case 1A: Room Class

print("             Test Case 1A: Room Class             ")
print("This is where we create room1 and test its attributes before and after updating.")

# here it will test the Room class
room1 = Room(101, "Single", 900, True, ["Wi-Fi", "TV", "Mini Bar"])
# here it will test the room number
print("Room Number:", room1.get_room_number())
# here it will test the room type
print("Room Type:", room1.get_room_type())
# here it will test the price per night
print("Price Per Night:", room1.get_price_per_night())
# here it will test if the room is available
print("Availability:", room1.get_availability_status())
# here it will test the amenities
print("Amenities:", room1.get_amenities())

# now we will change the values using setters
room1.set_room_number(120)  # Change the room number to 120
room1.set_room_type("Double")  # Change the room type from "Single" to "Double"
room1.set_price_per_night(1500)  # Update the price per night from 900 to 1500
room1.set_availability_status(False)  # Change the availability status to False (room is now unavailable)
room1.set_amenities(["Wi-Fi", "TV", "Mini Bar"])  # Set the room's amenities to a new list: Wi-Fi, TV, and Mini Bar

# here we check the updated room number
print("Updated Room Number:", room1.get_room_number())
# here we check the updated room type
print("Updated Room Type:", room1.get_room_type())
# here we check the updated price
print("Updated Price Per Night:", room1.get_price_per_night())
# here we check the updated availability
print("Updated Availability:", room1.get_availability_status())
# here we check the updated amenities
print("Updated Amenities:", room1.get_amenities())


# Function to filter available rooms based on criteria
def search_available_rooms(rooms, required_type, max_price, required_amenities):
    available_rooms = []  # this will hold rooms matching our criteria
    for room in rooms:  # go through each room we have
        # we check if the room matches our requirements
        if (room.get_availability_status() and  # room must be available
            room.get_room_type() == required_type and  # matches room type we need
            room.get_price_per_night() <= max_price and  # price should be equal or less than our budget
            all(amenity in room.get_amenities() for amenity in required_amenities)):  # has all amenities we want
            available_rooms.append(room)  # add room if it matches
    return available_rooms  # we return the rooms that match

# Test Case 1B: Search Available Rooms
print("             Test Case 1B: Searching for Available Rooms             ")
print("Here we search for available rooms based on room type, price, and amenities.")

# create some room examples to search from
room1 = Room(101, "Single", 900, True, ["Wi-Fi", "TV", "Mini Bar"])
room2 = Room(102, "Double", 1200, True, ["Wi-Fi", "TV"])
room3 = Room(103, "Single", 700, False, ["Wi-Fi"])
room4 = Room(104, "Single", 800, True, ["Wi-Fi", "TV"])

# list of rooms we have
all_rooms = [room1, room2, room3, room4]

# search criteria we want
room_type_needed = "Single"
max_budget = 900
amenities_needed = ["Wi-Fi", "TV"]

# perform the search
matched_rooms = search_available_rooms(all_rooms, room_type_needed, max_budget, amenities_needed)

# we print the rooms we found
print("Rooms matching the criteria:")
for matched_room in matched_rooms:
    print(matched_room)
