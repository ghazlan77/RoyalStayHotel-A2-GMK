from datetime import datetime
from Room import Room
from Guest import Guest

class Booking:
    # Constructor to initialize the booking details
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        try:
            if booking_id <= 0:  # Ensure booking_id is a valid positive number
                raise ValueError("Booking ID must be greater than zero.")  # Raise an error if booking_id is invalid
            self._booking_id = booking_id  # Booking ID to uniquely identify the booking
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if the booking_id is invalid
            self._booking_id = 0  # Default value if error occurs

        self._guest = guest  # Instance of Guest class to store the guest making the booking
        self._room = room  # Instance of Room class to store the room being booked

        try:
            if not isinstance(check_in_date, datetime):  # Ensure check_in_date is a datetime object
                raise TypeError(
                    "Check-in date must be a valid datetime object.")  # Raise an error if check_in_date is invalid
            self._check_in_date = check_in_date  # Check in date for the booking
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if check_in_date is invalid
            self._check_in_date = datetime.now()  # Default to the current date if error occurs

        try:
            if not isinstance(check_out_date, datetime):  # Ensure check_out_date is a datetime object
                raise TypeError(
                    "Check-out date must be a valid datetime object.")  # Raise error if check_out_date is invalid
            self._check_out_date = check_out_date  # Check out date for the booking
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if check_out_date is invalid
            self._check_out_date = datetime.now()  # Default to the current date if error occurs

    # Getter method for booking ID
    def get_booking_id(self):
        return self._booking_id  # Returns the booking ID

    # Setter method for booking ID
    def set_booking_id(self, booking_id):
        try:
            if booking_id <= 0:  # Ensure booking_id is a valid positive number
                raise ValueError("Booking ID must be greater than zero.")  # Raise an error if booking_id is invalid
            self._booking_id = booking_id  # Sets the booking ID
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if booking_id is invalid

    # Getter method for guest
    def get_guest(self):
        return self._guest  # Returns the guest information

    # Setter method for guest
    def set_guest(self, guest):
        self._guest = guest  # Sets the guest instance

    # Getter method for room
    def get_room(self):
        return self._room  # Returns the room information

    # Setter method for room
    def set_room(self, room):
        self._room = room  # Sets the room instance

    # Getter method for check in date
    def get_check_in_date(self):
        return self._check_in_date  # Returns the check in date

    # Setter method for check-in date
    def set_check_in_date(self, check_in_date):
        try:
            if not isinstance(check_in_date, datetime):  # Ensure check_in_date is a datetime object
                raise TypeError(
                    "Check in date must be a valid datetime object.")  # Raise an error if check_in_date is invalid
            self._check_in_date = check_in_date  # Sets the check in date
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if check_in_date is invalid

    # Getter method for check out date
    def get_check_out_date(self):
        return self._check_out_date  # Returns the check out date

    # Setter method for check out date
    def set_check_out_date(self, check_out_date):
        try:
            if not isinstance(check_out_date, datetime):  # Ensure check_out_date is a datetime object
                raise TypeError(
                    "Check out date must be a valid datetime object.")  # Raise error if check_out_date is invalid
            self._check_out_date = check_out_date  # Sets the check-out date
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if check_out_date is invalid

    # String representation method to print a summary of the booking
    def __str__(self):
        # Returns a formatted string with booking details
        return f"Booking ID: {self._booking_id}, Guest: {self._guest.get_name()}, Room: {self._room.get_room_number()}, Check in: {self._check_in_date}, Check out: {self._check_out_date}"
## Method to simulate sending a booking confirmation notification to the guest
    def send_booking_confirmation(self):
        # here it will print simulating an email notification
        print(f"Notification sent to guest {self._guest.get_name()} for booking ID {self._booking_id}")

    # This method will show the details of a reservation
    def show_reservation_details(self):
        # here it will print the booking ID
        print(f"Booking ID: {self._booking_id}")
        # here it will print the guest's name
        print(f"Guest: {self._guest.get_name()}")
        # here it will print the room number booked
        print(f"Room: {self._room.get_room_number()}")
        # here it will print the check-in date
        print(f"Check-in: {self._check_in_date.date()}")
        # here it will print the check-out date
        print(f"Check-out: {self._check_out_date.date()}")

    # This method will cancel the booking we made
    def cancel_booking(self):
        # here we are changing the status of the room to available again
        self._room.set_availability_status(True)
        # now we will tell the guest that the booking is cancelled and the room is ready for booking again
        print(f"Booking {self._booking_id} canceled successfully, room {self._room.get_room_number()} is now available.")

# simulate sending an email or notification to the guest

print("             Test Case 3A: Booking Class             ")
print("This is where we create a booking, test the guest, room, and date information, and send a notification to the customer.")

# here it will test the Booking class
guest1 = Guest(1, "Ghazlan Mohammed Alketbi", "Ghazlan.M.Alketbi@icloud.com", "Gold")
room2 = Room(101, "Single", 900, True, ("Wi-Fi", "TV"))
booking1 = Booking(276611, guest1, room2, datetime(2025, 3, 22), datetime(2025, 3, 25))

# here it will print booking ID
print("Booking ID:", booking1.get_booking_id())
# here it will print the guest name from the booking
print("Guest Name:", booking1.get_guest().get_name())
# here it will print the room number from the booking
print("Room Number:", booking1.get_room().get_room_number())
# here it will print the check-in date
print("Check-in Date:", booking1.get_check_in_date().date())
# here it will print the check-out date
print("Check-out Date:", booking1.get_check_out_date().date())

# send a confirmation notification right after the booking creation
booking1.send_booking_confirmation()

# Now we update the check in and check out dates
booking1.set_check_in_date(datetime(2025, 3, 23))
booking1.set_check_out_date(datetime(2025, 3, 26))

# print updated check in and check out
print("Updated Check in Date:", booking1.get_check_in_date().date())
print("Updated Check out Date:", booking1.get_check_out_date().date())



# here we test the reservation history feature for the guest
print("              Test Case 3B: Reservation History Test             ")
print("Here we create multiple bookings and display guest reservation history clearly.")

# creating a second room to book for the guest with new dates
room3 = Room(102, "Double", 1200, True, ["Wi-Fi", "TV", "Mini Bar"])

# making another booking for the same guest but with new room and dates
booking2 = Booking(277119, guest1, room3, datetime(2025, 4, 10), datetime(2025, 4, 15))

# here we have a list to save both bookings for our guest
guest_bookings = [booking1, booking2]


# here we will print out all the bookings for the guest to test reservation history
print("Reservation History for Guest:", guest1.get_name())

# looping through each booking in the list to show details clearly
for booking in guest_bookings:

# printing booking ID for each booking
    print("Booking ID:", booking.get_booking_id())
# printing the room number for each booking
    print("Room Number:", booking.get_room().get_room_number())
# printing check-in date for each booking
    print("Check-in Date:", booking.get_check_in_date().date())
# printing check-out date for each booking
    print("Check-out Date:", booking.get_check_out_date().date())

# here we test the cancellation of the reservation clearly
print("              Test Case 3C: Reservation Cancellation Test             ")
print("Here we cancel an existing booking and check if room availability changes.")

# cancel the first booking (booking1)
booking1.cancel_booking()

# print clearly if room is available now after canceling
print("Room Availability after cancellation:", booking1.get_room().get_availability_status())

