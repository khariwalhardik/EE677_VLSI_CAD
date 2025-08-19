# 🖥️ VHDL Logic Simulator

This project is a **command-line tool** for simulating **gate-level VHDL netlists** with custom input vectors.  
It parses a `.vhdl` netlist, converts it to an intermediate representation, generates simplified logic, and evaluates the circuit against simulation vectors.

---

## 📂 Project Structure

```
A1_LOGIC_SIMULATOR/
│── main.py                     # Entry point to run the app
│── requirements.txt             # Dependencies
│── README.md                    # Documentation
│
├── src/                         # Source code modules
│   ├── config.py                # Path configuration
│   ├── parse_gate_level.py      # Parse VHDL netlist → JSON
│   ├── generate_slc.py          # Generate simplified logic expression
│   ├── compiled_code_simulation.py  # Logic simulation engine
│
├── data/
│   ├── inputs/                  # Input files
│   │   ├── gate_level_netlist.vhdl   # Example VHDL netlist
│   │   └── inputs.txt                # Simulation input vectors
│   ├── intermediate/            # Intermediate outputs (auto-generated)
│   │   ├── gate_level_netlist.json
│   │   └── gate_level_netlist_slc.txt
│   ├── outputs/                 # Final simulation outputs
│   │   └── gate_level_netlist_output.txt
│
└── venv/                        # Virtual environment (optional)
```

---

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/vhdl-logic-simulator.git
cd vhdl-logic-simulator
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the app:

```bash
python main.py
```

You will be prompted for:

1. **VHDL netlist file name** (without extension, must be in `data/inputs/`)
2. **Simulation vectors file name** (without extension, must be in `data/inputs/`)

Example:

```
Enter the name of your VHDL file (without vhdl extension): gate_level_netlist
Enter the name of your simulation vectors file (without txt extension): inputs
```

---

## ⚙️ Workflow

1. **Parse VHDL netlist** → JSON (`intermediate/`)
2. **Generate simplified logic expression (SLC)** → text file (`intermediate/`)
3. **Run simulation** using vectors from `data/inputs/`
4. **Write results** to `data/outputs/`

---

## 📖 Example

### Input VHDL (`gate_level_netlist.vhdl`)

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux2to1 is
    Port ( a : in STD_LOGIC;
           b : in STD_LOGIC;
           sel : in STD_LOGIC;
           y : out STD_LOGIC);
end mux2to1;

architecture gate_level of mux2to1 is
    signal nsel, a_and, b_and : STD_LOGIC;
begin
    n1: not_gate port map (sel, nsel);
    n2: and_gate port map (a, nsel, a_and);
    n3: and_gate port map (b, sel, b_and);
    n4: or_gate  port map (a_and, b_and, y);
end gate_level;

```

### Input Vectors (`inputs.txt`)

```
a b sel
0 0 0
0 1 0
1 0 1
1 1 1
```

### Output (`outputs/gate_level_netlist_output.txt`)

```
OUTPUT
0
0
0
1
```

---

## 🛠️ Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature-new`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-new`)
5. Open a Pull Request 🚀

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` file for details.
