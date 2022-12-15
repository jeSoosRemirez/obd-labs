import csv

# providers.csv, providers_ind.csv
# S.fl
providers_fields = ["provider_id", "surname", "status", "city"]
providers_rows = [
    ["0", "Khomych", "ON", "Kyiv"],
    ["1", "Petrenko", "OFF", "Lviv"],
    ["2", "Duda", "ON", "Wroclaw"]
]
providers_filename = "providers.csv"

# S.ind
providers_ind_fields = ["provider_code", "provider_id"]
providers_ind_rows = [
    ["012", "0"],
    ["123", "1"],
    ["234", "2"]
]
providers_ind_filename = "providers_ind.csv"


# deliveries.csv, deliveries_ind.csv
# SP.fl
deliveries_fields = ["provider_code", "delivery_code", "price", "count"]
deliveries_rows = [
    ["012", "123456", "200", "1"],
    ["012", "234567", "400", "2"],
    ["123", "456654", "200", "1"],
    ["234", "654321", "1000", "10"]
]
deliveries_filename = "deliveries.csv"

# SP.ind
deliveries_ind_fields = ["provider_code", "delivery_code"]
deliveries_ind_rows = [
    ["012", "123456, 234567"],
    ["123", "123456"],
    ["234", "654321"]
]
deliveries_ind_filename = "deliveries_ind.csv"


def write_csv(filename, fields, rows):

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    return "Done"


write_csv(providers_filename, providers_fields, providers_rows)
write_csv(providers_ind_filename, providers_ind_fields, providers_ind_rows)
write_csv(deliveries_filename, deliveries_fields, deliveries_rows)
write_csv(deliveries_ind_filename, deliveries_ind_fields, deliveries_ind_rows)
