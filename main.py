from __future__ import annotations
import math
import statistics
import random
import ast
import operator
from typing import List
from fastmcp import FastMCP

# Initialize the Server
mcp = FastMCP("Unified-Math-Tools-Server")

# Helper Functions (Internal Use)
def _as_number(x) -> float:
    """Converts input to a float, raises TypeError if invalid."""
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise TypeError(f"Invalid number: {x}")

def _as_int(x) -> int:
    """Converts input to an integer, raises ValueError if not an integer."""
    val = _as_number(x)
    if not val.is_integer():
        raise ValueError("Expected integer")
    return int(val)

def _as_list(data: List[float]) -> List[float]:
    """Ensures input is a list of floats."""
    if not data:
        raise ValueError("Input list cannot be empty")
    return [_as_number(x) for x in data]

#1. Basic Arithmetic (Add, Subtract, Multiply, Divide, Modulo, Power)
@mcp.tool
async def add(numbers: List[float]) -> float:
    """Adds multiple numbers."""
    return sum(_as_list(numbers))

@mcp.tool
async def multiply(numbers: List[float]) -> float:
    """Multiplies multiple numbers."""
    result = 1.0
    for n in _as_list(numbers):
        result *= n
    return result

@mcp.tool
async def subtract(numbers: List[float]) -> float:
    """Subtracts numbers sequentially: a - b - c ..."""
    nums = _as_list(numbers)
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result

@mcp.tool
async def divide(numbers: List[float]) -> float:
    """Divides numbers sequentially: a / b / c ..."""
    nums = _as_list(numbers)
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            raise ValueError("Division by zero")
        result /= n
    return result


@mcp.tool
async def divide_multiple(numbers: List[float]) -> float:
    """Divides numbers sequentially: a / b / c ..."""
    nums = _as_list(numbers)
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            raise ValueError("Division by zero")
        result /= n
    return result

@mcp.tool
async def modulo(a: float, b: float) -> float:
    """Calculates the remainder of division (a % b)."""
    return _as_number(a) % _as_number(b)

@mcp.tool
async def power(base: float, exponent: float) -> float:
    """Calculates the base raised to the power of the exponent."""
    return math.pow(_as_number(base), _as_number(exponent))

# 2. Advanced Math (Square Root, Logarithms) 

@mcp.tool
async def sqrt(x: float) -> float:
    """Calculates the square root of a positive number."""
    val = _as_number(x)
    if val < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(val)

@mcp.tool
async def log(x: float, base: float = 2.718281828) -> float:
    """
    Calculates the logarithm of x with a specific base.
    Defaults to Natural Log (base e) if base is not provided.
    """
    val = _as_number(x)
    b = _as_number(base)
    if val <= 0:
        raise ValueError("Logarithm input must be positive.")
    return math.log(val, b)

@mcp.tool
async def log10(x: float) -> float:
    """Calculates the base-10 logarithm of x."""
    val = _as_number(x)
    if val <= 0:
        raise ValueError("Logarithm input must be positive.")
    return math.log10(val)

#3. Number Theory(Factorial, GCD, LCM)

@mcp.tool
async def factorial(x: int) -> int:
    """Calculates the factorial of a non-negative integer (x!)."""
    n = _as_int(x)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

@mcp.tool
async def gcd(a: int, b: int) -> int:
    """Calculates the Greatest Common Divisor (GCD) of two integers."""
    return math.gcd(_as_int(a), _as_int(b))

@mcp.tool
async def lcm(a: int, b: int) -> int:
    """Calculates the Least Common Multiple (LCM) of two integers."""
    return math.lcm(_as_int(a), _as_int(b))

# 4. Trigonometry(Sine, Cosine, Tangent, Degree-Radian Conversion)

@mcp.tool
async def sin(x: float) -> float:
    """Calculates the sine of x (input in radians)."""
    return math.sin(_as_number(x))

@mcp.tool
async def cos(x: float) -> float:
    """Calculates the cosine of x (input in radians)."""
    return math.cos(_as_number(x))

