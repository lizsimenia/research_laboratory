import random
import time

# import gen_by_mass

def generate_mass(num):
    '''Функция создания массива, время создания массива и массив'''
    start_time = time.time()
    mass = [random.randint(1, 10) for i in range(num)]
    end_time = time.time()
    return end_time - start_time, mass

def sign_action(sign):
    if sign_action == '+':
        pass
    elif sign_action == '-':
        pass
    else: pass


def result_time(method, quantity, operation, type):
    if method == 'массив':
        mass, mass_time = generate_mass(quantity)
    elif method == 'переменные':
        pass

    # else:
    #     pass
    # c = 300*10**6
    # summ = 1
    # start_time = time.time()
    # for i in range(c):
    #     summ *= random.randint(1, 10)
    #     if summ >= 10**6:
    #         summ = 1
    # end_time = time.time()
    # print(summ, end_time-start_time)
    return 1512.445, {"sr_znach_mass": 5, "summ_res": 52}
