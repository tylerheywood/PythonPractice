final = []
list1 = [1,2,4]
list2 = [1,3,4]
l1_len = len(list1)
l2_len = len(list2)

# sort to resolve any input errors

list1.sort()
list2.sort()

if not list1:
    for num in list2:
        final.append(num)
        print("a")
elif not list2:
    for num in list1:
        final.append(num)
        print("b")
else:
    for i, num in enumerate(list1):
        if list1[i] <= list2[i]:
            final.append(num)
            print("c")
    for i, num in enumerate(list2):
        if list2[i] <= list1[i]:
            final.append(num)
            print("d")

    print(final)






