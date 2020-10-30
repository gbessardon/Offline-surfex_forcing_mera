#Calls all other functions
import get_filepath as gf
import read_config_file as rcf
import datatreatment as dt
import sortfiles as sort
import write_userfile as wu
import write_config_file as wcf
import create_symlink as cs
from sys import argv

script=argv[0]
fn=argv[1]
#read config file
(startime,endtime,MERAdir,filenameout,dirout,Flength,Areafn,CFfn,forcingfn,userfn)=rcf.read_config(fn)
#Write user file
wu.create_user_file(userfn,Flength)
#list all the MERA files
filesave,datelist=gf.get_filepaths(MERAdir,Flength,startime,endtime)
# check numbers of files for each parameter
(indicatorofparamlist,heights,repeat,paramlist)=sort.sortfiles(filesave,MERAdir,startime,endtime)
# clear files before writting them
[sort.clear_files(f,dirout,filenameout,indicatorofparamlist,startime,endtime) for f in filesave]

# write config file for next step
wcf.write_offline_surfex_config_file(CFfn,startime,endtime,Areafn,forcingfn,dirout,filenameout,indicatorofparamlist,userfn,repeat)

### write the files
for f in filesave:
	dt.datatreatment3(f,dirout,filenameout,indicatorofparamlist,startime,endtime)
    
#### create symbolik link 
cs.threehourslink(startime,endtime,dirout,filenameout,Flength)