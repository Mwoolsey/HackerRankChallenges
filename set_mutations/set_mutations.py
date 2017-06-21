
if __name__ == "__main__":
    raw_input()
    main_set = set(map(int, raw_input().split()))
    n = int(raw_input())

for _ in range(n):
    cmd_input = raw_input().split()
    operation = cmd_input[0]
    new_set = set(map(int, raw_input().split()))

    if operation == 'intersection_update':
        main_set.intersection_update(new_set)
    elif operation == 'update':
        main_set.update(new_set)
    elif operation == 'symmetric_difference_update':
        main_set.symmetric_difference_update(new_set)
    elif operation == 'difference_update':
        main_set.difference_update(new_set)
print sum(main_set)
