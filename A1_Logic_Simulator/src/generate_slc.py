import json

def generate_expression(json_file, out_file):
    # Load JSON into Python dict
    with open(json_file, "r") as f:
        netlist_json = json.load(f)

    op_map = {
        "AND": "({} & {})",
        "OR":  "({} | {})",
        "XOR": "({} ^ {})",
        "NOT": "(~{})"
    }

    # Build lookup table: output_signal -> gate
    gate_map = {node["outputs"][0]: node for node in netlist_json["gates"]}

    def expand(signal):
        # If signal is primary input, return as-is
        if signal in netlist_json["primary_inputs"]:
            return signal
        # Otherwise expand via its producing gate
        gate = gate_map[signal]
        if gate["type"] == "NOT":
            return op_map["NOT"].format(expand(gate["inputs"][0]))
        elif gate["type"] in ("AND", "OR", "XOR"):
            return op_map[gate["type"]].format(expand(gate["inputs"][0]), expand(gate["inputs"][1]))
        else:
            raise ValueError(f"Unknown gate type: {gate['type']}")

    # Handle multiple outputs
    output_expressions = {}
    for output_signal in netlist_json["primary_outputs"]:
        output_expressions[output_signal] = expand(output_signal)

    # Save to file
    with open(out_file, "w") as f:
        for name, expr in output_expressions.items():
            f.write(f"{name} = {expr}\n")

    return output_expressions


# # Example usage
# if __name__ == "__main__":
#     input_file = "gate_level_netlist"
#     expr = generate_expression(f'{input_file}.json', f'{input_file}_slc.txt')
#     print("Generated Expression:", expr)

