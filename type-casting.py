# Type Casting refers to the process of converting a value from one data type to another. In Python, you can perform type casting using built-in functions such as int(), float(), str(), list(), tuple(), dict(), set(), and more. Here are some examples of type casting in Python:

#Implicit Type Casting (Automatic Type Conversion)
# In Python, implicit type casting occurs when the interpreter automatically converts one data type to another without the programmer's intervention. This usually happens when you perform operations between different data types. For example:
# Adding an integer and a float
num1 = 10   # int
num2 = 3.14 # float
result = num1 + num2  # The integer is implicitly converted to a float
print("Result:", result)
print("Type of result:", type(result))  # Output will be a float