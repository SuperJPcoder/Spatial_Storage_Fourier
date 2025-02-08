import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Or try 'Qt5Agg' if TkAgg still doesn't work
import matplotlib.pyplot as plt

# ... rest of your script ...
from scipy.fft import fft, ifft
import geopandas as gpd

# Load detailed geospatial data (e.g., coastline of a region)
try:
    gdf = gpd.read_file('https://raw.githubusercontent.com/johan/world.geo.json/master/countries/USA/FL.geo.json')
    coastline = gdf.geometry[0].exterior.coords.xy
    x = np.array(coastline[0])
    y = np.array(coastline[1])
except Exception as e:
    print("Could not fetch detailed data, using sample data instead:", e)
    x = np.linspace(-80, -80, 200) + np.cos(np.linspace(0, 4 * np.pi, 200))
    y = np.linspace(25, 30, 200) + np.sin(np.linspace(0, 4 * np.pi, 200))

n_points = len(x)
t = np.linspace(0, 2 * np.pi, n_points, endpoint=False)

x_coefficients = fft(x)
y_coefficients = fft(y)

def fourier_series(t, coeffs, n_terms=50):
    a0 = coeffs[0].real / len(coeffs)
    result = a0 * np.ones_like(t)
    for n in range(1, n_terms):
        a_n = coeffs[n].real / len(coeffs)
        b_n = coeffs[n].imag / len(coeffs)
        result += 2 * (a_n * np.cos(n * t) - b_n * np.sin(n * t))
    return result

x_approx = fourier_series(t, x_coefficients, n_terms=50)
y_approx = fourier_series(t, y_coefficients, n_terms=50)


# --- Displaying Fourier Series Information ---
n_terms_to_display = 51  # Number of terms to show

print("Fourier Series Coefficients (First {} terms):".format(n_terms_to_display))

for n in range(n_terms_to_display):
  x_mag = np.abs(x_coefficients[n]) / len(x_coefficients)  # Magnitude
  x_phase = np.angle(x_coefficients[n])  # Phase
  y_mag = np.abs(y_coefficients[n]) / len(y_coefficients)
  y_phase = np.angle(y_coefficients[n])
  print(f"Term {n+1}:")
  print(f"  X: Magnitude = {x_mag:.4f}, Phase = {x_phase:.4f}")
  print(f"  Y: Magnitude = {y_mag:.4f}, Phase = {y_phase:.4f}")
  print("-" * 30)

# --- Plotting ---
plt.figure(figsize=(12, 8))
plt.plot(x, y, label='Original Complex Map', color='blue', linewidth=1)
plt.plot(x_approx, y_approx, label='Fourier Approximation', color='red', linestyle='--', linewidth=2)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.title('Complex Map - Original vs. Fourier Series Approximation')
plt.grid(True)
plt.show()
