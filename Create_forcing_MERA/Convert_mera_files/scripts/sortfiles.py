import numpy as np
import os
import pygrib
from matplotlib import dates
import datetime
from dateutil.rrule import rrule, MONTHLY
# ## removes parameter number duplicates in sortfiles


def remove_duplicates(test_list):
    res=[]
    ind=[]
    for i,t in enumerate(test_list): 
        if t not in res: 
            res.append(t)
            ind.append(i)
    return ind,res  


# ## counts duplicates  to check variable is present for every month of the study



def count_duplicates(singlelist,totallist,styear,stmonth,stday,sthour,endyear,endmonth,endday,endhour):
    strt_dt = datetime.datetime(styear,stmonth,stday,sthour)
    end_dt = datetime.datetime(endyear,endmonth,endday,endhour)
    dates = [dt for dt in rrule(MONTHLY, dtstart=strt_dt, until=end_dt)]
    diff=len(dates)
    repeat=[len(np.where(s==np.array(totallist))[0])/(diff) for s in singlelist]
    return np.array(repeat)



# ## Saves only the files between the start year/start month and end year/end month



def sortfiles(fp,MERA,startime,endtime):
    paramlist=[fs.replace(MERA+'/','').split('_')[4] for fs in fp]
    paramheight=[fs.replace(MERA+'/','').split('_')[4] for fs in fp]
    styear=int(startime.split('/')[0])
    stmonth=int(startime.split('/')[1])
    stday=int(startime.split('/')[2])
    sthour=int(startime.split('/')[3])
    endyear=int(endtime.split('/')[0])
    endmonth=int(endtime.split('/')[1])
    endday=int(endtime.split('/')[2])
    endhour=int(endtime.split('/')[3])
    ind,indicatorofparamlist= remove_duplicates(paramlist)
    repeat=count_duplicates(indicatorofparamlist,paramlist,styear,stmonth,stday,sthour,endyear,endmonth,endday,endhour)
    heights=np.array(paramheight)[ind]

    return(indicatorofparamlist,heights,repeat,paramlist)


def clear_files(o,dirout,filenameout,indicatorofparamlist,startime,endtime):
    styear=int(startime.split('/')[0])
    stmonth=int(startime.split('/')[1])
    stday=int(startime.split('/')[2])
    sthour=int(startime.split('/')[3])
    endyear=int(endtime.split('/')[0])
    endmonth=int(endtime.split('/')[1])
    endday=int(endtime.split('/')[2])
    endhour=int(endtime.split('/')[3])
    stT=dates.date2num(datetime.datetime(styear,stmonth,stday,sthour))
    endT=dates.date2num(datetime.datetime(endyear,endmonth,endday,endhour))
    grbs=pygrib.open(o)
    times=np.array([(dates.date2num(g.validDate),g.hour,g.endStep) for g in grbs])
    vT=times.T[0]
    HH=times.T[1]
    FC=times.T[2]
    indices=np.where((vT>=stT) * (vT<=endT))[0]
    grbs=pygrib.open(o)
    for ind in indices:
        g=grbs.message(ind+1)
        hh="%02d" %(HH[ind])
        fc="%02d" %(FC[ind])
        fn=dirout+'/'+filenameout+str(g.dataDate).zfill(8)+'_'+hh+'+'+fc+'.grb'
        if os.path.exists(fn):
            os.remove(fn)
    return
