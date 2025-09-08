from .pla_parser import parse_pla


def pla_to_sop_text_multi(filename):
    pla = parse_pla(filename)
    inputs = pla.input_labels
    outputs = pla.output_labels
    sop_dict = {out: [] for out in outputs}

    for in_pat, out_pat in pla.cubes:
        for j, bit in enumerate(out_pat):
            if bit == '1':
                term = []
                for i, ch in enumerate(in_pat):
                    if ch == '1':
                        term.append(inputs[i])
                    elif ch == '0':
                        term.append("~" + inputs[i])
                if term:
                    sop_dict[outputs[j]].append("(" + " & ".join(term) + ")")

    lines = []
    lines.append("inputs: " + " ".join(inputs))
    lines.append("outputs: " + " ".join(outputs))
    for out in outputs:
        if sop_dict[out]:
            lines.append(f"{out} = " + " | ".join(sop_dict[out]))
        else:
            lines.append(f"{out} = 0")  # no terms → constant 0

    return "\n".join(lines)


if __name__ == "__main__":
    input_file_name = input("Enter the input PLA file name (from outputs/pla/, without extension): ")
    filename = f'outputs/pla/{input_file_name}.pla'
    sop_text = pla_to_sop_text_multi(filename)
    print(sop_text)
    with open(f'outputs/txt/{input_file_name}_sop.txt', "w") as f:
        f.write(sop_text)
