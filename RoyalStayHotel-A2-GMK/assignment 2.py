from datetime import datetime

# were using this import statement to work with dates and times so we can easily handle and compare check in and check out dates for bookings.

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




class Guest:
    # Constructor method to initialize a new Guest object with its details
    def __init__(self, guest_id, name, contact_info, loyalty_status):
        try:
            if not isinstance(guest_id, int):  # Check if guest_id is an integer
                raise TypeError("Guest ID must be an integer.")  # Raise an error if guest_id is not an integer
            self._guest_id = guest_id  # Initialize the guest's unique ID
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints a error message if guest_id is not an integer
            self._guest_id = 0  # Default value if error occurs
        try:
            if not isinstance(name, str) or len(name) == 0:  # Check if name is a non-empty string
                raise ValueError("Name must be a non-empty string.")  # Raise error if name is not valid
            self._name = name  # Initialize the guest's name
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints an error message if name is invalid
            self._name = "Unknown"  # Default value if error occurs

        self._contact_info = contact_info  # Initialize the guest's contact information

        allowed_statuses = ["Bronze", "Silver", "Gold"]
        try:
            if loyalty_status not in allowed_statuses:  # Check if loyalty status is Bronze Silver or Gold
                raise ValueError("Loyalty status must be Bronze Silver or Gold.")  # Raise error if invalid
            self._loyalty_status = loyalty_status  # Initialize the guest's loyalty status
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if loyalty_status is invalid
            self._loyalty_status = "Bronze"  # Default value if error occurs

    # Getter method for guest's ID
    def get_guest_id(self):
        return self._guest_id  # Return the guest's unique ID

    # Setter method for guest's ID
    def set_guest_id(self, guest_id):
        try:
            if not isinstance(guest_id, int):  # Ensure guest_id is an integer
                raise TypeError("Guest ID must be an integer.")  # Raise error if guest_id is not an integer
            self._guest_id = guest_id  # Set the guest's ID to the provided value
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if guest_id is invalid

    # Getter method for guest's name
    def get_name(self):
        return self._name  # Return the guest's name

    # Setter method for guest's name
    def set_name(self, name):
        try:
            if not isinstance(name, str) or len(name) == 0:  # Ensure name is a non-empty string
                raise ValueError("Name must be a non-empty string.")  # Raise error if name is invalid
            self._name = name  # Set the guest's name to the provided value
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if name is invalid

    # Getter method for guest's contact information
    def get_contact_info(self):
        return self._contact_info  # Return the guest's contact information

    # Setter method for guest's contact information
    def set_contact_info(self, contact_info):
        self._contact_info = contact_info  # Set the guest's contact info to the provided value

    # Getter method for guest's loyalty status
    def get_loyalty_status(self):
        return self._loyalty_status  # Return the guest's loyalty status

    # Setter method for guest's loyalty status
    def set_loyalty_status(self, loyalty_status):
        allowed_statuses = ["Bronze", "Silver", "Gold"]
        try:
            if loyalty_status not in allowed_statuses:  # Ensure loyalty status is Bronze Silver or Gold
                raise ValueError("Loyalty status must be Bronze Silver or Gold.")  # Raise error if invalid
            self._loyalty_status = loyalty_status  # Set the guest's loyalty status to the provided value
        except TypeError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if loyalty_status is invalid

    # String representation method to provide a readable string format of the guest's details
    def __str__(self):
        return f"Guest ID: {self._guest_id}, Name: {self._name}, Contact Info: {self._contact_info}, Loyalty Status: {self._loyalty_status}"



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




# Invoice Class - Represents an invoice for a booking
class Invoice:
    def __init__(self, invoice_id, booking, total_amount):
        try:
            if invoice_id <= 0:  # Ensure invoice_id is a valid positive number
                raise ValueError("Invoice ID must be greater than zero.")  # Raise an error if invoice_id is invalid
            self._invoice_id = invoice_id  # Stores the unique invoice ID.
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if invoice_id is invalid
            self._invoice_id = 0  # Default value if error occurs

        self._booking = booking  # Associates the invoice with a Booking object.

        try:
            if total_amount <= 0:  # Ensure total_amount is a positive value
                raise ValueError("Total amount must be greater than zero.")  # Raise an error if total_amount is invalid
            self._total_amount = total_amount  # Stores the total amount for the booking.
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if total_amount is invalid
            self._total_amount = 0  # Default value if error occurs

    # Getter Method for Invoice ID
    def get_invoice_id(self):
        return self._invoice_id  # Returns the unique invoice ID.

    # Setter Method for Invoice ID
    def set_invoice_id(self, invoice_id):
        try:
            if invoice_id <= 0:  # Ensure invoice_id is a valid positive number
                raise ValueError("Invoice ID must be greater than zero.")  # Raise an error if invoice_id is invalid
            self._invoice_id = invoice_id  # Sets a new invoice ID.
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if invoice_id is invalid

    # Getter Method for Booking (associates the invoice with the booking)
    def get_booking(self):
        return self._booking  # Returns the Booking object associated with the invoice.

    # Setter Method for Booking
    def set_booking(self, booking):
        self._booking = booking  # Sets the booking associated with the invoice.

    # Getter Method for Total Amount
    def get_total_amount(self):
        return self._total_amount  # Returns the total amount for the invoice.

    # Setter Method for Total Amount
    def set_total_amount(self, total_amount):
        try:
            if total_amount <= 0:  # Ensure total_amount is a positive value
                raise ValueError("Total amount must be greater than zero.")  # Raise an error if total_amount is invalid
            self._total_amount = total_amount  # Sets a new total amount for the invoice.
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if total_amount is invalid

    # String Representation of the Invoice
    def __str__(self):
        # Returns a string that represents the invoice, displaying the invoice ID, booking ID, and total amount.
        return f"Invoice ID: {self._invoice_id}, Booking ID: {self._booking.get_booking_id()}, Total Amount: {self._total_amount}"



