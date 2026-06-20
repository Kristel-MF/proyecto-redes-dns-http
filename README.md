# Proyecto Redes DNS y HTTP

## IF5000 – Redes y Comunicación de Datos

### Universidad de Costa Rica – Sede del Sur

### Integrantes

* Kristel Muñoz
* Joseph Hernández
* Emma torres

---

# Descripción

Este proyecto implementa un sistema de análisis de protocolos de la capa de aplicación TCP/IP mediante el desarrollo de dos módulos independientes:

* Servidor DNS personalizado.
* Servidor HTTP personalizado.

El objetivo es demostrar el funcionamiento interno de ambos protocolos mediante captura de tráfico real, procesamiento manual de mensajes y detección de anomalías características de la capa de aplicación.

---

# Tecnologías Utilizadas

* Python 3
* Sockets TCP y UDP
* Wireshark
* GitHub
* Visual Studio Code

---

# Estructura del Proyecto

```text
proyecto-redes-dns-http/
│
├── dns/
│   ├── dns_server.py
│   ├── dns_response.py
│   ├── parser_dns.py
│   ├── zone_reader.py
│   └── zone.txt
│
├── detector/
│   └── detector_dns.py
│
├── http/
│   └── http_server.py
│
├── pruebas/
│   ├── dns_query.py
│   ├── dns_attack_simulator.py
│   └── test_dns.py
│
├── capturas/
│
└── README.md
```

---

# Requisitos

* Python 3.10 o superior
* Wireshark
* Sistema operativo Windows o Linux

Verificar instalación:

```bash
python --version
```

---

# Ejecución del Servidor DNS

Abrir una terminal:

```bash
python dns/dns_server.py
```

Salida esperada:

```text
Servidor DNS escuchando en UDP 8053...
```

---

# Ejecución de Consultas DNS

Abrir una segunda terminal:

```bash
python pruebas/dns_query.py
```

El sistema enviará consultas a:

* google.com
* ucr.ac.cr
* proyecto.local

y recibirá respuestas generadas por el servidor DNS.

---

# Simulación de Ataque DNS

Con el servidor DNS ejecutándose:

```bash
python pruebas/dns_attack_simulator.py
```

El sistema genera múltiples consultas consecutivas para simular un DNS Flood / DNS Amplification Attack.

Salida esperada:

```text
[ALERTA]
Posible DNS Amplification Attack / DNS Flood
IP sospechosa: 127.0.0.1
```

---

# Ejecución del Servidor HTTP

Abrir una terminal:

```bash
python http/http_server.py
```

Salida esperada:

```text
Servidor HTTP escuchando en puerto 8080...
```

---

# Pruebas HTTP

Abrir en el navegador:

```text
http://localhost:8080/
```

Respuesta esperada:

```text
Servidor HTTP propio funcionando
```

---

# Simulación de Escaneo Web

Acceder a las siguientes rutas:

```text
http://localhost:8080/admin
http://localhost:8080/login
http://localhost:8080/wp-admin
http://localhost:8080/config
http://localhost:8080/phpmyadmin
```

El sistema generará respuestas:

```text
404 Not Found
```

y detectará actividad sospechosa.

Salida esperada:

```text
[ALERTA HTTP]
Posible escaneo web detectado
IP sospechosa: 127.0.0.1
```

---

# Validación con Wireshark

## DNS

Filtro:

```text
udp.port == 8053
```

## HTTP

Filtro:

```text
tcp.port == 8080
```

Las capturas obtenidas permiten validar el funcionamiento del sistema y comparar los mensajes procesados con los observados por Wireshark.

---

# Anomalías Implementadas

## DNS

* DNS Flood
* DNS Amplification Attack

## HTTP

* Escaneo de rutas web
* Múltiples respuestas 404 desde una misma dirección IP

---

# Resultados Obtenidos

* Implementación exitosa de un servidor DNS funcional.
* Implementación exitosa de un servidor HTTP funcional.
* Parsing manual de mensajes DNS.
* Parsing manual de peticiones HTTP.
* Detección automática de anomalías.
* Validación de resultados mediante Wireshark.

---

# Repositorio

Repositorio utilizado para el desarrollo del proyecto:

https://github.com/Kristel-MF/proyecto-redes-dns-http

---

# Asistencia de IA

Durante el desarrollo del proyecto se utilizó inteligencia artificial generativa como apoyo para:

* Revisión de código.
* Resolución de errores.
* Generación de documentación técnica.
* Elaboración de ejemplos de pruebas.
* Redacción del README y material de presentación.

Todo el código fue revisado, probado y adaptado por los integrantes del proyecto antes de su incorporación al sistema final.
