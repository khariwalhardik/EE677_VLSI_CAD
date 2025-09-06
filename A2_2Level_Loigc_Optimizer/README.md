# 2-Level Logic Optimizer (EE677 VLSI CAD Assignment)

**Author:** Hardik Khariwal
**Course:** EE677 – Foundations of VLSI CAD

---

## Project Overview

This project implements a **2-level logic optimizer** for Boolean functions in **PLA (Programmable Logic Array) format**.
It reads a PLA file, generates cubes for the ON-set and don't-care set, computes **prime implicants**, applies a **heuristic cover algorithm** to select a minimal set of primes, and writes the optimized function back to a PLA file.

The optimizer supports **multi-output functions** and is designed for **educational purposes** as part of the EE677 course.

---

## Folder Structure

```
project_root/
├─ inputs/                  # Input PLA files go here
├─ outputs/                 # Optimized PLA files will be written here
├─ src/                     # Python modules
│   ├─ cube.py              # Boolean cube representation and operations
│   ├─ pla_parser.py        # PLA file parser
│   ├─ pla_to_cubes.py      # Convert PLA cubes to Cube objects
│   ├─ prime_generator.py   # Generate prime implicants
│   ├─ heuristic_cover.py   # Heuristic minimal cover selection
│   └─ pla_writer.py        # Write optimized cubes to PLA
├─ main.py                  # Entry point to run the optimizer
├─ PLA_format.md             # PLA format specification and examples
├─ ProblemStatement.md       # Assignment problem statement
└─ README.md                # Project documentation (this file)
```

---

## Documentation

* **[ProblemStatement.md](ProblemStatement.md)** – Explains the assignment, objectives, and detailed problem description.
* **[PLA\_format.md](PLA_format.md)** – Describes the PLA file format, input/output conventions, and examples.

---

## How to Use the Project

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. **Place PLA files in the `inputs/` folder**

* Example: `inputs/example1.pla`

3. **Run the optimizer**

```bash
python main.py
```

* Enter the **input PLA filename** (relative to `inputs/`):

```
Enter the input file Name from input folder:
example1.pla
```

4. **Check the output**

* The optimized PLA will be written to the `outputs/` folder:

```
outputs/example1_optimized.pla
```

* Open the PLA file to see the reduced number of product terms.

---

## Example Workflow

**Input PLA (`inputs/example1.pla`):**

```pla
.i 3
.o 1
.ilb a b c
.ob f
110 1
111 1
001 1
011 1
101 1
.e
```

**Output PLA (`outputs/example1_optimized.pla`):**

```pla
.i 3
.o 1
.ilb a b c
.ob f
11- 1
1-1 1
.e
```

> The output shows a **reduced set of cubes**, covering the same ON-set as the input.

---

## Project Workflow (High-level)

1. **Parse PLA** → `pla_parser.py`
2. **Convert to cubes** → `pla_to_cubes.py`
3. **Generate prime implicants** → `prime_generator.py`
4. **Select heuristic minimal cover** → `heuristic_cover.py`
5. **Write optimized PLA** → `pla_writer.py`

---

## Notes

* The heuristic cover algorithm is **fast** but may not always produce the exact minimal SOP.
* For exact minimal results, **Quine–McCluskey** or **Espresso exact mode** would be required.
* Multi-output functions are supported; each output is optimized independently.

---

## Dependencies

* Python 3.x
* No external libraries required

---

## License

This project is for **educational purposes** as part of EE677 VLSI CAD. All rights reserved.


