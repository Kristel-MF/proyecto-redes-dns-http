from collections import defaultdict
import time

requests_by_ip = defaultdict(list)

THRESHOLD = 5
TIME_WINDOW = 10


def register_request(ip, domain):
    current_time = time.time()

    requests_by_ip[ip].append(current_time)

    requests_by_ip[ip] = [
        t for t in requests_by_ip[ip]
        if current_time - t <= TIME_WINDOW
    ]

    total_requests = len(requests_by_ip[ip])

    if total_requests > THRESHOLD:
        print("\n[ALERTA]")
        print("Posible DNS Amplification Attack / DNS Flood")
        print(f"IP sospechosa: {ip}")
        print(f"Dominio consultado: {domain}")
        print(f"Consultas en los últimos {TIME_WINDOW} segundos: {total_requests}")