import csv


def write_csv(filename, fields, rows):

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    return "Done"


def read_csv(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        rows = [row for row in csvreader]

    return rows

# write_csv(providers_filename, providers_fields, providers_rows)
# write_csv(providers_ind_filename, providers_ind_fields, providers_ind_rows)
# write_csv(deliveries_filename, deliveries_fields, deliveries_rows)
# write_csv(deliveries_ind_filename, deliveries_ind_fields, deliveries_ind_rows)
