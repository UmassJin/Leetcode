[G4G](http://www.geeksforgeeks.org/calculate-angle-hour-hand-minute-hand/)

This problem is know as Clock angle problem where we need to find angle between hands of an analog clock at .

Examples:

```
Input:  h = 12:00, m = 30.00
Output: 165 degree

Input:  h = 3.00, m = 30.00
Output: 75 degree
```

```python
def time_calcAngle(hour, minite):
    if hour < 0 or minite < 0 or minite > 60 or hour > 24:
        return None
    hour = hour %12
    minite = minite %60

    # hour_angle: 360'/12h = 30'/h -> 30'/60 = 0.5'/min
    # ex: 12:25 -> hour angle is 25 mins * 0.5'/min for hour angle 
    hour_angle =  (360.0/60)*(1.0/12)*minite + (360.0/12)*hour
    minite_angle = (360.0/60) * minite

    print "hour:", hour_angle
    print "minite: ", minite_angle
    angle = abs(hour_angle - minite_angle)%360
    return angle

print time_calcAngle(12,25)
print time_calcAngle(3,25)

# Note: we should use the 360.0/60, not 360/60!!!
```                        
