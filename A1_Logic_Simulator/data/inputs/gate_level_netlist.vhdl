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
