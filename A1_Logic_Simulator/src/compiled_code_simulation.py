import ast
import operator

# Define safe operators
ops = {
    ast.BitAnd: operator.and_,
    ast.BitOr: operator.or_,
    ast.Invert: operator.inv
}

def safe_eval(expr, variables):
    """
    Safely evaluate a boolean expression using AST
    expr: string e.g. '(a & (~sel)) | (b & sel)'
    variables: dict {'a':0, 'b':1, 'sel':0}
    """
    node = ast.parse(expr, mode='eval').body

    def _eval(node):
        if isinstance(node, ast.Name):
            return variables[node.id]
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Invert):
            return 1 - _eval(node.operand)  # handle ~ as NOT (binary logic)
        elif isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.BitAnd):
                return _eval(node.left) & _eval(node.right)
            elif isinstance(node.op, ast.BitOr):
                return _eval(node.left) | _eval(node.right)
        raise ValueError("Unsupported expression")

    return _eval(node)

def process_files(expr_file, input_file, output_file):
    # Load boolean expression
    with open(expr_file, "r") as f:
        expr = f.read().strip()

    # Read inputs
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    headers = lines[0].split()
    input_rows = [line.split() for line in lines[1:]]

    results = []

    for row in input_rows:
        variables = {headers[i]: int(row[i]) for i in range(len(headers))}
        out_val = safe_eval(expr, variables)
        results.append(str(out_val))

    # Write outputs only
    with open(output_file, "w") as f:
        f.write("OUTPUT\n")
        for r in results:
            f.write(r + "\n")


# # Example usage
# if __name__ == "__main__":
#     process_files("gate_level_netlist_slc.txt", "inputs.txt", "outputs.txt")
#     print("Processed files successfully.")