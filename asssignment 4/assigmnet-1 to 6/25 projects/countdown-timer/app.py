import time

try:
    total_seconds = int(input("Enter time in seconds: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

while total_seconds > 0:
    mins, secs = divmod(total_seconds, 60)  
    timer = f"{mins:02d}:{secs:02d}"
    print(" Time left:", timer, end="\r")  
    time.sleep(1)
    total_seconds -= 1

print("\n Time's up!")
