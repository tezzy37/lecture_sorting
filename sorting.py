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

def selection_sort(numbers1, direction):
    while numbers1.sort():
        for idx in range(len(numbers1)-1):
            if numbers1[idx] > numbers1[idx+1]:
                numbers1[idx], numbers1[idx+1] = numbers1[idx+1], numbers1[idx]
            else:
                continue
    if direction == "sestupne":
        numbers1 = numbers1[::-1]
    elif direction == "vzestupne":
        pass

    print(numbers1)


def main():
    numbers = read_data("numbers.csv")
    print(numbers)
    numbers1 = numbers['series_1']
    serazene = selection_sort(numbers1, "vzestupne")

if __name__ == '__main__':
    main()
