import csv
import argparse


def process_csv(directory):
    with open(str(fileDirectory)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('parsed_products.csv', mode='w', newline='') as products:
            csv_writer = csv.writer(
                products,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            categoryIndex = ""
            for i, row in enumerate(csv_reader):
                if i == 0:
                    print(f'Column names are {", ".join(row)}')
                    categoryIndex = row.index("Categories")
                    csv_writer.writerow(row)

                else:
                    if (row[categoryIndex]):
                        csv_writer.writerow(row)
                        print(row, "\n")


parser = argparse.ArgumentParser(description='Parses product lists.')
parser.add_argument('file', metavar='file', nargs='+',
                    help='product.csv file location')

args = parser.parse_args()
if (len(args.file) == 1):
    fileDirectory = args.file[0]
    print(fileDirectory)
    process_csv(fileDirectory)
else:
    print("invalid arguments")
