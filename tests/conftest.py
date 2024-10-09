# conftest.py
import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for num in range(num_records): # Range is from 0 to what user specifies 
        a = Decimal(fake.random_number(digits=2)) # create a random 2 digit in that range
        b = Decimal(fake.random_number(digits=2)) if num % 4 != 3 else Decimal(fake.random_number(digits=1)) #rankdom 2 digit or 1 digit number (if num/4 = 3)
        operation_name = fake.random_element(elements=list(operation_mappings.keys())) #pick random string 
        operation_func = operation_mappings[operation_name] #make the oper_func equal to the value of the string which refers to the actual function 
        
        if operation_func == divide: # if 0 change it to 1
            b = Decimal('1') if b == Decimal('0') else b
        
        try: 
            if operation_func == divide and b == Decimal('0'): # if #/0 give expected = "zerodivisionerror" just incase...
                expected = "Dividing by 0: Undefined"
            else:
                expected = operation_func(a, b) # expected = the opperation performed 
        except ZeroDivisionError:
            expected = "Dividing by 0: Undefined" 
        
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)