#Scrivi un programma che chieda all'utente una lista di numeri e fornisca in output il maggiore tra tutti.

nums = []

while True:
    n = input("Insert a number. Write 'f' if you have finished: ")
    if n.isnumeric():
        nums.append(int(n))
    elif n == "f":
        break
    else:
        print("Input not valid.")

if nums:
    num_max = nums[0]   #initialization
    for num in nums:
        if num > num_max:
            num_max = num
    print(num_max)
else:
    print("No numbers inserted.")