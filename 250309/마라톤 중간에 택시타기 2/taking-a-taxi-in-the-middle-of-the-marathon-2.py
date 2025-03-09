N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Taxi distance function
def taxi_distance(i, j):
    """Calculate taxi distance between checkpoint i and j using x, y lists."""
    return abs(x[i] - x[j]) + abs(y[i] - y[j])

# Compute the original full marathon distance
original_distance = sum(taxi_distance(i, i+1) for i in range(N-1))

# Initialize the minimum possible distance
min_distance = float('inf')

# Try skipping one checkpoint (except first and last)
for i in range(1, N-1):  # Exclude index 0 and N-1
    # Compute the distance when skipping checkpoint i
    new_distance = original_distance - taxi_distance(i-1, i) - taxi_distance(i, i+1) + taxi_distance(i-1, i+1)

    # Update minimum distance found
    min_distance = min(min_distance, new_distance)

# Output the result
print(min_distance)
