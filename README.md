# calculator_Reina_Hani

EECE 435L Lab 6: a simple calculator built and tested automatically with PyBuilder.

## Functions

The calculator is in `src/main/python/calculator_Reina_Hani/__init__.py`:

- `add(x, y)`, `subtract(x, y)`, `multiply(x, y)`
- `divide(x, y)`: raises an error when dividing by zero
- `modulus(x, y)`: the remainder of x divided by y, raises an error when y is zero
- `power(x, y)`: x raised to the power of y
- `square_root(x)`: raises an error for negative numbers

## Tests

`tests/unittest/calculator_Reina_Hani/test_calculator_Reina_Hani.py` has a unit test for every function, including the error cases.

## Build

`build.py` configures PyBuilder and tells it where the tests are.

## How to run

```
pip install pybuilder
pyb run_unit_tests
```

