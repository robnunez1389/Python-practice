# Looping through even numbers
for num in range(2,11,2):
    #Looping through odd numbers
    for snum in range(1,10,2):
        #Sum of looping number odd and even numbers in same index
        sum = num + snum
        #printed formatted string sum (odd/even numbers)
        print(f"{num}+{snum}={sum}")