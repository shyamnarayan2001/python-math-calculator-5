# Python Math Calculator

A simple Python-based calculator for basic mathematical operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division handling)

## Project Structure

```
python-math-calculator-5/
├── calculator.py          # Main calculator module
├── test_calculator.py     # Unit tests
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Installation

```bash
# Clone the repository
git clone https://github.com/shyamnarayan2001/python-math-calculator-5.git

# Navigate to the project directory
cd python-math-calculator-5

# Install dependencies
pip install -r requirements.txt
```

## Usage

```python
from calculator import Calculator

calc = Calculator()

# Addition
result = calc.add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Subtraction
result = calc.subtract(10, 4)
print(f"10 - 4 = {result}")  # Output: 10 - 4 = 6

# Multiplication
result = calc.multiply(6, 7)
print(f"6 × 7 = {result}")  # Output: 6 × 7 = 42

# Division
result = calc.divide(20, 4)
print(f"20 ÷ 4 = {result}")  # Output: 20 ÷ 4 = 5.0
```

## Running Tests

```bash
pytest test_calculator.py -v
```

## Development

This project follows standard Python development practices:

- Code formatting with black
- Type hints for better code quality
- Comprehensive unit tests
- CI/CD pipeline for automated testing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
