# 2-Level Logic Optimizer

This project implements a **two-level Boolean logic optimizer**.
It supports **PLA format** (Programmable Logic Array) and **Boolean expression text files**, with conversion between the two.
The optimizer uses **prime implicant generation** and a **heuristic cover selection** approach, inspired by Espresso/Quine–McCluskey.

---

## 📂 Folder Structure

```
.
├── inputs/
│   ├── pla/        # Input .pla files
│   └── txt/        # Input Boolean expressions (.txt)
│
├── outputs/
│   ├── pla/        # Optimized PLA files
│   └── txt/        # SOP Boolean expressions from PLA
│
├── src/            # Source code
│   ├── pla_parser.py
│   ├── pla_to_cubes.py
│   ├── pla_writer.py
│   ├── pla_to_sop.py
│   ├── sop_to_pla.py
│   ├── prime_generator.py
│   ├── heuristic_cover.py
│   └── main.py     # Entry point
│
├── ProblemStatement.md
├── PLA_Format.md
└── README.md
```

---

## 🚀 Features

* Read Boolean expressions in **text format**

  ```
  inputs: a b c
  outputs: f
  f = (a & ~b) | (~a & c)
  ```
* Convert Boolean text to **PLA format**
* Convert PLA back to **Boolean SOP expressions**
* Optimize multi-output PLA files with **prime implicant merging + heuristic cover**
* Works with **don’t cares** as well
* Clean output in both **PLA** and **SOP text**

---

## ⚡ Usage

### 1. Run the Optimizer

```bash
python src/main.py
```

You will be prompted:

* `Select input type:`

  * `1` → Text file (`inputs/txt/`)
  * `2` → PLA file (`inputs/pla/`)

Enter the base filename (without extension).
The tool will:

1. Convert text → PLA (if needed)
2. Run optimization
3. Save results in `outputs/pla/` and `outputs/txt/`

---

### 2. Example Input (Text)

`inputs/txt/example_expr.txt`:

```
inputs: x y z
outputs: f
f = (x & (~y | z)) | (~x & y & z)
```

---

### 3. Example Optimized Output

* Optimized PLA → `outputs/pla/example_expr.pla`
* SOP Expression → `outputs/txt/example_expr_output.txt`

```
inputs: x y z
outputs: f
f = (x & ~y) | (x & z) | (~x & y & z)
```

---
## Example Run

Below is an example showing the program execution for both input types:

- **Left:** Input from a Boolean Expression Text File (`.txt`)
- **Right:** Input from a PLA File (`.pla`)


<img width="1382" height="337" alt="image" src="https://github.com/user-attachments/assets/7df5dd71-9ebb-4232-9d08-00f6deaf8ea1" />

## 📘 References

* **Quine–McCluskey Algorithm** – for prime implicant generation
* **Espresso Logic Minimizer** – inspiration for heuristic cover
* [PLA Format](./PLA_Format.md) – file format details
* [Problem Statement](./ProblemStatement.md) – original assignment/problem description

---

## 👨‍💻 Author

**Hardik Khariwal** · Department of Electrical Engineering · *IIT Bombay*


