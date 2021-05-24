try:
    age = int(input('age '))
    income = 10000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Can't devide by zero")
except ValueError:
    print('Invalid Value ')


#Try: & except
