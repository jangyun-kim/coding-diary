N = int(input())
A, B, C = [], [], []
for _ in range(N):
    num, cnt1, cnt2 = map(int, input().split())
    A.append(str(num))
    B.append(cnt1)
    C.append(cnt2)

valid_count = 0 # count all valid cases

for a in range(1, 10):
    for b in range(1, 10):
        if b == a:
            continue

        for c in range(1, 10):
            if c == a and c == b:
                continue
            
            candidate = f"{a}{b}{c}"
            is_valid = True

            for i in range(N):
                B_guess = A[i] # B inputs three digit num
                expected_cnt1 = B[i] # strike number
                expected_cnt2 = C[i] # ball number

                # calculate actual strikes and balls count
                cnt1 = sum(candidate[j] == B_guess[j] for j in range(3))
                common_digits = set(candidate) & set(B_guess)
                cnt2 = len(common_digits) - cnt1

                # except from candidate if they don't satisfy the conditions
                if cnt1 != expected_cnt1 or cnt2 != expected_cnt2:
                    is_valid = False
                    break # no more check

            if is_valid:
                valid_count += 1
                print(candidate)

            

print(valid_count)