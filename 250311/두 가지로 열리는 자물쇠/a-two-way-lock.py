N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# the function of the calculating circlar diestance 
def is_within_range(x, target):
    return (abs(x - target) <= 2) or (abs(x - target) >= N - 2)

valid_combinations = set()

# the set of storing the number of combination of possible
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            first_valid = (is_within_range(x, a1) and is_within_range(y, b1) and is_within_range(z, c1))

            second_valid = (is_within_range(x, a2) and is_within_range(y, b2) and is_within_range(z, c2))

            if first_valid or second_valid:
                valid_combinations.add((x, y, z))

print(len(valid_combinations))