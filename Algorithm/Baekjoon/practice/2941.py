s = input()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alphabet:
        s = s.replace(i, "a")

print(len(s))