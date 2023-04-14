def concatenate_args(*strings):
    concat = ""
    for str in strings:
        concat+=str
    return concat 
  

def concatenate_kwargs(**string):
     dict = ""
     for key,value in string.items():
         dict+=(f"{key}{value}")
     return dict     