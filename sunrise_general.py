from math import sin, cos, asin, acos, sqrt, radians, degrees
import matplotlib.pyplot as plt

def calc_day_len(n_d, lat, long, ax, e, days_per_year):
    # Mean solar time
    J_star = n_d - long/360
    print(f"Mean solar time: J* = {J_star}")

    # Solar mean anomaly
    M = 360*J_star/days_per_year
    print(f"Mean solar anomaly: M = {M % 360}\u00b0")

    # Equation of the center
    a0 = degrees(asin(2*e - (1/4)*e**3 + (5/96)*e**5 + (107/4608)*e**7))
    a1 = degrees(asin((5/4)*e**2 - (11/24)*e**4 + (17/192)*e**6))
    a2 = degrees(asin((13/12)*e**3 - (43/64)*e**5 + (95/512)*e**7))
    C = a0*sin(radians(M)) + a1*sin(radians(2*M)) + a2*sin(radians(3*M))
    print(f"Equation of center: C = {C}\u00b0")

    # Ecliptic longitude
    lam = (M + C) % 360
    print(f"Ecliptic longitude: lambda = {lam}\u00b0")

    # Declination of the Sun
    sin_del = sin(radians(lam))*sin(radians(ax))
    print(f"Declination: delta = {degrees(asin(sin_del))}\u00b0")

    # Hour angle
    cos_wo = (sin(-radians(0.833)) - sin(radians(lat))*sin_del)/(cos(radians(lat))*cos(asin(sin_del)))
    print(f"Hour angle: w0 = {degrees(acos(cos_wo))}\u00b0")

    return 2*100*degrees(acos(cos_wo))/360

# Current Julian day
days = 90
lat = 45.
long = 0.
axial_tilt = 23.4397
eccentricity = 0.01671
days_per_year = 365.25

print(f"Day length (percent of day): tau = {calc_day_len(days, lat, long, axial_tilt, eccentricity, days_per_year)}%")