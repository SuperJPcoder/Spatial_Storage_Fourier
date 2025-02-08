# 🌍 Fourier Approximation of Geospatial Data

This project explores the application of **Fourier Series** to approximate complex geospatial shapes, specifically coastlines and land boundaries, using **Python**. By leveraging **Fast Fourier Transform (FFT)**, the algorithm decomposes geospatial data into frequency components, reconstructing the original shape with a limited number of terms to balance accuracy and efficiency.

The method offers a compact representation of geographical features, which is particularly useful in data compression, geospatial analysis, and computational geometry - possibly even helping in spatial querying as it then relies on math.

---
## 📸 Media

<img src="https://github.com/user-attachments/assets/5944b978-3d58-44fa-a940-e53dcbca386d" width="300">

---

## 🚀 Installation

Ensure you have Python installed. Then, install the required dependencies:

```sh
pip install numpy matplotlib scipy geopandas
```

---

## 📜 Usage

To run the script and visualize Fourier approximations of geospatial data:

```sh
python SGD_research.py
```

If the detailed geospatial data cannot be fetched, the script will generate a synthetic dataset automatically.

---

## 📊 Methodology

1. **Data Acquisition**: The script retrieves geospatial boundary data using **GeoPandas**.
2. **Fourier Transform**: The coordinates are converted into a complex plane representation, followed by applying **Fast Fourier Transform (FFT)**.
3. **Truncation and Reconstruction**: By limiting the number of Fourier coefficients, the shape is reconstructed with varying levels of detail.
4. **Visualization**: Results are plotted using **Matplotlib** to compare original and approximated shapes.

This approach allows users to explore how different frequency components contribute to shape reconstruction and experiment with different levels of approximation.

---

## 🛠 Contributing

We welcome contributions! To get started:

1. **Fork** the repository 🍴
2. **Clone** your forked repo:

```sh
git clone https://github.com/your-username/Spatial_Storage_Fourier.git
```

3. **Create a new branch** for your feature:

```sh
git checkout -b feature-name
```

4. **Make your changes & commit**:

```sh
git commit -am "Added an awesome feature!"
```

5. **Push to your branch**:

```sh
git push origin feature-name
```

6. Open a **Pull Request (PR)** 🚀

---

## ⚡ Open for Expansion!

This project is open-source and ready for further improvements!

Feel free to contribute and push this project further! 🚀🎨

