import csv

dictionary = {}
with open("data.csv", "r") as data:
    csv_reader = csv.reader(data)
    for line in csv_reader:
        if not line:
            pass
        else:
            dictionary[line[0]] = int(line[1])

final_dict = {key: value for key, value in sorted(
    dictionary.items(), key=lambda item: item[1], reverse=True)}

print(final_dict)

with open("final_data.csv", "a", newline='') as data:
    writer = csv.writer(data)
    for key, value in final_dict.items():
        writer.writerow([key, value])
