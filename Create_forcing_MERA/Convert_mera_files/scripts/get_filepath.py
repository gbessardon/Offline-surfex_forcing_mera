import os
from dateutil.rrule import rrule, MONTHLY
import datetime

## Gets the file path of all files with the right forecast length or analysis 
def get_filepaths(directory,flength,startime,endtime):
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
    file_paths = [] 
    dateslist= [(dt.year,dt.month) for dt in rrule(MONTHLY, dtstart=stT, until=endT)]
    # List which will store all of the full filepaths.
    # Walk the tree.
    for d in dateslist:
        YY=str(d[0])
        MM="%02d" % (d[1])
        i=0
        j=0
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath= os.path.join(root, filename)
                if '_'+YY+'_'+MM+'_' in filename:
                    if filename.endswith('0_FC'+flength+'hr'):
                        file_paths.append(filepath)  # Add it to the list.
                        j=j+1
        if j==0:
            print('warning no FORECAST file found FORECAST files required')
    return file_paths,dateslist