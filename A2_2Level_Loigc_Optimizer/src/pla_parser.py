class PLA:
    def __init__(self):
        self.num_inputs = 0
        self.num_outputs = 0
        self.input_labels = []
        self.output_labels = []
        self.cubes = []  # list of tuples (input_pattern, output_pattern)

    def __repr__(self):
        return (f"PLA(inputs={self.num_inputs}, outputs={self.num_outputs}, "
                f"cubes={len(self.cubes)})")


def parse_pla(filename: str) -> PLA:
    pla = PLA()

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # skip comments/empty
                continue

            # Header lines (check full tokens, not just prefix!)
            if line.startswith(".i "):  # number of inputs
                pla.num_inputs = int(line.split()[1])
            elif line.startswith(".o "):  # number of outputs
                pla.num_outputs = int(line.split()[1])
            elif line.startswith(".ilb"):  # input labels
                pla.input_labels = line.split()[1:]
            elif line.startswith(".ob"):  # output labels
                pla.output_labels = line.split()[1:]
            elif line.startswith(".e"):
                break
            else:
                # Cube line: input_pattern output_pattern
                parts = line.split()
                if len(parts) == 2:
                    input_pattern, output_pattern = parts
                    pla.cubes.append((input_pattern, output_pattern))

    return pla


if __name__ == "__main__":
    # quick test
    pla = parse_pla("inputs/example1.pla")
    print(pla)
    print("Inputs:", pla.input_labels)
    print("Outputs:", pla.output_labels)
    print("Cubes:")
    for cube in pla.cubes:
        print("  ", cube)
