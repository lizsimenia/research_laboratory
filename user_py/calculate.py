import random
import time

#TODO генерировать обратные для умножения float; генерировать маленькие для int
#TODO выводить результаты вычисления
#TODO генерировать положительные и отрицательные для сложения


def generate_mass(num, type_data, operation):
    '''Функция создания массива, возвращает время создания массива и массив'''
    start_time, end_time = 0, 0
    mass = []
    if type_data == 'int':
        if operation == "+" or operation == "*":
            start_time = time.time()
            mass = [random.randint(2, 3) for i in range(num)]
            end_time = time.time()
            init = random.randint(2, 3)

        elif operation == "-":
            start_time = time.time()
            mass = [random.randint(-5, 6) for i in range(num)]
            end_time = time.time()
            init = random.randint(-5, 6)

        elif operation == "/":
            start_time = time.time()
            mass = [random.randint(1, 10) for i in range(num//2)]
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
        mass_time, mass, init= generate_mass(quantity, type_data, operation)

        if operation == '+':
            res = 0
            start_time = time.time()
            for i in range(quantity):
                res += mass[i]
            end_time = time.time()

        elif operation == '-':
            res = 10**6
            start_time = time.time()
            for i in range(quantity):
                res -= mass[i]
            end_time = time.time()

        elif operation == '/':
            #TODO: доделать чтобы не получать ноль
            res = 10**6
            start_time = time.time()
            for i in range(quantity//2):
                res //= mass[i]
                res //= mass[i]
            add = quantity-quantity//2
            if add != 0:
                for i in range(add):
                    res //= mass[0]
            end_time = time.time()

        elif operation == '*':
            res = 1
            millions = 0
            start_time = time.time()
            for i in range(quantity):
                res *= mass[i]
                if res > 10**6:
                    res = 1
                    millions += 1
            end_time = time.time()
            res = '{:.03e}'.format(millions*10**6)

        return end_time-start_time, mass_time, mass, res



        # elif operation == '*' and type_data == 'int':
        #     #TODO генерация маленьких чисел
        #     pass
        # elif operation == '*' and type_data == 'float':
        #     #TODO генерация малельньких чисел и обратные им
        #     pass
        # elif operation == '/' and type_data == 'int':
        #     #TODO
        #     pass
        # elif operation == '/' and type_data == 'float':
        #     #TODO
        #     pass



        # elif operation == '-':
        #     start_time = time.time()
        #     for i in range(quantity):
        #         init -= mass[i]
        #         if init <= -10**3:
        #             init = mass[i]
        #     end_time = time.time()

        # elif operation == '*':
        #     start_time = time.time()
        #     for i in range(quantity):
        #         init *= mass[i]
        #         if init >= 10**6:
        #             init = mass[i]
        #     end_time = time.time()

        # elif operation == '/':
        #     start_time = time.time()
        #     for i in range(quantity):
        #         init /= mass[i]
        #         if round(init) == 0:
        #             init = mass[i]
        #     end_time = time.time()

        # return end_time - start_time, mass_time, init

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

        return end_time - start_time, init
