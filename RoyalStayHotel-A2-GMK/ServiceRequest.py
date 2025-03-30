from datetime import datetime



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



print("             Test Case 7: ServiceRequest Class             ")
print("This is where we create a service request and update its status.")

# here it will test the ServiceRequest class
service1 = ServiceRequest(1, "Room Service", "Pending", "John")
# here it will print service request ID
print("Request ID:", service1.get_request_id())
# here it will print type of the request
print("Request Type:", service1.get_request_type())
# here it will print current request status
print("Request Status:", service1.get_request_status())
# here it will print assigned staff name
print("Assigned Staff:", service1.get_assigned_staff())

# now we update the status of the request
service1.set_request_status("Completed")

# here it will print updated request status
print("Updated Status:", service1.get_request_status())

