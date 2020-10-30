from dateutil.rrule import rrule, HOURLY
import datetime
import os
# links forecast files missing set the +03 forecast as the +00 of the next forecast except for first loop where 00 is set as equal to +01

def threehourslink(startime,endtime,dirout,filenameout,Flength):
    styear=int(startime.split('/')[0])
    stmonth=int(startime.split('/')[1])
    stday=int(startime.split('/')[2])
    sthour=int(startime.split('/')[3])
    endyear=int(endtime.split('/')[0])
    endmonth=int(endtime.split('/')[1])
    endday=int(endtime.split('/')[2])
    endhour=int(endtime.split('/')[3])
    stT=datetime.datetime(styear,stmonth,stday,sthour)
    endT=datetime.datetime(endyear,endmonth,endday,endhour)
    hourlist= list(rrule(HOURLY, dtstart=stT, until=endT)) # makes a list of everyhour during the forecast
    Thhourlist=[hourlist[r]  for r in range(0,len(hourlist),int(Flength))]
    forecastdates=[str(Th.year)+str(Th.month).zfill(2)+str(Th.day).zfill(2)+'_'+str(Th.hour).zfill(2) for Th in Thhourlist]
    for i,f in enumerate(forecastdates):
        if os.path.isfile(dirout+filenameout+forecastdates[i]+'+00.grb'):
            os.unlink(dirout+filenameout+forecastdates[i]+'+00.grb')
        if i==0:
            os.symlink(dirout+filenameout+forecastdates[i]+'+01.grb',dirout+filenameout+forecastdates[i]+'+00.grb')
        else:
            os.symlink(dirout+filenameout+forecastdates[i-1]+'+03.grb',dirout+filenameout+forecastdates[i]+'+00.grb')
    return