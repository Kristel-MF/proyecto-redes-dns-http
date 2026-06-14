def load_zone():

    records = {}

    with open("dns/zone.txt", "r") as file:

        for line in file:

            line = line.strip()

            if "=" not in line:
                continue

            domain, ip = line.split("=")

            records[domain.strip()] = ip.strip()

    return records