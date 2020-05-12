import random

def binary_search(sorted_data, target, low_index, high_index):
    status = False

    while not low_index > high_index:
        mid_index = (low_index + high_index) // 2

        if target == sorted_data[mid_index]:
            status = True
            return (status, mid_index)
        elif target < sorted_data[mid_index]:
            low_index = low_index
            high_index = mid_index - 1
            continue
        elif target > sorted_data[mid_index]:
            low_index = mid_index + 1
            high_index = high_index
            continue

    return status
        

if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(10)]
    print(f'Data: {data}')
    
    sorted_data = sorted(data)
    print(f'Sorted data: {sorted_data}')

    target = int(input('What number would you like to find? '))
    found = binary_search(sorted_data, target, 0, len(sorted_data) - 1)

    print(found)
    