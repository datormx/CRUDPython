import random

def binary_search(sorted_data, target, low_index, high_index):
    if low_index > high_index:
        return False
    
    mid_index = (low_index + high_index) // 2

    if target == sorted_data[mid_index]:
        return (True, mid_index)
    elif target < sorted_data[mid_index]:
        return binary_search(sorted_data, target, low_index, mid_index - 1)
    elif target > sorted_data[mid_index]:
        return binary_search(sorted_data, target, mid_index + 1, high_index)


if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(10)]
    print(f'Data: {data}')
    
    sorted_data = sorted(data)
    print(f'Sorted data: {sorted_data}')

    target = int(input('What number would you like to find? '))
    found = binary_search(sorted_data, target, 0, len(sorted_data) - 1)

    print(found)
    