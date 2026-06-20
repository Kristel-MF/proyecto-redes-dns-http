import socket
import time

HOST = "0.0.0.0"
PORT = 8080

requests_404 = {}
WINDOW_SECONDS = 10
THRESHOLD_404 = 5


def register_404(ip, uri):
    now = time.time()

    if ip not in requests_404:
        requests_404[ip] = []

    requests_404[ip].append((now, uri))

    requests_404[ip] = [
        item for item in requests_404[ip]
        if now - item[0] <= WINDOW_SECONDS
    ]

    if len(requests_404[ip]) >= THRESHOLD_404:
        print("\n[ALERTA HTTP]")
        print("Posible escaneo web detectado")
        print(f"IP sospechosa: {ip}")
        print(f"Solicitudes 404 recientes: {len(requests_404[ip])}")
        print("Rutas solicitadas:")
        for _, route in requests_404[ip]:
            print(f" - {route}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor HTTP escuchando en puerto {PORT}...")

while True:
    client_socket, client_address = server.accept()
    ip_cliente = client_address[0]

    request = client_socket.recv(1024).decode("utf-8", errors="ignore")

    print("\n===== PETICIÓN HTTP =====")
    print(request)

    first_line = request.split("\r\n")[0]
    parts = first_line.split()

    if len(parts) >= 3:
        method = parts[0]
        uri = parts[1]
        version = parts[2]

        print(f"Método: {method}")
        print(f"URI: {uri}")
        print(f"Versión: {version}")

        if method == "GET" and uri == "/":
            body = "<html><body><h1>Servidor HTTP propio funcionando</h1></body></html>"
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
        else:
            register_404(ip_cliente, uri)

            body = "<html><body><h1>404 Not Found</h1></body></html>"
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
    else:
        body = "Bad Request"
        response = (
            "HTTP/1.1 400 Bad Request\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        )

    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()