from datetime import datetime


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



print("             Test Case 2: Guest Class             ")
print("This is where we create a guest and test their info before and after updating.")

# here it will test the Guest class
guest1 = Guest(20030, "Ghazlan Mohammed Alketbi", "Ghazlan.M.Alketbi@icloud.com", "Gold")
# here it will print guest ID
print("Guest ID:", guest1.get_guest_id())
# here it will print guest name
print("Guest Name:", guest1.get_name())
# here it will print guest contact info
print("Contact Info:", guest1.get_contact_info())
# here it will print guest loyalty status
print("Loyalty Status:", guest1.get_loyalty_status())

# now we update the guest's info
guest1.set_name("Mezna Mohammed Alketbi")
guest1.set_contact_info("Mezna_Alketbi@Gmail.com")
guest1.set_loyalty_status("Bronze")

# here it will print updated guest name
print("Updated Name:", guest1.get_name())
# here it will print updated contact info
print("Updated Contact Info:", guest1.get_contact_info())
# here it will print updated loyalty status
print("Updated Loyalty Status:", guest1.get_loyalty_status())

