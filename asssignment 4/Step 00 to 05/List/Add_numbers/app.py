def add_many_numbers(numbers: list[int]) -> int:
    
    total = 0  
    for num in numbers:  
        total += num  
    return total  

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  
    sum_of_numbers: int = add_many_numbers(numbers)  
    print(f"Total Sum: {sum_of_numbers}")  

if __name__ == '__main__':
    main()