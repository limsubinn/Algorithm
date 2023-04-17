def mk_to_dec(mk):
    size = len(mk)
    k = 1
    if 'K' in mk:
        k = 5
    return 10 ** (size - 1) * k

def find_value(value):
    answer = ''
    for i in value:
        if not i:
            continue
        answer += str(mk_to_dec(i))
    return int(answer)

mk = input()

array = mk.split('K')
max_value = []
min_value = []

for i in range(len(array)-1):
    max_value.append(array[i] + 'K')
    min_value.append(array[i])
    min_value.append('K')

if 'K' in array[-1]:
    max_value.append(array[-1])
else: # 맨 끝값은 'K'가 붙어있지 않기 때문에 M을 분리해서 저장하는 것이 최댓값
    for i in array[-1]:
        max_value.append(i)
min_value.append(array[-1])

print(find_value(max_value))
print(find_value(min_value))