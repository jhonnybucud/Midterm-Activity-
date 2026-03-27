total = 0

print("Number Processor (type 'stop' to end)\n")

while True:
    entry = input("Input a number: ")

    if entry.lower() == "stop":
        print("\nProgram ended.")
        break

    if not entry.lstrip('-').isdigit():
        print("Invalid input. Please enter a valid number.\n")
        continue

    num = int(entry)

    if num == 0:
        print("Zero entered → no change.")
    elif num % 2 == 0:
        total += num
        print(f"{num} is even → added.")
    else:
        total -= num
        print(f"{num} is odd → subtracted.")

    print(f"Current total: {total}\n")

print(f"Final total: {total}")