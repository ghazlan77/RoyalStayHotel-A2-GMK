from datetime import datetime
from Booking import Booking
from Guest import Guest
from Room import Room


class Payment:
    # The constructor method is used to initialize the attributes of the Payment class
    def __init__(self, payment_id, booking, amount, payment_method):
        try:
            if payment_id <= 0:  # Ensure payment_id is a valid positive number
                raise ValueError("Payment ID must be greater than zero.")  # Raise an error if payment_id is invalid
            self._payment_id = payment_id  # Initialize the payment ID (private attribute)
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints an error message if payment_id is invalid
            self._payment_id = 0  # Default value if error occurs

        self._booking = booking  # Initialize the booking (an instance of the Booking class)

        try:
            if amount <= 0:  # Ensure the amount is a positive value
                raise ValueError("Amount must be greater than zero.")  # Raise an error if the amount is invalid
            self._amount = amount  # Initialize the payment amount (private attribute)
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints a error message if amount is invalid
            self._amount = 0  # Default value if error occurs

        self._payment_method = payment_method  # Initialize the payment method (private attribute)
        self._status = "Pending"  # Set the initial payment status as "Pending"

    # Getter method for payment ID
    def get_payment_id(self):
        return self._payment_id  # Return the payment ID

    # Setter method for payment ID
    def set_payment_id(self, payment_id):
        try:
            if payment_id <= 0:  # Ensure payment_id is a valid positive number
                raise ValueError("Payment ID must be greater than zero.")  # Raise an error if payment_id is invalid
            self._payment_id = payment_id  # Set the payment ID to a new value
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if payment_id is invalid

    # Getter method for booking associated with the payment
    def get_booking(self):
        return self._booking  # Return the associated booking

    # Setter method for booking
    def set_booking(self, booking):
        self._booking = booking  # Set the booking to a new booking instance

    # Getter method for the payment amount
    def get_amount(self):
        return self._amount  # Return the payment amount

    # Setter method for the payment amount
    def set_amount(self, amount):
        try:
            if amount <= 0:  # Ensure the amount is a positive value
                raise ValueError("Amount must be greater than zero.")  # Raise an error if amount is invalid
            self._amount = amount  # Set the payment amount to a new value
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints a error message if amount is invalid

    # Getter method for payment method (Credit Card, PayPal)
    def get_payment_method(self):
        return self._payment_method  # Return the payment method

    # Setter method for payment method
    def set_payment_method(self, payment_method):
        self._payment_method = payment_method  # Set the payment method to a new value

    # Getter method for payment status
    def get_status(self):
        return self._status  # Return the payment status (Pending, Successful, Failed)

    # Setter method for payment status
    def set_status(self, status):
        self._status = status  # Set the payment status to a new value

    # The __str__ method is used to return a string representation of the Payment object
    def __str__(self):
        # Return a formatted string that contains the payment details
        return f"Payment ID: {self._payment_id}, Booking ID: {self._booking.get_booking_id()}, Amount: {self._amount}, Payment Method: {self._payment_method}, Status: {self._status}"



print("             Test Case 4A: Payment Class             ")
print("This is where we create a payment and test its values before and after updating.")

# this is our guest
guest1 = Guest(1, "Ghazlan Mohammed Alketbi", "Ghazlan.M.Alketbi@icloud.com", "Gold")
# this is the room that is being booked
room1 = Room(101, "Single", 900, True, ["Wi-Fi", "TV"])
# this is the booking dates
booking1 = Booking(1, guest1, room1, datetime(2025, 3, 22), datetime(2025, 3, 25))

# here it will test the Payment class
payment1 = Payment(100084673387, booking1, 900, "Credit Card")
# here it will print payment ID
print("Payment ID:", payment1.get_payment_id())
# here it will print payment amount
print("Payment Amount:", payment1.get_amount())
# here it will print payment method
print("Payment Method:", payment1.get_payment_method())
# here it will print initial payment status
print("Payment Status:", payment1.get_status())

# now we update the payment amount and status
payment1.set_amount(950)
payment1.set_status("Successful")

# here it will print updated payment amount
print("Updated Amount:", payment1.get_amount())
# here it will print updated status
print("Updated Status:", payment1.get_status())


# Second test case using Apple Pay to test another payment method
print("                       Test Case 4B: Apple Pay Method                         ")
print("This is where we test another payment method apple pay")

# new booking and payment with Apple Pay
guest2 = Guest(2, "Roudha Alketbi", "Roudh.alketbi@outlook.com", "Silver")
room2 = Room(102, "Double", 1200, True, ["Wi-Fi", "TV", "Breakfast"])
booking2 = Booking(2, guest2, room2, datetime(2025, 4, 1), datetime(2025, 4, 5))

payment2 = Payment(100084673399, booking2, 4800, "Apple Pay")

print("Payment ID:", payment2.get_payment_id())
print("Payment Amount:", payment2.get_amount())
print("Payment Method:", payment2.get_payment_method())
print("Payment Status:", payment2.get_status())

# updating the second payment
payment2.set_amount(4700)
payment2.set_status("Successful")

print("Updated Amount:", payment2.get_amount())
print("Updated Status:", payment2.get_status())