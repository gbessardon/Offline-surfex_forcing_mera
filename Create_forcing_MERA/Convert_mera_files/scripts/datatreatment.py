import os
import numpy as np
import pygrib
from matplotlib import dates
import datetime
def datatreatment3(f,dirout,filenameout,indicatorofparamlist,startime,endtime):
        if not os.path.isdir(dirout):
            os.mkdir(dirout)
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
        grbs=pygrib.open(f)
        times=np.array([(dates.date2num(g.validDate),g.hour,g.endStep) for g in grbs])
        vT=times.T[0]
        HH=times.T[1]
        FC=times.T[2]
        indices=np.where((vT>=stT) * (vT<=endT))[0]
        grbs=pygrib.open(f)
        for ind in indices:
                    g=grbs.message(ind+1) ## input message
                    gout=g # output message
                    if g.indicatorOfParameter==117:
                            V117=g['values']
                            f116=f.replace('_117_','_116_')
                            V116=pygrib.open(f116).message(ind+1)['values']
                            gout.values=V117-V116
                           # print(V116)
                           # print(V117)
                           #print(gout.values)
                    if g.indicatorOfTypeOfLevel!='sfc':
                        gout.indicatorOfTypeOfLevel='sfc'
                    if g.timeRangeIndicator!=0:
                        gout.timeRangeIndicator=0
                    hh="%02d" %(HH[ind])
                    fc="%02d" %(FC[ind])
                    grbout= open(dirout+'/'+filenameout+str(gout.dataDate).zfill(8)+'_'+hh+'+'+fc+'.grb','ab')
                    grbout.write(gout.tostring())
                    grbout.close()
                    print(dirout+'/'+filenameout+str(gout.dataDate).zfill(8)+'_'+hh+'+'+fc+'.grb')
                    print(f)
        
        grbs.close()
        gro=pygrib.open(dirout+'/'+filenameout+str(g.dataDate).zfill(8)+'_'+hh+'+'+fc+'.grb')
        outparamlist=[go.indicatorOfParameter for go in gro]

        return