import itertools
import re
class PLA:
    def __init__(self):
        self.num_inputs = 0
        self.num_outputs = 0
        self.input_labels = []
        self.output_labels = []
        self.cubes = []

def eval_expression(expr: str, env: dict) -> int:
    """
    Evaluate Boolean expression with given environment mapping.
    Supports ~ (NOT), & (AND), | (OR), and parentheses.
    """
    expr_eval = expr
    # Replace variables with 0/1
    for var, val in env.items():
        expr_eval = re.sub(rf"\b{var}\b", str(val), expr_eval)

    # Replace operators with Python equivalents
    expr_eval = expr_eval.replace("~", " not ")
    expr_eval = expr_eval.replace("&", " and ")
    expr_eval = expr_eval.replace("|", " or ")

    return int(eval(expr_eval))


def sop_to_pla(filename: str) -> PLA:
    pla = PLA()

    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # First two lines: inputs and outputs
    pla.input_labels = lines[0].replace("inputs:", "").strip().split()
    pla.output_labels = lines[1].replace("outputs:", "").strip().split()
    pla.num_inputs = len(pla.input_labels)
    pla.num_outputs = len(pla.output_labels)

    # Equations: dict {output_name: expression}
    equations = {}
    for line in lines[2:]:
        out_name, expr = line.split("=")
        equations[out_name.strip()] = expr.strip()

    # Generate cubes via truth table enumeration
    for values in itertools.product([0, 1], repeat=pla.num_inputs):
        env = dict(zip(pla.input_labels, values))
        out_bits = []

        for out in pla.output_labels:
            result = eval_expression(equations[out], env)
            out_bits.append(str(result))

        if "1" in out_bits:  # at least one output active
            inp_pattern = "".join(str(v) for v in values)
            pla.cubes.append((inp_pattern, "".join(out_bits)))

    return pla


def write_pla_file(pla: PLA, filename: str):
    with open(filename, "w") as f:
        f.write(f".i {pla.num_inputs}\n")
        f.write(f".o {pla.num_outputs}\n")
        f.write(".ilb " + " ".join(pla.input_labels) + "\n")
        f.write(".ob " + " ".join(pla.output_labels) + "\n")
        for inp, outp in pla.cubes:
            f.write(inp + " " + outp + "\n")
        f.write(".e\n")


# -------------------------- 
# Example Run 
# --------------------------
if __name__ == "__main__":
    text_file = "inputs/example_expr.txt"
    pla = sop_to_pla(text_file)
    write_pla_file(pla, "outputs/from_text.pla")
    print("✅ Converted text -> PLA written to outputs/from_text.pla")
