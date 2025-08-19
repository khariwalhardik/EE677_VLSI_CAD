import re
import json
import os

def parse_vhdl_netlist(file_path, out_path):
    with open(file_path, "r") as f:
        text = f.read()

    # Entity name
    entity_match = re.search(r'entity\s+(\w+)', text, re.IGNORECASE)
    entity_name = entity_match.group(1) if entity_match else "unknown"

    # Ports
    ports = re.findall(r'(\w+)\s*:\s*(in|out)\s+STD_LOGIC', text, re.IGNORECASE)
    primary_inputs = [p[0] for p in ports if p[1].lower() == "in"]
    primary_outputs = [p[0] for p in ports if p[1].lower() == "out"]

    # Internal signals
    signals = re.findall(r'signal\s+(.*?)\s*:', text, re.IGNORECASE)
    internal_signals = [s.strip() for line in signals for s in line.split(',')]

    # Gates (instances)
    gate_pattern = re.compile(r'(\w+)\s*:\s*(\w+)\s+port\s+map\s*\((.*?)\);', re.IGNORECASE)
    gates = []
    for match in gate_pattern.finditer(text):
        name, gtype, conn_str = match.groups()
        conns = [c.strip() for c in conn_str.split(',')]
        inputs, outputs = conns[:-1], [conns[-1]]
        gates.append({
            "name": name,
            "type": gtype.replace("_gate", "").upper(),
            "inputs": inputs,
            "outputs": outputs
        })

    # JSON object
    result = {
        "entity": entity_name,
        "primary_inputs": primary_inputs,
        "primary_outputs": primary_outputs,
        "internal_signals": internal_signals,
        "gates": gates
    }

    # ✅ Ensure output directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Save JSON
    with open(out_path, "w") as f:
        json.dump(result, f, indent=4)
    print(f"Parsed VHDL netlist saved to {out_path}")


# # Example usage
# input_file = "gate_level_netlist"
# parse_vhdl_netlist(f'{input_file}.vhdl', f'{input_file}.json')
