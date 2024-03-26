class EuclideanAlgorithm:
    def __init__(self):
        pass

    def gcd(self, a, b):
        """
        Calculate the greatest common divisor (GCD) of two given integers.

        Parameters:
        a -- first integer
        b -- second integer

        Returns:
        The greatest common divisor of the two integers
        """
        # Check if a and b are positive integers
        if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
            raise ValueError("Both inputs must be positive integers.")

        # Euclidean algorithm for calculating GCD
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


# Example usage
if __name__ == "__main__":
    # Create an instance of EuclideanAlgorithm
    euclidean_algo = EuclideanAlgorithm()

    try:
        # Input two integers from the user
        num1 = int(input("Enter the first positive integer: "))
        num2 = int(input("Enter the second positive integer: "))

        # Calculate the greatest common divisor and print the result
        result = euclidean_algo.gcd(num1, num2)
        print("The greatest common divisor is:", result)

    except ValueError as ve:
        print("Error:", ve)
