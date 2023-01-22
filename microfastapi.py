import functools #pip install micropython-functools
import _thread
import time
import socket
import json
from microhttpparser import MicroHttpParser

class MicroFastApi:
    
    def __init__(self, ip, port,  mac):
        self.routes = {}
        self.ipaddress = ip
        self.port = port
        self.mac = mac
        
        #self.lock = _thread.allocate_lock()
        
        addr = socket.getaddrinfo("0.0.0.0", self.port)[0][-1]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.socket.bind(addr)
        self.socket.listen(1) # server concurrent connections capacity 
        
        #self.thread = _thread.start_new_thread(self._http_handler,())
        print(self)
       
    def __str__(self):
        server_info = f"""API server running on http://{self.ipaddress}:{self.port}"""
        return server_info
    
    def get(self,route:str):
        def decorate_get_api(func):
            @functools.wraps(func)
            def decorated_get_func(*args, **kwargs):
                # pre-processing 
                ret_val = func(*args, **kwargs)
                # post-processing 
                return json.dumps(ret_val)
            #with self.lock:
            self.routes[route] = decorated_get_func
            return decorated_get_func
        return decorate_get_api
    
    def Run(self):
        self._http_handler()
        
    def _http_handler(self):
        while True:
            try:
                client_socket, client_addr = self.socket.accept()
                client_stream = client_socket.makefile('rwb', 0)
                #MicroHttpParser.parse_request(client_stream)
                print('client connected from', client_addr)
                testjson = {'userId':'1'}
                response = json.dumps(testjson)
                client_socket.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
                client_socket.send(response)
                client_socket.close()
                print("client closed!")
            except OSError as e:
                print(e)
                
            #with self.lock: # acquire the lock and release it when done.
                #for route in self.routes:
                    #print(f"route {route} is mapped to {self.routes[route].__name__}. result:"+ self.routes[route]())
 
            
            
           
        
        