# LoyaltyProgram Class - Represents the loyalty points and available rewards for a guest.
class LoyaltyProgram:
    # Constructor method to initialize the loyalty program with points balance and available rewards
    def __init__(self, points_balance, rewards_available):
        try:
            if points_balance < 0:  # Ensure points_balance is a non-negative value
                raise ValueError(
                    "Points balance must be greater than or equal to zero.")  # Raise an error if points_balance is invalid
            self._points_balance = points_balance  # Stores the current points balance of the guest
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if points_balance is invalid
            self._points_balance = 0  # Default value if error occurs

        try:
            if not isinstance(rewards_available, bool):  # Ensure rewards_available is a boolean value
                raise TypeError(
                    "Rewards available must be a boolean value.")  # Raise error if rewards_available is not boolean
            self._rewards_available = rewards_available  # Stores the available rewards for the guest
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if rewards_available is not boolean
            self._rewards_available = False  # Default value if error occurs

    # Getter method to retrieve the points balance
    def get_points_balance(self):
        return self._points_balance  # Returns the current points balance

    # Setter method to update the points balance
    def set_points_balance(self, points_balance):
        try:
            if points_balance < 0:  # Ensure points_balance is a non-negative value
                raise ValueError(
                    "Points balance must be greater than or equal to zero.")  # Raise error if points_balance is invalid
            self._points_balance = points_balance  # Sets a new value for points balance
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if points_balance is invalid

    # Getter method to retrieve the available rewards
    def get_rewards_available(self):
        return self._rewards_available  # Returns the available rewards

    # Setter method to update the available rewards
    def set_rewards_available(self, rewards_available):
        try:
            if not isinstance(rewards_available, bool):  # Ensure rewards_available is a boolean value
                raise TypeError(
                    "Rewards available must be a boolean value.")  # Raise error if rewards_available is not boolean
            self._rewards_available = rewards_available  # Sets a new value for rewards available
        except TypeError as e:  # Catch the TypeError exception
            print(f"Error: {e}")  # Prints error message if rewards_available is not boolean

    # String representation method to return a readable format of the LoyaltyProgram object
    def __str__(self):
        # Returns a string displaying the points balance and rewards available in a formatted way
        return f"Points Balance: {self._points_balance}, Rewards Available: {self._rewards_available}"




# ServiceRequest Class - Represents a request made by the guest for additional services
class ServiceRequest:
    # Constructor method to initialize the request with ID, type, status, and assigned staff
    def __init__(self, request_id, request_type, request_status, assigned_staff):
        try:
            if request_id <= 0:  # Ensure request_id is a valid positive number
                raise ValueError("Request ID must be greater than zero.")  # Raise an error if request_id is invalid
            self._request_id = request_id  # Initialize request ID, unique for each service request
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if request_id is invalid
            self._request_id = 0  # Default value if error occurs

        try:
            if not isinstance(request_type, str) or len(request_type) == 0:  # Ensure request_type is a non empty string
                raise ValueError(
                    "Request type must be a non empty string.")  # Raise an error if request_type is invalid
            self._request_type = request_type  # Initialize the type of request (Room Service, Housekeeping)
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if request_type is invalid
            self._request_type = "Unknown"  # Default value if an error occurs

        try:
            if not isinstance(request_status, str) or len(
                    request_status) == 0:  # Ensure request_status is a non empty string
                raise ValueError(
                    "Request status must be a non empty string.")  # Raise an error if request_status is invalid
            self._request_status = request_status  # Initialize the status of the request (Pending, Completed)
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if request_status is invalid
            self._request_status = "Pending"  # Default value if error occurs

        self._assigned_staff = assigned_staff  # Initialize the staff member assigned to handle the request

    # Getter method for request ID
    def get_request_id(self):
        return self._request_id  # Return the unique request ID

    # Setter method for request ID
    def set_request_id(self, request_id):
        try:
            if request_id <= 0:  # Ensure request_id is a valid positive number
                raise ValueError("Request ID must be greater than zero.")  # Raise an error if request_id is invalid
            self._request_id = request_id  # Set the request ID to a new value
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if request_id is invalid

    # Getter method for request type
    def get_request_type(self):
        return self._request_type  # Return the type of service request

    # Setter method for request type
    def set_request_type(self, request_type):
        try:
            if not isinstance(request_type, str) or len(request_type) == 0:  # Ensure request_type is a non empty string
                raise ValueError("Request type must be a non empty string.")  # Raise error if request_type is invalid
            self._request_type = request_type  # Set the type of service request to a new value
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if request_type is invalid

    # Getter method for request status
    def get_request_status(self):
        return self._request_status  # Return the current status of the service request

    # Setter method for request status
    def set_request_status(self, request_status):
        try:
            if not isinstance(request_status, str) or len(
                    request_status) == 0:  # Ensure request_status is a non empty string
                raise ValueError(
                    "Request status must be a non empty string.")  # Raise error if request_status is invalid
            self._request_status = request_status  # Set the status of the service request to a new value
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if request_status is invalid

    # Getter method for assigned staff
    def get_assigned_staff(self):
        return self._assigned_staff  # Return the staff member assigned to handle the request

    # Setter method for assigned staff
    def set_assigned_staff(self, assigned_staff):
        self._assigned_staff = assigned_staff  # Set the assigned staff to a new value

    # String representation method to provide a readable string format of the request details
    def __str__(self):
        # Return a formatted string displaying the request details, including ID, type, status, and assigned staff
        return f"Request ID: {self._request_id}, Type: {self._request_type}, Status: {self._request_status}, Assigned Staff: {self._assigned_staff}"





