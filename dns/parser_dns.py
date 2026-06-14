import struct

def parse_dns_header(data):

    if len(data) < 12:
        print("Paquete demasiado pequeño para DNS")
        return

    transaction_id, flags, qdcount, ancount, nscount, arcount = struct.unpack(
        "!HHHHHH",
        data[:12]
    )

    print("\n===== DNS HEADER =====")
    print(f"Transaction ID : {hex(transaction_id)}")
    print(f"Flags          : {hex(flags)}")
    print(f"Questions      : {qdcount}")
    print(f"Answers        : {ancount}")
    print(f"Authority RR   : {nscount}")
    print(f"Additional RR  : {arcount}")

    return parse_domain_name(data)


def parse_domain_name(data):

    offset = 12
    domain_parts = []

    length = data[offset]

    while length != 0:

        offset += 1

        label = data[offset:offset + length].decode()

        domain_parts.append(label)

        offset += length

        length = data[offset]

    domain = ".".join(domain_parts)

    print(f"\nDominio solicitado: {domain}")

    return domain