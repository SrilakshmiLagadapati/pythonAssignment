"""
Check if all digits of a number divide it
Given a number n, find whether all digits of n divide it or not.
Examples: 
Input : 128
Output : Yes
128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Input : 130
Output : No
"""
n = input()
l = len(n)
result_list = []
for char in n:
    if char == "0":
        pass
    else:
        if int(n)%int(char) == 0:
            result_list.append(char)
if l == len(result_list):
    print("Yes")
else:
    print("No")