def generator_numbers_1(max_number: int):
    print("called generator_numbers_1 function")
    numbers = []
    for i in range(1, max_number+1):
        numbers.append(i)
    return numbers


#generator 객체 생성 함수
def generator_numbers_2(max_number : int):
    print("called generator_numbers_2 function")
    for i in range(1, max_number+1):
        yield i



numbers_1 = generator_numbers_1(10)
numbers_2 = generator_numbers_2(10)
print(numbers_1)
print(numbers_2)

gen1 = (i**2 for i in [1,2,3,4,5])
