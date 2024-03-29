from math import sin, cos, asin, acos, sqrt, radians, degrees
import matplotlib.pyplot as plt

def calc_day_len(n_d, lat, long, ax, e, days_per_year, a, debug = False):
    # Mean stellar time
    J_star = n_d - long/360

    # Solar mean anomaly
    M = 360*J_star/days_per_year

    # Equation of the center
    a0 = degrees(asin(2*e - (1/4)*e**3 + (5/96)*e**5 + (107/4608)*e**7))
    a1 = degrees(asin((5/4)*e**2 - (11/24)*e**4 + (17/192)*e**6))
    a2 = degrees(asin((13/12)*e**3 - (43/64)*e**5 + (95/512)*e**7))
    C = a0*sin(radians(M)) + a1*sin(radians(2*M)) + a2*sin(radians(3*M))

    # Ecliptic longitude
    lam = (M + C) % 360

    # Declination of the Star
    sin_del = sin(radians(lam))*sin(radians(ax))

    # Hour angle
    cos_wo = (sin(radians(a)) - sin(radians(lat))*sin_del)/(cos(radians(lat))*cos(asin(sin_del)))

    if debug:
        print(f"Mean stellar time: J* = {J_star}")
        print(f"Mean stellar anomaly: M = {M % 360}\u00b0")
        print(f"Equation of center: C = {C}\u00b0")
        print(f"Ecliptic longitude: lambda = {lam}\u00b0")
        print(f"Declination of the Star: delta = {degrees(asin(sin_del))}\u00b0")
        print(f"Hour angle: w0 = {degrees(acos(cos_wo))}\u00b0")

    if cos_wo > 1:
        return 0
    elif cos_wo < -1:
        return 100
    else:
        return 2*100*degrees(acos(cos_wo))/360

# Current Julian day
lat = 45.           # Observer's planetary latitude
long = 0.           # Observer's planetary longitude
axial_tilt = 45     # Tilt of planet's rotational axis relative to orbital plane
eccentricity = 0    # Eccentricity of planet's orbit
days_per_year = 100
stellar_angle = -0.833   # Angle from stellar centre to upper arm

for day in range(days_per_year):
    print(f"Day length (percent of day): tau = {calc_day_len(day, lat, long, axial_tilt, eccentricity, days_per_year, stellar_angle)}%")