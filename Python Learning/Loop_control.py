# Example using break statement
for i in range(10):
    if i == 5:
        print("Encountered 5, breaking loop")
        break         # Exit the loop when i equals 5
    print("Current value of i:", i)
print("Loop ended\n")


# Example using continue statement
print("Example using continue statement:")
for i in range(10):
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue      # Skip the rest of the loop for even numbers
    print("Processing odd number:", i)
print("Loop ended\n")


# Example using pass statement
print("Example using pass statement:")
for i in range(3):
    if i == 1:
        print("Encountered 1, but continuing loop without any action")
        pass         # Do nothing and continue the loop
    print("Current value of i:", i)
print("Loop ended")
