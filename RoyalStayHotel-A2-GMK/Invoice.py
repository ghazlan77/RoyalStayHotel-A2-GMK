from datetime import datetime
from Room import Room
from Guest import Guest
from Booking import Booking
from Payment import Payment

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



print("             Test Case 5: Invoice Class             ")
print("This is where we create an invoice and test its amount before and after updating.\n")

# first we create a guest object to use it in the booking
guest1 = Guest(1, "Ghazlan Mohammed Alketbi", "Ghazlan.M.Alketbi@icloud.com", True)
# here we create a room object so we can use it in the booking too
room2 = Room(101, "Single", 900, True, ["Wi-Fi", "TV"])
# now we make a booking using the guest and the room we created
booking1 = Booking(1, guest1, room2, datetime(2025, 3, 22), datetime(2025, 3, 25))


# here it will test the Invoice class
invoice1 = Invoice(1, booking1, 900)
# here it will print invoice ID
print("Invoice ID:", invoice1.get_invoice_id())
# here it will print booking ID linked to invoice
print("Booking ID (from Invoice):", invoice1.get_booking().get_booking_id())
# here it will print total amount of invoice
print("Invoice Amount:", invoice1.get_total_amount())

# now we update the total amount
invoice1.set_total_amount(950)

# here it will print updated invoice amount
print("Updated Invoice Amount:", invoice1.get_total_amount())

