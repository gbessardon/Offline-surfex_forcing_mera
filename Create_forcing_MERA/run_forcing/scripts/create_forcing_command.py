from sys import argv
import os
def read_config(fn):
    text = open(fn,'r')
    rawtextlist=[t for t in text] #converts text to list for manipulation
    argstarts=[i for i,t in enumerate(rawtextlist) if t.startswith('~')] # defines where positional and optional args starts
    #### 1.read positional arguments
    positional_args=[t for i,t in enumerate(rawtextlist) if i>argstarts[0] and i<argstarts[1] and not t.startswith('#')] # get the positional arguments lines
    startime=[p.split('=')[1].strip() for p in positional_args if 'start' in p][0] # reads start time
    endtime=[p.split('=')[1].strip() for p in positional_args if 'end' in p][0] # reads end time
    areafn=[p.split('=')[1].strip() for p in positional_args if 'area' in p][0]#reads area file name 
    
    #### 2. read optional arguments
    optional_args=[t for i,t in enumerate(rawtextlist) if i>argstarts[1] and not t.startswith('#') and not t.startswith('\n')]
    optional_args_indices=[i for i,o in enumerate(optional_args) if not o.startswith('-') and len(o.split('=')[1].strip())>0]
    commandslist=[optional_args[oai-1].strip()+' '+optional_args[oai].split('=')[1].strip() for oai in optional_args_indices]
    optionsstr=','.join(commandslist).replace(',',' ')
    char='create_forcing'+' '+startime+' '+endtime+' '+areafn+' '+optionsstr
    return (char)
    
script=argv[0]
inputfile=argv[1]
cmd=read_config(inputfile)
print(cmd)
os.system(cmd)