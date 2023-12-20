import user_py.calculate
import time
import random
import sys

# print(user_py.calculate.generate_mass(10000, 'int'))
# print(user_py.calculate.generate_mass(10000, 'float'))

exp = 3

# print("'массив', 200000000, '+', 'int'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '+', 'int'))

# print("'массив', 200000000, '+', 'float'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '+', 'float'))


# print("'массив', 200000000, '-', 'int'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '-', 'int'))

# print("'массив', 200000000, '-', 'float'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '+', 'float'))


# print("'массив', 200000000, '*', 'int'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '*', 'int'))

# print("'массив', 200000000, '*', 'float'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '*', 'float'))


# print("'массив', 200000000, '/', 'int'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '/', 'int'))

# print("'массив', 200000000, '/', 'float'")
# for i in range(exp):
#     print(user_py.calculate.result_time('массив', 200000000, '/', 'float'))


# print("'переменные', 200000000, '+', 'int'")
# for i in range(exp):
#     print(user_py.calculate.result_time('переменные', 200000000, '+', 'int'))

sys.set_int_max_str_digits(0)
# res = 1
# start = time.time()
# for i in range(1, 200000000+1):
#     res *= random.randint(2, 4)
#     if res > 10**6:
#         res = 1
# end = time.time()
# print(res, end - start)
# print(2**200*10**6*3**200*10**6)

# res = 1
# start = time.time()
# for i in range(1, 200000000+1):
#     res *= random.randint(2, 4)
# end = time.time()
# print(res, end - start)
# res = 1
# start = time.time()
# for i in range(1, 200000000+1):
#     res *= random.randint(2, 4)
# end = time.time()
# print(res, end - start)


# def umn_2(mass):
#     res = 1
#     n = len(mass)
#     start_time = time.time()
#     for i in range(n):
#         res *= mass[i]
#     end_time = time.time()
#     return res, end_time - start_time

# def umn_1(mass, n):
#     res = 1
#     start_time = time.time()
#     count_mil = 0
#     for i in range(n):
#         res *= mass[i]
#         if res > 10**6:
#             count_mil += 1
#             res = 1
#     # count_2, count_3 = mass.count(2), mass.count(3)
#     end_time = time.time()
#     ress = '{:.03e}'.format(count_mil*10**6)
#     return ress, end_time - start_time

# for elem in range(190*10**6, 200*10**6+1, 10**6):
#     start_time = time.time()
#     mass = [random.randint(2, 3) for _ in range(elem)]
#     end_time = time.time()
#     print(f'Генерация массива {elem}:', end_time - start_time)
#     print(umn_1(mass, elem))

# a = 6**(300*10**6) - 2**(100*10**6) - 3**(100*10**6)
# print(a)


# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def generate_coprime_sequence(n):
#     coprime_sequence = [1]  # Начинаем с 1, так как 1 взаимно просто со всеми числами
#     for i in range(2, n + 1):
#         if gcd(coprime_sequence[-1], i) == 1:
#             coprime_sequence.append(i)
#     return coprime_sequence

# n = 200  # Количество чисел в последовательности
# result = generate_coprime_sequence(n)
# print(result)

# print(umn_1(mass_100))
# print(umn_2(mass_100))

# print(umn_1(mass_1000))
# print(umn_2(mass_1000))

# print(umn_1(mass_10000))
# print(umn_2(mass_10000))

# sys.set_int_max_str_digits(0)

# start_time = time.time()
# mass_200mln = [random.randint(2, 3) for i in range(200*10**6)]
# end_time = time.time()
# print(end_time - start_time)
# print(umn_1(mass_200mln))
# print(umn_2(mass_200mln))

# quantity = 200*10**6
# mass = []

# start_time = time.time()
# mass = [random.uniform(2.0,3.0) for i in range(quantity//2)]
# mass.extend([1/j for j in mass])
# if quantity%2 != 0:
#     mass.append(random.uniform(2.0,3.0))
# end_time = time.time()


# print(end_time - start_time)

# res = 10**6
# start_time = time.time()
# for i in range(quantity//2):
#     res /= mass[i]
#     res /= mass[quantity//2 + i]
# if quantity%2!=0:
#     res /= mass[-1]
# end_time = time.time()

# print(res, end_time - start_time)

# start_time = time.time()
# mass = [i for i in range(200*10**6, 1, 0)]
# end_time = time.time()
# res = mass
# for j in mass:

# print(mass[-1], end_time-start_time)
