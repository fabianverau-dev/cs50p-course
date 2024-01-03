# # Creating variables and turns it into Integers.
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # Round the result
# # z = round(x + y)

# # print(f"{z:,}")

# # Division
# # z = round(x / y, 2)
# z = x / y
# print(f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
    return n ** 2
main()