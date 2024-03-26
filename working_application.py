class EuclideanAlgorithm:
    def __init__(self):
        pass

    def gcd(self, a, b):
        """
        Calculate the greatest common divisor (GCD) of the given two integers.

        Parameters：
        a -- first integer
        b -- second integer

        Returns：
        The greatest common divisor of the two integers
        """
        # Euclidean algorithm for calculating GCD
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


# Example
if __name__ == "__main__":
    #Create an instance of Euclidean Algorithm
    euclidean_algo = EuclideanAlgorithm()

    # Input two integers
    num1 = int(input("Enter first integer:"))
    num2 = int(input("Enter second integer:"))

    # Calculate the greatest common divisor and print the result
    result = euclidean_algo.gcd(num1, num2)
    print("The greatest common divisor is:", result)
