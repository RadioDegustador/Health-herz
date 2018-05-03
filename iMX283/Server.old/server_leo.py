from http.server import HTTPServer, BaseHTTPRequestHandler
#Librerias solo disponibles en python3

HOST = 5050	#Puerto en el que estara el servidor

class HttpHandler(BaseHTTPRequestHandler):


	def do_GET(self):
		self.send_response(200)
		#Ahora se envian las cabeceras (estas son informacion del tipo de dato)
		self.send_header('Content-type', 'text/HTML; charset=utf-8')
		self.end_headers()

		#Imprimo un fichero html que ya se tiene
		message = open("formulario.html").read().encode()
		image = open("imagen.png")
		self.wfile.write(message)


if __name__ == "__main__":
	server_address = ('', HOST) 				#Se declara la direccion del servidor
	httpd = HTTPServer(server_address, HttpHandler)		#Se declara el servidor
	print('Servidor abierto en el puerto: ');
	print(HOST);
	httpd.serve_forever()					#Se deja funcionando por siempre
