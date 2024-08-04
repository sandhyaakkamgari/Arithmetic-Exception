try:
    result = 10 / 0  # This will raise an ArithmeticException
    print(result)
except ArithmeticError as e:
    print("Arithmetic Exception:", e)