import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile="public.pem",keyfile="private.pem") ###############

bindsocket = socket.socket()
bindsocket.bind(('', 8080))
bindsocket.listen(5)

while True:
    try:
        newsocket, fromaddr = bindsocket.accept()
        sslsoc = context.wrap_socket(newsocket, server_side=True)
        request = sslsoc.read()
        print(request)
    except:
        print("ERROR")
