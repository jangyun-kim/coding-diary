N = int(input())
blocks = [int(input()) for _ in range(N)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# remove first block
remaining_blocks = blocks[:s1-1] + blocks[e1:]  # remove range s1~e1

# remove second block
remaining_blocks = remaining_blocks[:s2-1] + remaining_blocks[e2:]  # remove range s2~e2

# print the number of leaved blocks
print(len(remaining_blocks))

# print leaved blocks in order from the top
for block in remaining_blocks:
    print(block)
