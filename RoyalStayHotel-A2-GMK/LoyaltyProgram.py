from datetime import datetime


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


print("             Test Case 6: LoyaltyProgram Class             ")
print("This is where we test loyalty points and rewards before and after updating.")

# here it will test the LoyaltyProgram class
loyalty1 = LoyaltyProgram(500, ["Free Night", "Discount Voucher"])
# here it will print the current points balance
print("Points Balance:", loyalty1.get_points_balance())
# here it will print the available rewards
print("Rewards Available:", loyalty1.get_rewards_available())

# now we update the loyalty info
loyalty1.set_points_balance(600)
loyalty1.set_rewards_available(["Free Night", "Exclusive Offer"])

# here it will print updated points balance
print("Updated Points Balance:", loyalty1.get_points_balance())
# here it will print updated rewards
print("Updated Rewards:", loyalty1.get_rewards_available())

