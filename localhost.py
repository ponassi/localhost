#Use to create local host
import http.server
import socketserver

PORT = 8081
ADDRESS = '127.0.0.1'

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
       ".js": "application/javascript",
})

print('Starting server...')
server_address = (ADDRESS, PORT)
httpd = socketserver.TCPServer(server_address, Handler)
print ("Serving at address", ADDRESS)
print ("Serving at port", PORT)
print('Server ready...')
link = '"http://'+str(ADDRESS)+':'+str(PORT)+'"'
print(link)
httpd.serve_forever()