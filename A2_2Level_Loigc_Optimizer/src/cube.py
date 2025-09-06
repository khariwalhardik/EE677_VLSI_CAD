class Cube:
    """
    Represents a Boolean cube (product term) in SOP form.
    Example:
        "110"  -> a=1, b=1, c=0
        "11-"  -> a=1, b=1, c=don't care
    """

    def __init__(self, pattern: str):
        self.pattern = pattern  # string of '0','1','-'

    def __repr__(self):
        return f"Cube({self.pattern})"

    # ------------------------------------------------------------
    # Count the number of literals in the cube
    # e.g. "11-" has 2 literals (a=1, b=1, c=don't care)
    # ------------------------------------------------------------
    def literal_count(self) -> int:
        return sum(1 for ch in self.pattern if ch != "-")

    # ------------------------------------------------------------
    # Check if this cube covers a minterm
    # A cube covers a minterm if all its fixed bits match
    # Example: Cube("1-0") covers minterm "100" and "110"
    # ------------------------------------------------------------
    def covers(self, minterm: str) -> bool:
        if len(minterm) != len(self.pattern):
            raise ValueError("Minterm and cube must have same length")
        return all(c == "-" or c == m for c, m in zip(self.pattern, minterm))

    # ------------------------------------------------------------
    # Try to merge with another cube
    # Merge possible if they differ in exactly 1 position
    # Example: "110" + "111" -> "11-"
    # Returns a new Cube if merge is possible, else None
    # ------------------------------------------------------------
    def merge(self, other: "Cube"):
        if len(self.pattern) != len(other.pattern):
            raise ValueError("Cubes must have same length to merge")

        diffs = 0
        merged = []
        for c1, c2 in zip(self.pattern, other.pattern):
            if c1 == c2:
                merged.append(c1)
            else:
                diffs += 1
                merged.append("-")
            if diffs > 1:
                return None  # can't merge

        if diffs == 1:
            return Cube("".join(merged))
        return None

    # ------------------------------------------------------------
    # Check if this cube absorbs another cube
    # A absorbs B if every minterm of B is also covered by A
    # Equivalent to: for each position, either same or A='-'
    # Example: Cube("1-0") absorbs Cube("110")
    # ------------------------------------------------------------
    def absorbs(self, other: "Cube") -> bool:
        if len(self.pattern) != len(other.pattern):
            raise ValueError("Cubes must have same length to compare")
        return all(c1 == "-" or c1 == c2 for c1, c2 in zip(self.pattern, other.pattern))


if __name__ == "__main__":
    c1 = Cube("110")
    c2 = Cube("111")
    merged = c1.merge(c2)

    print("Cube1:", c1)
    print("Cube2:", c2)
    print("Merged:", merged)

    print("Literal count of", c1, "=", c1.literal_count())
    print("Does", c1, "cover 110?", c1.covers("110"))
    print("Does", c1, "cover 010?", c1.covers("010"))
    print("Does", Cube("1-0"), "absorb", Cube("110"), "?", Cube("1-0").absorbs(Cube("110")))
