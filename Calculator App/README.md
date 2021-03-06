# Calculator App

This is a fully functional calculator class that can execute simple actions that are listed below.

## Functionality:

1. Addition / Subtraction
2. Multiplication / Division
3. Take (n) root of number
4. Save numbers in memory and manipulate them

## Instalation:

Run the folowing to install:

```python
pip install git+https://github.com/VilkaMini/calculatorApp
```
## Usage: 2 components

```python
from calculator import Calculator

#  Create a calculator object
myCalculator = Calculator()

# You can add, subtract, multiply, divide two number and take a n-th root of any given number

# Addition:
myCalculator.add(2, 5)

# Subraction:
myCalculator.subract(2, 5)

# Multiplication:
myCalculator.multiply(5, 2)

# Division:
myCalculator.divide(10, 2)

# Take a n-th root , format (n, number):
myCalculator.n_root(2, 4)
```
## Usage: Memory + 1 component

```python
from calculator import Calculator

# Create a calculator object with specific number in memory
# If not manually entered, calculators memory will be set to 0.0
myCalculator = Calculator(5)

# All computations will be executed with a number in memory

# Addition:
myCalculator.add(2)

# Subraction:
myCalculator.subract(2)

# Multiplication:
myCalculator.multiply(5)

# Division:
myCalculator.divide(10)

# Take a n-th root:
myCalculator.n_root(2)
```

## License:

The MIT License (MIT). Please see the [license file](./LICENSE) for more information.