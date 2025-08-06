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

num = int(input("Masukkan angka untuk menghitung faktorial: "))
factorial_result = factorial(num)     
print("Faktorial dari 5 adalah:", factorial(5))  # Contoh penggunaan