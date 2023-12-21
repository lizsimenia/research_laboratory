import random
import time
import math

def generate_mass(num, type_data, operation):
    '''Функция создания массива, возвращает время создания массива и массив'''
    start_time, end_time = 0, 0
    mass = []
    if type_data == 'int':
        if operation == "+" or operation == "*":
            start_time = time.time()
            mass = [random.randint(2, 3) for i in range(num)]
            end_time = time.time()

        elif operation == "-":
            start_time = time.time()
            mass = [random.randint(-5, 10) for i in range(num)]
            end_time = time.time()

        elif operation == "/":
            start_time = time.time()
            mass = [random.randint(2,3) for i in range(num)]
            end_time = time.time()

        elif operation == 'log':
            start_time = time.time()
            mass = [random.randint(10, 20) for i in range(num)]
            end_time = time.time()

    elif type_data == 'float':
        if operation == "+" or operation == "*":
            start_time = time.time()
            mass = [random.uniform(2.0, 3.0) for i in range(num)]
            end_time = time.time()

        elif operation == "-":
            start_time = time.time()
            mass = [random.uniform(-5.0, 6.0) for i in range(num)]
            end_time = time.time()

        elif operation == "/":
            start_time = time.time()
            mass = [random.uniform(2.0,3.0) for i in range(num//2)]
            mass.extend([1/j for j in mass])
            if num%2 != 0:
                mass.append(random.uniform(2.0,3.0))
            end_time = time.time()

        elif operation == 'log':
            start_time = time.time()
            mass = [random.uniform(10.0, 20.0) for i in range(num)]
            end_time = time.time()

    return end_time - start_time, mass


def result_time(method, quantity, operation, type_data):
    if method == 'массив':
        mass_time, mass = generate_mass(quantity, type_data, operation)
        if operation == '+':
            res = mass[0]
            start_time = time.time()
            for i in range(1, quantity):
                res += mass[i]
            end_time = time.time()

        elif operation == '-':
            res = mass[0]
            start_time = time.time()
            for i in range(1, quantity):
                res -= mass[i]
            end_time = time.time()

        elif operation == '/' and type_data == 'int':
            res = mass[0]
            count = 0
            add = 0
            start_time = time.time()
            for i in range(1, quantity):
                res /= mass[i]
                if res <= 10**(-6):
                    add += 10**(-6) - res
                    count += 1
                    res = mass[i]
            end_time = time.time()
            if res == mass[i]:
                res = 0
            res = '{:.03e}'.format(add + res + count*10**(-6))

        elif operation == '/' and type_data == 'float':
            res = mass[0]
            start_time = time.time()
            for i in range(1, quantity//2):
                res /= mass[i]
                res /= mass[quantity//2 + i]
            if quantity%2!=0:
                res /= mass[-1]
            end_time = time.time()
            res = '{:.03e}'.format(res)

        elif operation == '*':
            res = mass[0]
            millions = 0
            add = 0
            start_time = time.time()
            for i in range(1, quantity):
                res *= mass[i]
                if res >= 10**6:
                    add += res - 10**6
                    res = mass[i]
                    millions += 1
            end_time = time.time()
            if res == 2 or res == 3:
                    res = 0
            res = '{:.03e}'.format(add + res + millions*10**6)

        elif operation == 'log':
            res = mass[0]
            start_time = time.time()
            for i in range(1, quantity):
                res = math.log(mass[i])
            end_time = time.time()

        return end_time-start_time, mass_time, mass, res

    elif method == 'переменные':

        if type_data == 'int':
            if operation == '+':
                res = 0
                start_time = time.time()
                for i in range(quantity):
                    res += random.randint(2, 3)
                end_time = time.time()

            elif operation == '-':
                res =  random.randint(-5, 10)
                start_time = time.time()
                for i in range(1, quantity):
                    res -= random.randint(-5, 10)
                end_time = time.time()

            elif operation == '/':
                res = random.randint(2,3)
                count = 0
                add = 0
                start_time = time.time()
                for i in range(1, quantity):
                    res /= random.randint(2,3)
                    if res <= 10**(-6):
                        add += 10**(-6) - res
                        count += 1
                        res = random.randint(2,3)
                end_time = time.time()
                if res == 2 or res == 3:
                    res = 0
                res = '{:.03e}'.format(add + res + count*10**(-6))

            elif operation == '*':
                res = random.randint(2, 3)
                millions = 0
                add = 0
                start_time = time.time()
                for i in range(1, quantity):
                    res *= random.randint(2, 3)
                    if res >= 10**6:
                        add += res - 10**6
                        res = random.randint(2, 3)
                        millions += 1
                end_time = time.time()
                if res == 2 or res == 3:
                    res = 0
                res = '{:.03e}'.format(add + res + millions*10**6)

            elif operation == 'log':
                res = random.randint(10, 20)
                start_time = time.time()
                for i in range(1, quantity):
                    res = math.log(random.randint(10, 20))
                end_time = time.time()

        elif type_data == 'float':
            if operation == '+':
                res = 0
                start_time = time.time()
                for i in range(quantity):
                    res += random.uniform(2.0, 3.0)
                end_time = time.time()

            elif operation == '-':
                res =  random.uniform(-5.0, 10.0)
                start_time = time.time()
                for i in range(1, quantity):
                    res -= random.uniform(-5.0, 10.0)
                end_time = time.time()

            elif operation == '/':
                res = random.uniform(2.0,3.0)
                count = 0
                add = 0
                start_time = time.time()
                for i in range(1, quantity):
                    res /= random.uniform(2.0,3.0)
                    if res <= 10**(-6):
                        add += 10**(-6) - res
                        count += 1
                        res = random.uniform(2.0,3.0)
                end_time = time.time()
                if 3.0>=res>=2.0:
                    res = 0
                res = '{:.03e}'.format(add + res + count*10**(-6))

            elif operation == '*':
                res = random.uniform(2.0,3.0)
                millions = 0
                add = 0
                start_time = time.time()
                for i in range(1, quantity):
                    res *= random.uniform(2.0,3.0)
                    if res >= 10**6:
                        add += res - 10**6
                        res = random.uniform(2.0,3.0)
                        millions += 1
                end_time = time.time()
                if 3.0>=res>=2.0:
                    res = 0
                res = '{:.03e}'.format(add + res + millions*10**6)

            elif operation == 'log':
                res = random.uniform(10.0, 20.0)
                start_time = time.time()
                for i in range(1, quantity):
                    res = math.log(random.uniform(10.0, 20.0))
                end_time = time.time()

        return end_time - start_time, res
