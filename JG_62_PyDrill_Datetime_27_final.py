#   62_PyDrill_Datetime_27_idle
#
#   John Goya
#
#   For Python Drill #62 - Using Datetime with Python & idle.
#
from datetime import datetime
#import timezone
import pytz

#day/time for Portland - US/Pacific
dt_pdx = datetime.now(pytz.timezone('US/Pacific'))
print str(dt_pdx)
print str('Portland time - {:%I:%M %p}\n'.format(dt_pdx))

'''
print 'It is {:%I:%M %p} in New York now.'.format(datetime.now(pytz.timezone('US/Eastern')))
print 'It is {:%I:%M %p} now.'.format(datetime.now())
print 'Today is {:%B %d, %Y}'.format(datetime.now())
'''

#day/time for NYC - US/Eastern
dt_nyc = datetime.now(pytz.timezone('US/Eastern'))
#'{:%I:%M %p}'.format(dt_nyc)
print str(dt_nyc)
print str('NYC current time - {:%I:%M %p}'.format(dt_nyc))

#set open/close time for NYC

def nyc_open (hr, min=0, sec=0, micros=0):
   now = datetime.now(pytz.timezone('US/Eastern'))
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

def nyc_close (hr, min=0, sec=0, micros=0):
   now = datetime.now(pytz.timezone('US/Eastern'))
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


#dt_nyc_open = datetime(2000, 1, 1, 9, 00, tzinfo=(pytz.timezone('US/Eastern')))
#dt_nyc_close = datetime(2000, 1, 1, 21, 0, tzinfo=(pytz.timezone('US/Eastern')))

print nyc_close(9)

print ('NYC store open time {:%I:%M %p}'.format(nyc_open(9)))

print nyc_close(21)

print str('NYC store close time {:%I:%M %p}\n'.format(nyc_close(21)))


if nyc_open(9).strftime("%H:%M %p") < dt_nyc.strftime("%H:%M %p") and dt_nyc.strftime("%H:%M %p") < nyc_close(21).strftime("%H:%M %p"):
    print('NYC store is open\n')
else:
    print('NYC store is closed')
#day/time for London - Europe/London
dt_ldn = datetime.now(pytz.timezone('Europe/London'))
#'{:%I:%M %p}'.format(dt_ldn)
print str(dt_ldn)
print str('London current time - {:%I:%M %p}'.format(dt_ldn))

#set open/close time for London

def ldn_open (hr, min=0, sec=0, micros=0):
   now = datetime.now(pytz.timezone('Europe/London'))
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

def ldn_close (hr, min=0, sec=0, micros=0):
   now = datetime.now(pytz.timezone('Europe/London'))
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


#dt_ldn_open = datetime(2000, 1, 1, 9, 00, tzinfo=(pytz.timezone('Europe/London')))
#dt_ldn_close = datetime(2000, 1, 1, 21, 0, tzinfo=(pytz.timezone('Europe/London')))

print ldn_close(9)

print ('London store open time {:%I:%M %p}'.format(ldn_open(9)))

print ldn_close(21)

print str('London store close time {:%I:%M %p}\n'.format(ldn_close(21)))


if ldn_open(9).strftime("%H:%M %p") < dt_ldn.strftime("%H:%M %p") and dt_ldn.strftime("%H:%M %p") < ldn_close(21).strftime("%H:%M %p"):
    print('London store is open')
else:
    print('London store is closed')
