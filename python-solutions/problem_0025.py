from utilities import fibonacci

for index, item in enumerate(fibonacci()):
    if len(str(item)) >= 1000:
        print index
        break


