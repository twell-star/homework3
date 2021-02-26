# Решение задачи #2 - FizzBuzz

start_value = 1000       # начальное значение диапазона 
end_value = 20000        # конечное значение диапазон

sum_fizzbuzz = 0         # сумма искомых значений 'fizzbuzz'

for i in range(start_value, end_value+1):
    if (i % 3) == 0 and (i % 5) == 0:
        sum_fizzbuzz = sum_fizzbuzz + i                     

print(f'Сумма значений FizzBuzz в заданном диапазоне: {sum_fizzbuzz}')    
        