PYTHON VARIABLE ANNOTATION


Type annotations in Python 3

Type annotations are a feature in Python that allow you to specify the expected data types of function arguments, return values, and variables. They help with readability, debugging, and can be used by static type checkers like mypy to validate code.


How you can use type annotations to specify function signatures and variable types

Function Signatures
You can use type annotations to specify the types of parameters and return values in function signatures. Here’s an example:

python
Copy code
def greet(name: str) -> str:
    return f"Hello, {name}!"
In this example:

name: str specifies that the name parameter should be of type str.
-> str indicates that the function returns a str.
Variable Annotations
Type annotations can also be used for variables:

python
Copy code
age: int = 25
height: float = 5.9
names: list[str] = ["Alice", "Bob", "Charlie"]


Duck typing

Duck Typing
Duck typing is a concept in Python where the type or class of an object is less important than the methods it defines or the behavior it exhibits. The name comes from the phrase "If it looks like a duck and quacks like a duck, it must be a duck."

Here’s an example:

python
Copy code
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck):
    duck.quack()

d = Duck()
p = Person()

make_it_quack(d)  # Output: Quack!
make_it_quack(p)  # Output: I'm quacking like a duck!
In this example, the make_it_quack function works with any object that has a quack method, regardless of its actual type.



How to validate your code with mypy

Validating Your Code with mypy
mypy is a static type checker for Python that can be used to check the correctness of your type annotations. Here's how you can use mypy to validate your code:

Install mypy:

bash
Copy code
pip install mypy
Write your code with type annotations:

python
Copy code
def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"
Run mypy on your code:

bash
Copy code
mypy your_script.py
mypy will check the type annotations and report any mismatches or errors.

For example, if you have the following code:

python
Copy code
def add(x: int, y: int) -> int:
    return x + y

result = add(5, "10")  # This should cause a mypy error
Running mypy on this script will produce an error because "10" is not an int.

By using type annotations, duck typing, and mypy, you can make your Python code more robust, readable, and maintainable.