@mcp.tool
async def tan(x: float) -> float:
    """Calculates the tangent of x (input in radians)."""
    return math.tan(_as_number(x))

@mcp.tool
async def degrees_to_radians(degrees: float) -> float:
    """Converts an angle from degrees to radians."""
    return math.radians(_as_number(degrees))

@mcp.tool
async def radians_to_degrees(radians: float) -> float:
    """Converts an angle from radians to degrees."""
    return math.degrees(_as_number(radians))

#5. Statistics (Mean, Median, Standard Deviation, Variance)

@mcp.tool
async def mean(data: list[float]) -> float:
    """Calculates the arithmetic mean (average) of a list of numbers."""
    if not data:
        raise ValueError("Input list cannot be empty.")
    return statistics.mean(data)

@mcp.tool
async def median(data: list[float]) -> float:
    """Calculates the median (middle value) of a list of numbers."""
    if not data:
        raise ValueError("Input list cannot be empty.")
    return statistics.median(data)

@mcp.tool
async def stdev(data: list[float]) -> float:
    """Calculates the standard deviation of a sample."""
    if len(data) < 2:
        raise ValueError("Standard deviation requires at least two data points.")
    return statistics.stdev(data)

@mcp.tool
async def variance(data: list[float]) -> float:
    """Calculates the variance of a sample."""
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points.")
    return statistics.variance(data)

#6. Geometry(Hypotenuse, Distance, Area Calculations)
@mcp.tool
async def hypotenuse(a: float, b: float) -> float:
    """Calculates the length of the hypotenuse of a right triangle (sqrt(a^2 + b^2))."""
    return math.hypot(_as_number(a), _as_number(b))

@mcp.tool
async def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.dist((_as_number(x1), _as_number(y1)), (_as_number(x2), _as_number(y2)))

@mcp.tool
async def circle_area(radius: float) -> float:
    """Calculates the area of a circle given its radius."""
    r = _as_number(radius)
    if r < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (r ** 2)

#7. Utilities & Rounding(Absolute Value, Floor, Ceil, Round, Random Number Generation, Constants)

@mcp.tool
async def abs_val(x: float) -> float:
    """Calculates the absolute value of x."""
    return abs(_as_number(x))

@mcp.tool
async def floor(x: float) -> int:
    """Rounds a number DOWN to the nearest integer."""
    return math.floor(_as_number(x))

@mcp.tool
async def ceil(x: float) -> int:
    """Rounds a number UP to the nearest integer."""
    return math.ceil(_as_number(x))

@mcp.tool
async def round_num(x: float, digits: int = 0) -> float:
    """Rounds a number to a specified number of decimal digits."""
    return round(_as_number(x), _as_int(digits))

@mcp.tool
async def random_int(min_val: int, max_val: int) -> int:
    """Generates a random integer between min_val and max_val (inclusive)."""
    return random.randint(_as_int(min_val), _as_int(max_val))

@mcp.tool
async def get_pi() -> float:
    """Returns the value of Pi."""
    return math.pi

@mcp.tool
async def get_e() -> float:
    """Returns the value of Euler's number e."""
    return math.e



#8. Distance between Points (Absolute Difference,Euclidean Distance in 2D/3D, Manhattan Distance)

@mcp.tool
async def distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Calculates the Euclidean distance between two points (x1, y1, z1) and (x2, y2, z2)."""
    return math.dist((_as_number(x1), _as_number(y1), _as_number(z1)), (_as_number(x2), _as_number(y2), _as_number(z2)))

@mcp.tool
async def manhattan_distance(point1: List[float], point2: List[float]) -> float:
    """Calculates the Manhattan distance between two points in n-dimensional space."""
    p1 = _as_list(point1)
    p2 = _as_list(point2)
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions.")
    return sum(abs(a - b) for a, b in zip(p1, p2))

@mcp.tool
async def absolute_difference(a: float, b: float) -> float:
    """Calculates the absolute difference between two numbers."""
    return abs(_as_number(a) - _as_number(b))


if __name__ == "__main__":
    mcp.run()
