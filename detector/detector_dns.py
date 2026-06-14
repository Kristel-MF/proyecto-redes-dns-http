from collections import defaultdict
import time

requests = defaultdict(list)


def register_request(ip):

    current_time = time.time()

    requests[ip].append(current_time)

    requests[ip] = [
        t for t in requests[ip]
        if current_time - t < 10
    ]

    if len(requests[ip]) > 5:

        print("\n[ALERTA]")
        print("Posible DNS Amplification Attack")
        print(f"IP sospechosa: {ip}")
        print(f"Consultas recientes: {len(requests[ip])}")