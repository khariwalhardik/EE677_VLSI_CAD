## 🔎 What is a PLA file?

PLA = **Programmable Logic Array** description.
It is a **text file** format that describes **multi-output Boolean functions** in terms of ON-set and don’t-cares.

Think of it as a **truth table with compact notation**.

---

## 🗂️ Structure of a PLA file

A `.pla` file has 3 parts:

1. **Header (parameters)**

   * `.i N` → number of inputs
   * `.o M` → number of outputs
   * `.ilb` → optional: input labels (names of input variables)
   * `.ob` → optional: output labels (names of functions)

2. **Cube list (body)**

   * Each line has two parts:

     ```
     input_pattern   output_pattern
     ```

     * `input_pattern`: sequence of `0/1/-` (`-` = don’t care input).
     * `output_pattern`: sequence of `0/1/-` (`-` = don’t care output).

   * Example:

     ```
     1-0  10
     ```

     means:

     * Inputs: `1-0` (input1=1, input2=don’t care, input3=0)
     * Outputs: `10` (output1=1, output2=0)

3. **End of file**

   * `.e` marks the end.

---

## 📄 Example 1: Simple AND function

Function: `f(a,b) = a·b`

PLA:

```
.i 2
.o 1
.ilb a b
.ob f
11 1
.e
```

Explanation:

* 2 inputs, 1 output.
* Only when input = `11`, output = `1`.

---

## 📄 Example 2: Multiple Outputs

Suppose:

* `f1 = a b`
* `f2 = a + b`

PLA:

```
.i 2
.o 2
.ilb a b
.ob f1 f2
11 10
10 01
01 01
.e
```

Explanation:

* Line `11 10`: when `a=1, b=1` → `f1=1, f2=0`.
* Line `10 01`: when `a=1, b=0` → `f1=0, f2=1`.
* Line `01 01`: when `a=0, b=1` → `f1=0, f2=1`.

---

## 📄 Example 3: Don’t cares

Function: `f(a,b) = a (don’t care when b=0)`

PLA:

```
.i 2
.o 1
.ilb a b
.ob f
1- 1
.e
```

Here `1-` means: input1 must be `1`, input2 can be anything.

---

✅ So, in this project:

* **inputs/** folder will contain `.pla` files (each representing a Boolean function to be optimized).
* Your program in **src/** will read these PLA files, parse them into internal data structures (minterms, cubes).
* Later, optimized output will go into **outputs/** as new `.pla` files.


