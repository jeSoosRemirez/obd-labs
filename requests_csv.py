import csv
import csv_structure as struct
import csv_interaction as interact


def get_m(provider_code: str):
    data_ind = interact.read_csv(struct.providers_ind_filename)
    provider_ind = [ind for ind in data_ind if provider_code == ind[0]][0][1]

    data_providers = interact.read_csv(struct.providers_filename)
    provider = [prov for prov in data_providers if provider_ind == prov[0]]

    return provider


def get_s(provider_code: str):
    data_ind = interact.read_csv(struct.deliveries_ind_filename)
    delivery_code = [deliv for deliv in data_ind if provider_code == deliv[0]][0][1]

    data_deliveries = interact.read_csv(struct.deliveries_filename)

    delivery_code = list(delivery_code.split(", "))
    if len(delivery_code) > 1:
        deliveries = [
            deliv for deliv in data_deliveries
            for deliv_code in delivery_code
            if provider_code in deliv and deliv_code in deliv
        ]

    else:
        deliveries = [deliv for deliv in data_deliveries if provider_code in deliv and delivery_code[0] in deliv]

    return deliveries


def del_m(provider_code: str):
    filenames = [struct.deliveries_filename, struct.deliveries_ind_filename]
    for filename in filenames:
        lines = list()
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == provider_code:
                        lines.remove(row)
        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    return f"{provider_code} has been deleted from deliveries.csv and deliveries_ind.csv"


def del_s(provider_code: str):
    filenames = [struct.providers_ind_filename, struct.providers_filename]

    for filename in filenames:
        lines = list()
        if filename == struct.providers_filename:
            provider_code = provider_id
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == provider_code:
                        provider_id = row[1]
                        lines.remove(row)
        with open(filename, 'w') as writeFile:
            if filename == struct.providers_filename:
                new_id = 0
                for el in lines[1:]:
                    el[0] = str(new_id)
                    new_id += 1
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    return f"{provider_code} has been deleted from providers.csv and providers_ind.csv"


def update_m(provider_code: str, to_change: list):
    provider = get_m(provider_code)[0]
    filename = struct.providers_filename
    to_change.insert(0, get_m(provider_code)[0][0])

    if len(to_change) > len(provider):
        return "You have provided too many values to change(mb delete id)"

    lines = list()
    with open(filename, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row == provider:
                lines.append(to_change)
            else:
                lines.append(row)
    with open(filename, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    return to_change


def update_s(delivery_code: str, to_change: list):
    filename = struct.deliveries_filename
    to_change.insert(0, delivery_code)

    if len(to_change) > 3:
        return "You have provided too many values to change(mb delete id)"

    lines = list()
    with open(filename, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if delivery_code in row:
                to_change.insert(0, row[0])
                lines.append(to_change)
            else:
                lines.append(row)
    with open(filename, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    return to_change


# [provider_ind, surname, status, city]
def insert_m(data: list):
    if len(data) <= 1:
        data.append(["", "", ""])
    elif len(data) == 0 or data is None:
        return "No variables was provided to insert"

    filenames = [struct.providers_filename, struct.providers_ind_filename]
    provider_ind = data.pop(0)
    for filename in filenames:
        lines = list()
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if provider_ind in row:
                    return f"Provider '{data[0]}' already exist"
                lines.append(row)
            provider_id = len(lines)
            if filename == struct.providers_ind_filename:
                data = [provider_ind, provider_id]
            else:
                data.insert(0, provider_id)
            lines.append(data)
        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    return f"{data} has been added to providers.csv and providers_ind.csv"


def insert_s(data: list):
    if len(data) <= 2:
        data.append(["", ""])
    elif len(data) == 0 or data is None:
        return "No variables was provided to insert"

    filenames = [struct.deliveries_filename, struct.deliveries_ind_filename]
    provider_ind = data[0]
    delivery_ind = data[1]
    ind_is_in = False
    for filename in filenames:
        lines = list()
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if filename == struct.deliveries_ind_filename and provider_ind in row:
                    ind_is_in = True
                    row[1] = row[1] + ", " + delivery_ind
                    lines.append(row)
                else:
                    lines.append(row)

            if filename != struct.deliveries_ind_filename:
                lines.append(data)
            if not ind_is_in and filename == struct.deliveries_ind_filename:
                to_add = [provider_ind, delivery_ind]
                lines.append(to_add)
        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    return f"{data} has been added to deliveries.csv and deliveries_ind.csv"
