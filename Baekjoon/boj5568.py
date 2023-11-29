from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

nums = list(permutations(cards, k)) # cards에서 순서를 고려하여 중복 없이 k개를 뽑는다.
result = set()
for i in nums:
    temp = ''.join(i)
    result.add(int(temp))

print(len(result))