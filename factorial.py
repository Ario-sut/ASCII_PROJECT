# Program faktorial.py
def factorial(n):
    """Menghitung faktorial dari n."""
    if n < 0:
        raise ValueError("Faktorial tidak terdefinisi untuk bilangan negatif.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Masukkanlah angka untuk menghitung faktorialnya: "))
factorial_result = factorial(num)
print("Faktorial dari {} adalah: {}".format(num, factorial_result))