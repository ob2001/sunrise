from math import sin, ceil, degrees, cos, asin, acos, radians, sqrt
from datetime import datetime
import geocoder

def calc_day_len(date, lat, long, ax, e):
    # Calculate number of days since Jan 1st, 2000 12:00
    n = ceil(date - 2451545 + 0.0008)
    print(f"Julian days since Jan 1st, 2000, 12:00: n = {n}")

    # Mean solar time
    J_star = n - long/360
    print(f"Mean solar time: J* = {J_star}")

    # Solar mean anomaly
    M = (357.5291 + 0.98560028 * J_star) % 360
    print(f"Mean solar anomaly: M = {M}\u00b0")

    # Equation of the center
    a0 = degrees(asin(2*e - (1/4)*e**3 + (5/96)*e**5 + (107/4608)*e**7))
    a1 = degrees(asin((5/4)*e**2 - (11/24)*e**4 + (17/192)*e**6))
    a2 = degrees(asin((13/12)*e**3 - (43/64)*e**5 + (95/512)*e**7))
    C = a0*sin(radians(M)) + a1*sin(radians(2*M)) + a2*sin(radians(3*M))
    print(f"Equation of center: C = {C}\u00b0")

    # Ecliptic longitude
    lam = (M + C + 180 + 102.9372) % 360
    print(f"Ecliptic longitude: lambda = {lam}\u00b0")

    # Declination of the Sun
    sin_del = sin(radians(lam))*sin(radians(ax))
    print(f"Declination: delta = {degrees(asin(sin_del))}\u00b0")

    # Hour angle
    cos_wo = (sin(-radians(0.833)) - sin(radians(lat))*sin_del)/(cos(radians(lat))*cos(asin(sin_del)))
    print(f"Hour angle: w0 = {degrees(acos(cos_wo))}\u00b0")

    return 2*24*degrees(acos(cos_wo))/360

# Current Julian day
date = (datetime.now() - datetime.strptime('01/01/00 12:00:00', '%d/%m/%y %H:%M:%S')).days + 2451545 - 1

lat, long = geocoder.ip('').latlng
axial_tilt = 23.4397
eccentricity = 0.01671

print(f"Day length (hours): tau = {calc_day_len(date, lat, long, axial_tilt, eccentricity)}")