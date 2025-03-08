N = int(input())
str = input()

count_C = 0 # number of 'C' found
count_O = 0 # number of 'O' found
count_W = 0 # number of 'W' found

# Iterate through the string
for i in range(N):
    if str[i] == 'C': # found a 'C'
        count_C += 1
    elif str[i] == 'O': # only count 'O' if there's a previous 'C'
        count_O += count_C 
    elif str[i] == 'W': # only count 'W' if there's a previous 'O'
        count_W += count_O


print(count_W)