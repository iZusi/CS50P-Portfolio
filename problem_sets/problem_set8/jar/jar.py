# Define a class called "Jar" to represent a cookie jar
class Jar():
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Cookie jar can't be less than 0")
        self._capacity = capacity  # Set the jar's maximum capacity
        self.cookies = 0  # Initialize the number of cookies in the jar

    def __str__(self):
        # A special method to create a string representation of the jar
        cookie = "🍪"  # Define a cookie emoji
        return f"{self.cookies * cookie}"  # Return a string of cookies

    def deposit(self, n):
        # Method to add cookies to the jar
        if (self.cookies + n) > self._capacity:
            raise ValueError("Cookie jar is full!")  # Raise an error if the jar is full
        self.cookies += n  # Add the specified number of cookies to the jar

    def withdraw(self, n):
        # Method to remove cookies from the jar
        if (self.cookies - n) < 3:
            raise ValueError("Cookie jar is almost empty")  # Raise an error if there are too few cookies
        self.cookies -= n  # Remove the specified number of cookies from the jar

    @property
    def capacity(self):
        # Property to get the maximum capacity of the jar
        return self._capacity

    @property
    def size(self):
        # Property to get the current number of cookies in the jar
        return self.cookies

# Create an instance of the "Jar" class
cookies = Jar()
print(cookies)  # Print the current state of the cookie jar

# Deposit 5 cookies into the jar
cookies.deposit(5)
print(cookies)  # Print the updated state of the cookie jar

# Withdraw 2 cookies from the jar
cookies.withdraw(2)
print(cookies)  # Print the final state of the cookie jar
