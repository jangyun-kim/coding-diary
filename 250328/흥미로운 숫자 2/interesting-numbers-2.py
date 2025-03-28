X, Y = map(int, input().split())

def is_interesting(num):
    num_str = str(num)
    freq = [0] * 10

    for ch in num_str:
        digit = int(ch)
        freq[digit] += 1

    unique_digits = 0
    counts = []

    for f in freq:
        if f > 0:
            unique_digits += 1
            counts.append(f)

    if unique_digits != 2:
        return False

    counts.sort()
    return counts[0] == 1 and counts[1] == len(num_str) - 1

def count_interesting_numbers(X, y):
    count = 0
    for num in range(X, Y + 1):
        if is_interesting(num):
            count += 1
    return count

print(count_interesting_numbers(X, Y))
