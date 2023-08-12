def find_max_min(lst):
    max_val = max(lst)
    min_val = min(lst)
    return max_val, min_val

num_list = [25, 10, 45, 3, 18]
max_value, min_value = find_max_min(num_list)
print("Maximum value:", max_value)
print("Minimum value:", min_value)