# Feedback Class - Represents feedback given by a guest after their stay
class Feedback:
    # Constructor method to initialize the feedback attributes
    def __init__(self, feedback_id, guest_feedback, rating, review_text):
        try:
            if feedback_id <= 0:  # Ensure feedback_id is a valid positive number
                raise ValueError("Feedback ID must be greater than zero.")  # Raise an error if feedback_id is invalid
            self._feedback_id = feedback_id  # Initializes the unique feedback ID
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints an error message if feedback_id is invalid
            self._feedback_id = 0  # Default value if error occurs

        try:
            if not isinstance(guest_feedback, str) or len(
                    guest_feedback) == 0:  # Ensure guest_feedback is a non empty string
                raise ValueError(
                    "Guest feedback must be a non empty string.")  # Raise an error if guest_feedback is invalid
            self._guest_feedback = guest_feedback  # Initializes the feedback provided by the guest
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if guest_feedback is invalid
            self._guest_feedback = "No feedback provided"  # Default value if error occurs

        try:
            if not (1 <= rating <= 5):  # Ensure rating is between 1 and 5
                raise ValueError("Rating must be between 1 and 5.")  # Raise an error if rating is out of bounds
            self._rating = rating  # Initializes the rating 1 to 5 stars given by the guest
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if rating is invalid
            self._rating = 0  # Default value if error occurs

        self._review_text = review_text  # Initializes the detailed review text given by the guest

    # Getter method for the feedback ID
    def get_feedback_id(self):
        return self._feedback_id  # Returns the unique feedback ID

    # Setter method for the feedback ID
    def set_feedback_id(self, feedback_id):
        try:
            if feedback_id <= 0:  # Ensure feedback_id is a valid positive number
                raise ValueError("Feedback ID must be greater than zero.")  # Raise an error if feedback_id is invalid
            self._feedback_id = feedback_id  # Sets a new feedback ID
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if feedback_id is invalid

    # Getter method for guest feedback (overall feedback)
    def get_guest_feedback(self):
        return self._guest_feedback  # Returns the overall feedback (could be a summary or sentiment)

    # Setter method for guest feedback
    def set_guest_feedback(self, guest_feedback):
        try:
            if not isinstance(guest_feedback, str) or len(
                    guest_feedback) == 0:  # Ensure guest_feedback is a non empty string
                raise ValueError(
                    "Guest feedback must be a non empty string.")  # Raise error if guest_feedback is invalid
            self._guest_feedback = guest_feedback  # Sets the overall guest feedback
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if guest_feedback is invalid

    # Getter method for rating
    def get_rating(self):
        return self._rating  # Returns the rating given by the guest

    # Setter method for rating
    def set_rating(self, rating):
        try:
            if not (1 <= rating <= 5):  # Ensure rating is between 1 and 5
                raise ValueError("Rating must be between 1 and 5.")  # Raise error if rating is out of bounds
            self._rating = rating  # Sets the rating given by the guest
        except ValueError as e:  # Catch the ValueError exception
            print(f"Error: {e}")  # Prints error message if rating is invalid

    # Getter method for review text
    def get_review_text(self):
        return self._review_text  # Returns the detailed review text written by the guest

    # Setter method for review text
    def set_review_text(self, review_text):
        self._review_text = review_text  # Sets the detailed review text

    # String representation method to display feedback details
    def __str__(self):
        # Returns a formatted string that provides feedback details
        return f"Feedback ID: {self._feedback_id}, Rating: {self._rating}, Review: {self._review_text}"


