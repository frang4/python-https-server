from http import server
import ssl

httpd = server.HTTPServer(('0.0.0.0', 443), server.SimpleHTTPRequestHandler)

sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='./server.crt', keyfile='./server.key')

httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
