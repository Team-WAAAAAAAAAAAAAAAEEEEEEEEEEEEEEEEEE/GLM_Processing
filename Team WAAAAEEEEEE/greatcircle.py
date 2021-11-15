#-----------------------------------------------------------------------
# greatcircle.py
#-----------------------------------------------------------------------
#(c)2015 Robert Sedgewick, Kevin Wayne, and Robert Dondero
#import stdio
#import sys
import math
def great_circle(lat1, lon1, lat2, lon2): 
    # Accept float command-line arguments x1, y1, x2, and y2: the latitude
    # and longitude, in degrees, of two points on the earth. Compute and
    # write to standard output the great circle distance (in nautical
    # miles) between those two points.

    # The following formulas assume that angles are expressed in radians.
    # So convert to radians.

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Compute using the law of cosines.

    # Great circle distance in radians
    angle1 = math.acos(math.sin(lat1) * math.sin(lat2) \
             + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

    # Convert back to degrees.
    angle1 = math.degrees(angle1)

    # Each degree on a great circle of Earth is 60 nautical miles.
    distance1 = 60.0 * angle1

    return distance1

    # Compute using the Haversine formula.

    #a = math.sin((lat2-lat1)/2.0) ** 2.0 \
        #+ (math.cos(lat1) * math.cos(lat2) * (math.sin((lon2-lon1)/2.0) ** 2.0))

    # Great circle distance in radians
   #angle2 = 2.0 * math.asin(min(1.0, math.sqrt(a)))

    # Convert back to degrees.
    #angle2 = math.degrees(angle2)

    # Each degree on a great circle of Earth is 60 nautical miles.
    #distance2 = 60.0 * angle2

    #stdio.writeln(str(distance2) + ' nautical miles')

#-----------------------------------------------------------------------

# Leningrad to SF

# python greatcircle.py 59.9 -30.3 37.8 122.4
# 4784.369673474519 nautical miles
# 4784.369673474519 nautical miles
#
# Paris to Austin

# python greatcircle.py 48.87 -2.33 30.27 97.74
# 4423.14075970742 nautical miles
# 4423.140759707421 nautical miles
#
# Nashville airport (BNA) to LAX

# python greatcircle.py 36.12 -86.67 33.94 -118.4
# 1557.505111036951 nautical miles
# 1557.5051110369507 nautical miles
#
# Princeton to Paris

# python greatcircle.py 40.35 74.65 48.87 -2.33
# 3185.1779271158425 nautical miles
# 3185.1779271158416 nautical miles