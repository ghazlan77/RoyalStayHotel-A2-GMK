from datetime import datetime


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



print("             Test Case 8: Feedback Class             ")
print("This is where we create feedback and test its rating and review before and after updating.")

# here it will test the Feedback class
feedback1 = Feedback(1, "Excellent stay", 5, "Great service and clean rooms!")
# here it will print feedback ID
print("Feedback ID:", feedback1.get_feedback_id())
# here it will print guest feedback title
print("Guest Feedback:", feedback1.get_guest_feedback())
# here it will print the rating given
print("Rating:", feedback1.get_rating())
# here it will print the review text
print("Review:", feedback1.get_review_text())

# now we update the rating and review
feedback1.set_rating(4)
feedback1.set_review_text("Good service, but rooms could be better.")

# here it will print updated rating
print("Updated Rating:", feedback1.get_rating())
# here it will print updated review text
print("Updated Review:", feedback1.get_review_text())


