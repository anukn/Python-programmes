User_input= input(print("Please enter the numbers you wish to sort with space between each number:"))

listA = User_input.split()

mid = 0
list_left = list()
list_right = list()
list_a = list()

def merge(left, right, listA):

    list_a.append = list_left
    list_a.append = list_right

def mergesort(listA):
    if len(listA) < 2 :
        return listA

    mid = len(listA) // 2
    left = list()
    right = list()

    for i in range(mid-1):
        left[i] = listA[i]

    for i in range(mid):
        right[i-mid] = listA[i]


    mergesort(left)
    mergesort(right)

    merge(left,right,listA)


print(mergesort(listA))




