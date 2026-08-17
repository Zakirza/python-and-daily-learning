import ssl
import socket

HOST = "taxinformation.cbic.gov.in"
PORT = 443

ctx = ssl._create_unverified_context()

with socket.create_connection((HOST, PORT), timeout=10) as sock:
    with ctx.wrap_socket(sock, server_hostname=HOST) as ssock:
        der_cert = ssock.getpeercert(binary_form=True)
        pem_cert = ssl.DER_cert_to_PEM_cert(der_cert)

        with open("cbic_cert.pem", "w") as f:
            f.write(pem_cert)

        print("Saved certificate to cbic_cert.pem\n")

        decoded = ssl._ssl._test_decode_cert("cbic_cert.pem")
        print("Issuer:   ", decoded.get("issuer"))
        print("Subject:  ", decoded.get("subject"))
        print("Not After:", decoded.get("notAfter"))