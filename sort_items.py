import csv
import os
import random

cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """

    f = open(file_name, "r", encoding="utf-8")
    subor = csv.reader(f, delimiter="\t")

    values = []
    for line in subor:
        for value in line:
            values.append(int(value))

    return values


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """

    f = open(file_name, "r", encoding="utf-8")
    subor = csv.reader(f, delimiter=",")

    values = []
    for index, line in enumerate(subor):
        if index == row_number:
            return line

def selection_sort(number_array):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """

    for i in range(len(number_array)):

        min_idx = i
        for j in range(i + 1, len(number_array)):
            if number_array[min_idx] > number_array[j]:  # iba zmena >/<
                min_idx = j

        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]

    return number_array


def bubble_sort(arr):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    hodnoty = read_row("numbers_one.csv")
    print(hodnoty)
    # Ukol: Selection Sort

    hodnoty2 = read_rows("numbers_two.csv",2)

    select_sorted = selection_sort(hodnoty2)
    print(select_sorted)
    bubble_sorted = bubble_sort(hodnoty)
    print(bubble_sorted)

    # Ukol: Selection Sort - se smerem razeni

    # Ukol: Bubble Sort

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()
