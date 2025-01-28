import array as arr

def print_array(array, message):
    print(message, end = " ")
    for item in array:
        print(item, end =" ")
    print()

int_arr = arr.array('i', [1, 2, 3])

print("elements in array : ", end = " ")
for i in range(0, len(int_arr)):
    print(int_arr[i], end = " ")
print()

# 1 의 위치에 4의 값을 추가
int_arr.insert(1, 4)
print_array(int_arr, "elements after insertion : ")

# 1 의 위치 값을 삭제
int_arr.remove(1)
print_array(int_arr, "elements after delete \'1\' in array : ")

# 1 의 위치 값을 변경
int_arr[1] = 100
print_array(int_arr, "elements after update \'1\' in array : ")