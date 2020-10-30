def read_config(fn):
    text = open(fn,'r')
    rawtextlist=[t for t in text] #converts text to list for manipulation
    argstarts=[i for i,t in enumerate(rawtextlist) if t.startswith('~')] # defines where positional and optional args starts
    #### 1.read positional arguments
    positional_args=[t for i,t in enumerate(rawtextlist) if i>argstarts[0] and i<argstarts[1] and not t.startswith('#')] # get the positional arguments lines
    startime=[p.split('=')[1].strip() for p in positional_args if 'start' in p][0] # reads start time
    endtime=[p.split('=')[1].strip() for p in positional_args if 'end' in p][0] # reads end time
    dirout=[p.split('=')[1].strip() for p in positional_args if 'savedata' in p][0] # reads output directory name
    filenameout=[p.split('=')[1].strip() for p in positional_args if 'filename' in p][0] # reads output filename header
    MERAdir=[p.split('=')[1].strip() for p in positional_args if 'MERA' in p][0] # reads MERA directory
    Flength=[p.split('=')[1].strip() for p in positional_args if 'Forecast' in p][0] # reads Forecast length
    Areafn=[p.split('=')[1].strip() for p in positional_args if 'Areafn' in p][0] # reads Area filename
    CFfn=[p.split('=')[1].strip() for p in positional_args if 'CFfn' in p][0] # reads output config filename
    forcingfn=[p.split('=')[1].strip() for p in positional_args if 'forcingfn' in p][0] # reads output forcing filename 
    userfn=[p.split('=')[1].strip() for p in positional_args if 'Userfn' in p][0] # reads user filename input to offline-surfex-forcing
    #### 2. read optional arguments
    #### Open to modifications later
    return (startime,endtime,MERAdir,filenameout,dirout,Flength,Areafn,CFfn,forcingfn,userfn)