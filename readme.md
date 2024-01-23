Source: [Sunrise Equation](https://en.wikipedia.org/wiki/Sunrise_equation)

# Explanation of Algorithm for Earth
## Calculate the current Julian day
$$n=\lceil J_{date}-2451545.0+0.0008\rceil$$

where:
- $n$ is the number of days since Jan 1st, 2000 12:00
- $J_{date}$ is the Julian date
- 2451545.0 is the number of Julian days from the beginning of the Julian calendar to Jan 1st, 2000, 12:00. 0.0008 is the fractional Julian Day for leap seconds and terrestrial time

## Mean solar time
$$J^*=n-\frac{l_w}{360\degree}$$
where:
- $J^*$ is an approximation of mean solar time at Julian day $n$

## Solar mean anomaly
$$M=\left(357.5291+0.98560028J^*\right)\mod 360$$

## Equation of the center
$$C=1.9148\sin{M}+0.0200\sin{2M}+0.0003\sin{3M}$$
with the coefficients deriving from the eccentricity of the orbit $e$ as follows:
$$C=\arcsin{\left(2e+\frac{1}{4}e^3+\frac{5}{96}e^5+\frac{107}{4608}e^7\right)}\sin{M}$$

$$+\arcsin{\left(\frac{5}{4}e^2-\frac{11}{24}e^4+\frac{17}{192}e^6\right)}\sin{2M}$$

$$+\arcsin{\left(\frac{13}{12}e^3-\frac{43}{64}e^5+\frac{95}{512}e^7\right)}\sin{3M}+...$$
In the case of Earth, $e=0.01671$.

For a circular orbit, $e=0$ so $C=0$

## Ecliptic longitude
$$\lambda=\left(M+C+180+102.9371\right)\mod 360$$
with $102.9372$ being the value for the argument of the perihelion.

The argument of the perihelion (or periapsis) is the angle along the body's orbit at which it is closest to its orbiting partner, measured from its ascending node.

## Declination of the Sun
$$\sin{\delta}=\sin{\lambda}\cdot\sin{23.4397\degree}$$
with $23.4397\degree$ being the Earth's axial tilt toward the sun

## Hour angle
$$\cos{\omega_o}=\frac{\sin{-0.833\degree}-\sin{\phi}\sin{\delta}}{\cos{\phi}\cos{\delta}}$$
where:
- $\phi$ is the observer's latitude from the equator (positive is north, negative is south)
- $-0.833$ is the altitude angle of the center of the solar disc

## Duration from sunrise to sunset
$$\tau=2\cdot\frac{24}{360\degree}\omega_o$$

# Explanation of General Algorithm
## Mean solar time
$$J^*=n_d-\frac{L}{360\degree}$$
where:
- $n_d$ is the number of days
- $L$ is the observer's longitude ($-180\degree\le L\lt180\degree$)

## Solar mean anomaly
$$M=\frac{J^*}{y_l}360\degree$$
where:
- $y_l$ is the length of the planet's year in its days

## Equation of the center
$$C=a_0\sin{M}+a_1\sin{2M}+a_2\sin(M)$$
This is a truncation of the periodic series expansion with the coefficients calculated as follows:
- $a_0=\arcsin{\left(2e-\frac{1}{4}e^3+\frac{5}{96}e^5+\frac{107}{4608}e^7\right)}$
- $a_1=\arcsin{\left(\frac{5}{4}e^2-\frac{11}{24}e^4+\frac{17}{192}e^2\right)}$
- $a_2=\arcsin{\left(\frac{13}{12}e^3-\frac{43}{64}e^5+\frac{95}{512}e^7\right)}$

where $e$ is the eccentricity of the orbit, and each of the coefficients is in units of degrees.

This is a correction to the solar mean anomaly to account for the ellipticity of an orbit.

## Ecliptic longitude
$$\lambda=\left(M+C\right)\mod{360\degree}$$

## Declination of the Sun
$$\sin{\delta}=\sin{\lambda}\sin{\alpha}$$
where:
- $\alpha$ is the axial tilt of the planet

## Hour angle
$$\cos{\omega_o}=\frac{\sin{a}-\sin{l}\sin{\delta}}{\cos{l}\cos{\delta}}$$
where:
- $l$ is the observer's latitude on the planet
- $a$ is the altitude angle from the sun's center to its upper arm. ($-0.833\degree$)

## Duration from sunrise to sunset
$$\tau=\frac{2\omega_o}{360\degree}h$$
where:
- $h$ is the amount of time in a day on the planet (24 hours for Earth)

One could instead calculate the fraction or percentage of the day that has light:
$$\tau_{frac}=\frac{2\omega_o}{360\degree}\left(100\%\right)$$