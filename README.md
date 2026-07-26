# 🔢 Thomas Algorithm in Python

A Python implementation of the **Thomas Algorithm (Tridiagonal Matrix Algorithm - TDMA)** for efficiently solving systems of linear equations with a tridiagonal coefficient matrix.

---

## 📖 Overview

The Thomas Algorithm is a simplified form of Gaussian Elimination specifically designed for **tridiagonal matrices**. Since only the main diagonal and the two adjacent diagonals contain non-zero elements, the algorithm significantly reduces computational complexity compared to standard elimination methods.

This project provides a clean Python implementation of the algorithm along with an example problem and visualization of the computed solution.

---

## ✨ Features

- Efficient implementation of the Thomas Algorithm
- Solves tridiagonal systems of linear equations
- Simple and well-commented Python code
- Fast forward elimination and backward substitution
- Easy to modify for larger systems
- Suitable for engineering and scientific applications

---

## 📂 Repository Structure

```
Thomas-Algorithm-Python/
│
├── thomas_algorithm.py
├── example.py
├── sample_input.txt
├── sample_output.txt
├── figures/
│   ├── solution_plot.png
│   └── flowchart.png
├── presentation/
├── report/
├── LICENSE
└── README.md
```

---

## ⚙️ How the Algorithm Works

The Thomas Algorithm consists of two main stages:

### 1. Forward Elimination

- Modify the upper diagonal coefficients.
- Update the right-hand-side vector.
- Eliminate lower diagonal elements.

### 2. Backward Substitution

- Compute the final unknown values.
- Start from the last equation.
- Continue upward until all variables are determined.

---

## 🧮 Algorithm Steps

1. Read the lower, main, and upper diagonal arrays.
2. Read the right-hand-side vector.
3. Perform forward elimination.
4. Perform backward substitution.
5. Display the solution vector.

---

## 💻 Example

Given the tridiagonal system:

```
| 2 -1  0 | |x₁|   | 1 |
|-1  2 -1 | |x₂| = | 0 |
| 0 -1  2 | |x₃|   | 1 |
```

Output:

```
x₁ = 1.0
x₂ = 1.0
x₃ = 1.0
```

---

## ▶️ Getting Started

### Prerequisites

- Python 3.8 or later

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Thomas-Algorithm-Python.git
```

Move into the project directory:

```bash
cd Thomas-Algorithm-Python
```

Run the program:

```bash
python thomas_algorithm.py
```

---

## 📊 Time Complexity

| Operation | Complexity |
|-----------|------------|
| Forward Elimination | O(n) |
| Backward Substitution | O(n) |
| Total | **O(n)** |

---

## 🚀 Applications

The Thomas Algorithm is widely used in engineering and scientific computing, including:

- Computational Fluid Dynamics (CFD)
- Heat Transfer Analysis
- Finite Difference Method (FDM)
- Structural Engineering
- Numerical Solution of Differential Equations
- Groundwater Flow Simulation
- Computational Physics
- Electrical Circuit Analysis

---

## ✅ Advantages

- Very fast for tridiagonal systems
- Linear time complexity **O(n)**
- Low memory usage
- Easy to implement
- More efficient than Gaussian Elimination for tridiagonal matrices

---

## ⚠️ Limitations

- Applicable only to tridiagonal matrices
- Requires non-zero main diagonal elements
- Less suitable for sparse matrices with arbitrary patterns
- No pivoting, so numerical stability depends on the matrix properties

---

## 📈 Future Improvements

- Add support for sparse matrix formats
- Develop a graphical user interface (GUI)
- Benchmark against other numerical methods
- Extend to block tridiagonal systems
- Package the implementation as a reusable Python library

---

## 📚 References

1. Thomas, L. H. (1949). *Elliptic Problems in Linear Differential Equations over a Network.*
2. Chapra, S. C., & Canale, R. P. *Numerical Methods for Engineers.*
3. Burden, R. L., & Faires, J. D. *Numerical Analysis.*

---

## 👨‍💻 Author

**David Ojha**

Bachelor of Mechanical Engineering  
Kathmandu University

GitHub: https://github.com/yourusername

Portfolio: https://yourportfolio.com

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and share this project for educational and research purposes.

---

## ⭐ Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🐛 Report issues
- 💡 Suggest improvements
- 🤝 Contribute with pull requests

Your support is greatly appreciated!
