setA = set(map(int, raw_input().split()))

superset = False

for _ in range(int(raw_input())):
    setB = set(map(int, raw_input().split()))
    if setA >= setB :
        superset = True
    else:
        superset = False
        break

print superset
