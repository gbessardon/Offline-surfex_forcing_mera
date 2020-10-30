import os
import numpy as np
def write_offline_surfex_config_file(CFfn,startime,endtime,arean,forcingfn,dirout,filenameout,indicatorofparamlist,userfn,repeat):
    # MERA input format is always grib so no need to change the Xinputformat options
    header=("#Temperature/humidity reference height --zref and winds reference height --uref set as screen"            "\n"+"#means 2-m Temperature/humidity and 10-m wind speed other option ml does not work with the"            "\n"+"#offline-surfex-forcing version tested"            "\n"+"#co2 constant as not in MERA files 0.00062"            "\n"+"#Options regarding the field contained in the MERA file:\n" )


    Zs=0
    ws=0
    wd=0
    qa=0
    ta=0
    ps=0
    dir_sw=0
    sca_sw=0
    LW=0
    rainf=0
    snowf=0 
    cwd=os.getcwd()
    ft = open (cwd+'/default_files/config_offline_surfex_mera_default','r')
    charlist=[l for l in ft]
    newlist=[]
    ft.close()
    for f in charlist:
        if f.startswith('start_time'): 
            newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],startime.replace('/',''))+'\n')
        elif f.startswith('end_time'):
            newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],endtime.replace('/',''))+'\n')
        elif f.startswith('area_file'):
            newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],arean+'\n'))
        #elif f.startswith('area_mode'):
        #    if arean.endswith('.yml'):
        #        newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'conf_proj_domain\n'))
        #    else:
        #        newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'file\n'))
        elif f.startswith('input_forcing_file_pattern'):
            pattern=dirout+'/'+filenameout+'@YYYY@@MM@@DD@_@HH@+@LL@'+'.grb'
            newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],pattern+'\n'))
        elif f.startswith('outputfn'):
            newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],forcingfn+'\n'))
        elif f.startswith('config_file'):
            newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],userfn+'\n'))
        #surface pressure converter
        elif f.startswith('Pconverter'):
            if ('1' in indicatorofparamlist and repeat[np.where('1'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                ps=ps+1
        #Short wave radiation converter
        elif f.startswith('DSWconverter'):
            if ('116' in indicatorofparamlist and repeat[np.where('116'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                dir_sw=dir_sw+1
        #Scattered shortwave radiation
        elif f.startswith('SCA_SWconverter'):
            if ('116' in indicatorofparamlist and repeat[np.where('116'==np.array(indicatorofparamlist))[0]]==1
		and '117' in indicatorofparamlist and repeat[np.where('117'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                sca_sw=sca_sw+1
        #long wave radiation converter
        elif f.startswith('LWconverter'):
            if ('115' in indicatorofparamlist and repeat[np.where('115'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                LW=LW+1
        #Rain fall options
        elif f.startswith('Rainconverter'):
            if ('221' in indicatorofparamlist and repeat[np.where('221'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                rainf=rainf+1
            if ('61' in indicatorofparamlist and repeat[np.where('61'==np.array(indicatorofparamlist))[0]]==1
                and '184' in indicatorofparamlist and repeat[np.where('184'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'totalprec\n'))
                rainf=rainf+1
        #Snow direction options
        elif f.startswith('Snowconverter'):
            if ('185' in indicatorofparamlist and repeat[np.where('185'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                snowf=snowf+1           
        #wind speed options   
        elif f.startswith('Windconverter'):
            if ('33' in indicatorofparamlist and repeat[np.where('33'==np.array(indicatorofparamlist))[0]]==1 
                and '34' in indicatorofparamlist and repeat[np.where('34'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'windspeed\n'))
                ws=ws+1
            if ('31' in indicatorofparamlist and repeat[np.where('31'==np.array(indicatorofparamlist))[0]]==1
                and '32' in indicatorparamlist and repeat[np.where('32'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'windspeed\n'))
                ws=ws+1
        #wind direction options
        elif f.startswith('Winddirconverter'):
            if ('33' in indicatorofparamlist and repeat[np.where('33'==np.array(indicatorofparamlist))[0]]==1
                and '34' in indicatorofparamlist and repeat[np.where('34'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'winddir\n'))
                wd=wd+1
            if ('31' in indicatorofparamlist and repeat[np.where('31'==np.array(indicatorofparamlist))[0]]==1
                and '32' in indicatorofparamlist and repeat[np.where('32'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'winddir\n'))
                wd=wd+1
        #orography options
        #elif f.startswith('ZSconverter'):
         #   if ('8' in indicatorofparamlist and repeat[np.where('8'==np.array(indicatorofparamlist))[0]]==1):
          #      newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'phi2m\n'))
           #     Zs=Zs+1
                
         #temperature options
        elif f.startswith('TAconverter'):
            if ('11' in indicatorofparamlist and repeat[np.where('11'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                ta=ta+1
        #temperature options
        elif f.startswith('Qconverter'):
            if ('51' in indicatorofparamlist and repeat[np.where('51'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'none\n'))
                qa=qa+1
            if ('52' in indicatorofparamlist and repeat[np.where('52'==np.array(indicatorofparamlist))[0]]==1
                and '11' in indicatorofparamlist and repeat[np.where('11'==np.array(indicatorofparamlist))[0]]==1
                and '1' in indicatorofparamlist and repeat[np.where('1'==np.array(indicatorofparamlist))[0]]==1):
                newlist.append(f.split('=')[0]+'='+f.split('=')[1].replace(f.split('=')[1],'rh2q\n'))
                qa=qa+1
        else:
            newlist.append(f)

       
    
    header2=("#"+str(Zs)+ "Orography options available"         +"#"+str(ws)+" wind speed options available"+"\n"+ "#"+str(wd)+" wind directions available"+         "\n"+"#" +str(qa)+" Specific humidity options available"         "\n"+"#" +str(ta)+" temperature options available"+"\n"+"#"+ str(ps)+" surface pressure options available"+"\n"+         "\n"+"#" +str(dir_sw)+" direct shortwave options available"+"\n"+"#"+ str(sca_sw)+ " scattered shortwave options available"+         "\n"+"#" +str(LW)+" longwave radiation options available"+"\n"+"#"+ str(rainf)+ " rainfall options available"+         "#" +str(snowf)+" snowfall option available"+"\n")
    
    fout = open (CFfn,'w') #creates the output file
    fout.write(header) #writes the first header
    fout.write(header2) #writes the second headers
    for l in newlist:
        fout.write(l) #writes the main part of the file
    fout.close() #savesthe output file             
    return