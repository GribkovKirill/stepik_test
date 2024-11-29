class SomeIterator:                             
    def __init__(self, **args, **kwargs):
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self): 
        somebody = ''
        return somebody