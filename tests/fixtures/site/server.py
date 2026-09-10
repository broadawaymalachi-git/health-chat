import http.server, socketserver, json, os
PRODUCTS = {"products":[
 {"Name":"Test Disposable 1g","brand":{"name":"Fake Co"},"type":"Vaporizers",
  "Options":["1g"],"Prices":[40],"recSpecialPrices":[24]},
 {"Name":"Test Cart 0.5g","brand":{"name":"Fake Co"},"type":"Vaporizers",
  "Options":["0.5g"],"Prices":[30]}]}
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/menu/products"):
            b = json.dumps(PRODUCTS).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers(); self.wfile.write(b); return
        return super().do_GET()
    def log_message(self, *a): pass
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer(("127.0.0.1", 8901), H).serve_forever()
