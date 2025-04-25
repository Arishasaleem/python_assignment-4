def main():
    print("Enter two digit number u want")

    numb1 : str = input("Enter your first numb: ")
    numb1 : int = int(numb1)   
    
    numb2 : str = input("Enter your first numb: ")
    numb2 : int = int(numb2)   
    
    total : int = numb1 + numb2
    print("the total no is " + str(total) +  ".")

if __name__ == '__main__':
    main()
