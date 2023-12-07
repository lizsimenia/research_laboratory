import random
import time

def generate_mass(num, type_data):
    '''Функция создания массива, возвращает время создания массива и массив'''
    start_time, end_time = 0, 0
    mass = []
    if type_data == 'int':
        start_time = time.time()
        mass = [random.randint(1, 10) for i in range(num)]
        end_time = time.time()
        init = random.randint(1, 10)
    elif type_data == 'float':
        start_time = time.time()
        mass = [random.uniform(1.0, 10.0) for i in range(num)]
        end_time = time.time()
        init = random.uniform(1.0, 10.0)
    return end_time - start_time, mass, init


def result_time(method, quantity, operation, type_data):
    if method == 'массив':
        mass_time, mass, init= generate_mass(quantity, type_data)
        if operation == '+':
            start_time = time.time()
            for i in range(quantity):
                init += mass[i]
                if init >= 10**6:
                    init = mass[i]
            end_time = time.time()
            #sum(mass)/quantity

        elif operation == '-':
            start_time = time.time()
            for i in range(quantity):
                init -= mass[i]
                if init <= -10**3:
                    init = mass[i]
            end_time = time.time()

        elif operation == '*':
            start_time = time.time()
            for i in range(quantity):
                init *= mass[i]
                if init >= 10**6:
                    init = mass[i]
            end_time = time.time()

        elif operation == '/':
            start_time = time.time()
            for i in range(quantity):
                init /= mass[i]
                if round(init) == 0:
                    init = mass[i]
            end_time = time.time()

        return end_time - start_time, mass_time

    elif method == 'переменные':
        if type_data == 'int':
            init = random.randint(1, 10)
            if operation == '+':
                start_time = time.time()
                for _ in range(quantity):
                    init += random.randint(1, 10)
                    if init >= 10**6:
                        init = random.randint(1, 10)
                end_time = time.time()

            elif operation == '-':
                start_time = time.time()
                for _ in range(quantity):
                    init -= random.randint(1, 10)
                    if init <= -10**3:
                        init = random.randint(1, 10)
                end_time = time.time()

            elif operation == '*':
                start_time = time.time()
                for _ in range(quantity):
                    init *= random.randint(1, 10)
                    if init >= 10**6:
                        init = random.randint(1, 10)
                end_time = time.time()

            elif operation == '/':
                start_time = time.time()
                for _ in range(quantity):
                    init /= random.randint(1, 10)
                    if round(init) == 0:
                        init = random.randint(1, 10)
                end_time = time.time()

        elif type_data == 'float':
            init = random.uniform(1.0, 10.0)
            if operation == '+':
                start_time = time.time()
                for _ in range(quantity):
                    init += random.uniform(1.0, 10.0)
                    if init >= 10**6:
                        init = random.uniform(1.0, 10.0)
                end_time = time.time()

            elif operation == '-':
                start_time = time.time()
                for _ in range(quantity):
                    init -= random.uniform(1.0, 10.0)
                    if init <= -10**3:
                        init = random.uniform(1.0, 10.0)
                end_time = time.time()

            elif operation == '*':
                start_time = time.time()
                for _ in range(quantity):
                    init *= random.uniform(1.0, 10.0)
                    if init >= 10**6:
                        init = random.uniform(1.0, 10.0)
                    end_time = time.time()

            elif operation == '/':
                start_time = time.time()
                for _ in range(quantity):
                    init /= random.uniform(1.0, 10.0)
                    if round(init) == 0:
                        init = random.uniform(1.0, 10.0)
                end_time = time.time()

        return end_time - start_time, 'ff'
