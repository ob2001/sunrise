import numpy as np
import matplotlib.pyplot as plt

def safe_arcsin(x):
    return -90 if x < -1 else 90 if x > 1 else np.rad2deg(np.arcsin(x))

def safe_arcsin_arr(xs):
    return np.array([safe_arcsin(x) for x in xs])

def safe_arccos(x):
    return 180 if x < -1 else 0 if x > 1 else np.rad2deg(np.arccos(x))

def safe_arccos_arr(xs):
    return np.array([safe_arccos(x) for x in xs])

def calc_day_len(n_d, lat, ax, e, days_per_year, a, debug = False):
    # Solar mean anomaly
    M = 360*n_d/days_per_year

    # Equation of the center
    a0 = safe_arcsin(2*e - (1/4)*e**3 + (5/96)*e**5 + (107/4608)*e**7)
    a1 = safe_arcsin((5/4)*e**2 - (11/24)*e**4 + (17/192)*e**6)
    a2 = safe_arcsin((13/12)*e**3 - (43/64)*e**5 + (95/512)*e**7)
    
    C = a0*np.sin(np.deg2rad(M)) + a1*np.sin(np.deg2rad(2*M)) + a2*np.deg2rad(np.deg2rad(3*M))

    # Ecliptic longitude
    lam = (M + C) % 360

    # Stellar declination
    sin_del = np.sin(np.deg2rad(lam))*np.sin(np.deg2rad(ax))

    # Hour angle
    cos_wo_tmps = (np.sin(np.deg2rad(a)) - np.sin(np.deg2rad(lat))*sin_del)/(np.cos(np.deg2rad(lat))*np.cos(np.arcsin(sin_del)))
    wo = np.array([safe_arccos_arr(cos_wo_tmps[i]) for i in range(cos_wo_tmps.shape[0])])

    if debug:
        print(f"Mean stellar anomaly: M = {M % 360}\u00b0")
        print(f"Equation of center: C = {C}\u00b0")
        print(f"Ecliptic longitude: lambda = {lam}\u00b0")
        print(f"Declination of the Star: delta = {np.rad2deg(safe_arcsin(sin_del))}\u00b0")
        print(f"Hour angle: w0 = {wo}\u00b0")

    return 2*100*wo/360

# Current Julian day
axial_tilt = 23     # Tilt of planet's rotational axis relative to orbital plane
eccentricity = 0.3    # Eccentricity of planet's orbit (max ~= 0.516)
stellar_angle = 0   # Angle from stellar centre to upper arm
days_in_year = 1

days = np.linspace(0, days_in_year, 100)
lats = np.linspace(0, 90, 100)

X, Y = np.meshgrid(days, lats)
calcs = calc_day_len(X, Y, axial_tilt, eccentricity, days_in_year, stellar_angle)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection = "3d", 
                     title = f"Axial tilt: $\\theta={axial_tilt}\\degree$\nOrbital Eccentricity: $e={eccentricity}$\nStellar Angle: $\\Sigma={stellar_angle}\\degree$", 
                     xlabel = "Day of Year", 
                     ylabel = "Latitude ($\\degree$ from Equator)", 
                     zlabel = "% Daylight")

ax.plot_surface(X, Y, calcs)
plt.show()