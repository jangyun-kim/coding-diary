A = input()
L = len(A)

left_cnt = 0  # Count of '((' found so far
pair_cnt = 0  # Total valid '((' and '))' pairs

# Iterate through the string and count valid pairs
for i in range(L - 1):  # Ensure `A[i+1]` is in range
    if A[i] == '(' and A[i + 1] == '(':  
        left_cnt += 1  # Found a '((' pair
    elif A[i] == ')' and A[i + 1] == ')':
        pair_cnt += left_cnt  # Each '))' can pair with all previous '(('

print(pair_cnt)