import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as csv_file:
        reader = csv.DictReader(csv_file) #přečte ve formě slovníku #klíč je hlavička toho sloupce(series_1,2,3)
        #data = {"series_1": [], "series_2": [], "series_3": []}
        data = {} #podminka if key not in...
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
    return data

def selection_sort(numbers, direction):
    for i in range(len(numbers)):
        min_idx = i
        for num_idx in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[num_idx]:
                min_idx = num_idx
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    if direction == "sestupne":
        numbers1 = numbers[::-1]
    elif direction == "vzestupne":
        pass
    return numbers
def bubble_sort(numbers):
    while numbers.sort():
        for idx in range(len(numbers)-1):
            if numbers[idx] > numbers[idx+1]:
                numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
            else:
                continue
    return numbers

def main():
    numbers = read_data("numbers.csv")
    bublina = bubble_sort(numbers['series_1'])
    selekce = selection_sort(numbers['series_1'], "vzestupne")
    print(selekce)

if __name__ == '__main__':
    main()
