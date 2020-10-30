import os 

def create_user_file(userfn,Flength):
    fout = open (userfn,'w')
    fout.write('grib1:')
    fout.write('\n'+'     offset: 0')
    fout.write('\n'+'     file_inc: 3600')
    fout.write('\n'+'     fcint: '+str(int(Flength)*3600))
    fout.close()
    cwd=os.getcwd()
    ft = open (cwd+'/default_files/user_mera_default.yml','r')

    charlist=[l for l in ft]
    newlist=[]
    for c in charlist:
        if 'fcint:' in c:
            newlist.append('\n'+'     fcint: '+str(int(Flength)*3600))
        else: 
            newlist.append(c)
                         
    fout = open (userfn,'w')
    [fout.write(l) for l in newlist]
    fout.close()
    return