def insertion_sort_opt(ele):
    for i in range(1, len(ele)):
        anchor = ele[i]
        j = i - 1
        while j >= 0 and anchor < ele[j]:
            ele[j + 1] = ele[j]
            j = j - 1
        ele[j + 1] = anchor


#     Time complexity is 0(1)

if __name__ == '__main__':
    ele = [12, 34, 10, 5, 72, 65, 50]
    insertion_sort_opt(ele)
    print(f"Sorted list is : {ele}")