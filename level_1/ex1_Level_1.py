import csv
import os

output = './processed_data/output.csv'
if not os.path.isdir('./processed_data'):
    os.makedirs('./processed_data',exist_ok=True)
with open(output, mode="w+", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(['user_id','first_name','last_name','birthts','img_path'])
    for i in range(100):
        user_id = f'100{i}' if i< 10 else  f'10{i}'
        currentCsvFile = f'./02-src-data/100{i}.csv' if i < 10 else f'./02-src-data/10{i}.csv'
        currentPngFile = f'./02-src-data/100{i}.png' if i < 10 else f'./02-src-data/10{i}.png'

        if os.path.isfile(currentCsvFile) and os.path.exists(currentPngFile):
            with open(currentCsvFile, encoding='utf-8') as file:
                reader = list(csv.reader(file))
                file_writer.writerow([user_id, reader[1][0], reader[1][1], reader[1][2], currentPngFile])

            