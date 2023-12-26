import user_py.calculate
import numpy as np

def test_matrix_rolling_mean(data_type, operation, n):
    if operation == "+":
        expected_result = [2, 3]
    elif operation == '/':
        expected_result = [2, 3]
    elif operation == "*" :
        expected_result = [2, 3]
    elif operation == "-":
        expected_result = [-5, 10]
    elif operation == 'log' or operation == 'sqrt':
        expected_result = [10, 20]
    time, mass = user_py.calculate.generate_mass(n, data_type, operation)
    arr = np.array(mass)
    result = np.mean(arr)

    assert min(expected_result) < result < max(expected_result), f"Error"
    if min(expected_result) < result < max(expected_result):
        print(f"Test for {data_type} {operation} {n}: Complete")

operations_mass = ["+", "-", "*", "/", "log", "sqrt"]
type_data_mass = ["int", "float"]

for i_type in type_data_mass:
    for i_op in operations_mass:
        for num in range(10, 10**3):
            test_matrix_rolling_mean(i_type, i_op, num)
print("All tests Done")
