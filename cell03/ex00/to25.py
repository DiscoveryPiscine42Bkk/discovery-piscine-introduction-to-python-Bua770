value = int(input())
if value >= 25:
    print("error")
else:
    for num in range(value, 25):
        print(f"inside the loop, my variable is {num}")