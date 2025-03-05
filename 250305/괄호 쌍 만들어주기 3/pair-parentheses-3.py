A = input()
L = len(A)

cnt = 0
for i in range(L):
    for j in range(i + 1, L):
        if A[i] == '(' and A[j] == ')':
            cnt += 1

print(cnt)