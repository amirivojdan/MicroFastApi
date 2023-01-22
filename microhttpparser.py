class MicroHttpParser:
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    @staticmethod
    def parse_request(stream):
        request = {}
        while True:
            line = stream.readline()
            
            line_splitted = line.split(b' ')
            print(line_splitted[0])
            break
            if not line or line == b'\r\n':
                break
        request