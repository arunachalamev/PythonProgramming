

def angleClock(hour,minutes):

    if hour == 12: hour = 0
    if minutes == 60: minutes = 0

    hour_angle = 0.5 * (hour*60 + minutes)
    minute_angle = 6* minutes

    angle = abs(hour_angle- minute_angle)

    angle = min (360-angle,angle)
          
    return angle 


print (angleClock(12,30))
print (angleClock(3,30))
print (angleClock(3,15))
print (angleClock(4,50))
print (angleClock(12,0))

