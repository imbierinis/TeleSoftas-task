
# for loop misses first element of a list, because list elements starts to count from 0, not from 1
# fixed version:
def print_list(a_list):
    for i in range(0, len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))

a_list = [1, 2, 3, 5, 7, 9]
print_list(a_list)
