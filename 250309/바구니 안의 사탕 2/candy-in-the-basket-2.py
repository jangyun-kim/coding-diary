N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Sort baskets by position (while keeping candies aligned)
sorted_baskets = sorted(zip(pos, candy))  # Sort tuples by position
pos = [p for p, _ in sorted_baskets]  # Extract sorted positions
candy = [c for _, c in sorted_baskets]  # Extract corresponding candy counts

# Sliding window approach
max_candies = 0  # Maximum candies collected
current_candies = 0  # Sum of candies in the current window
left = 0  # Left boundary of the window

# Iterate through baskets using a sliding window
for right in range(N):
    # Expand the window by adding the new basket's candy count
    current_candies += candy[right]

    # Shrink the window if the range exceeds [c-K, c+K]
    while pos[right] - pos[left] > 2 * K:
        current_candies -= candy[left]  # Remove candies from the leftmost basket
        left += 1  # Move the left boundary forward

    # Update the maximum candies collected
    max_candies = max(max_candies, current_candies)

# Output the maximum candies found
print(max_candies)