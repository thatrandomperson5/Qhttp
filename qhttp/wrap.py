from .nim import qhttp
class ResponseWrapper:
    def __init__(self, obj):
        
        self.__dict__.update(obj.__dict__.copy())
        response = self.content
        self.default_content = response
        self.content = response
        if type(response) == str:
            self.content = response.encode()
            self.text = response
        else:
            self.text = response.decode('ISO-8859-1')

def get(url):
    out = qhttp.get(url)
    print(out.__dict__)
    return ResponseWrapper(out)
    