# 🟣 Descartes Circle Theorem Visualizer
Descartes Circle Theorem Visualizer is an interactive Python-based visualization tool that demonstrates the geometry behind Descartes’ Theorem (also known as the Kissing Circles Theorem).

> “Where circles touch, mathematics speaks.”

An interactive visualization tool for exploring **Descartes’ Circle Theorem (Kissing Circles Theorem)** using Python. This project helps users understand the relationship between four mutually tangent circles through dynamic and visual simulation.

---

## 📌 Overview

Descartes’ Theorem describes the relationship between four mutually tangent circles (each circle touching the other three). Given the curvature (k = 1/radius) of three circles, the fourth circle’s curvature can be calculated using a beautiful mathematical formula.

This project turns that abstract idea into an **interactive visual experience**.

---

## ✨ Features

- 🔵 Visualize four mutually tangent circles in real-time  
- 🔄 Dynamically adjust circle sizes and positions  
- 📐 Compute curvature using Descartes’ Theorem  
- 🧠 Better intuition of geometric relationships  
- 🎮 Interactive exploration of classical geometry  
- 📊 Optional 2D/3D visualization support (if extended)

---

## 🧮 Mathematical Background

For four mutually tangent circles with curvatures:

- \( k_1, k_2, k_3, k_4 \)

Descartes’ Theorem states:

\[
(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)
\]

Solving for the fourth circle:

\[
k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1k_2 + k_2k_3 + k_3k_1}
\]

This formula allows us to compute the exact size of the fourth “kissing” circle.

---

## 🖥️ Tech Stack

- Python 🐍  
- NumPy 🔢  
- Matplotlib 📊  
- (Optional) mpl_toolkits for 3D visualization  
