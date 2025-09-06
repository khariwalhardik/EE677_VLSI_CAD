# Problem statement (plain language)

Design and implement a **heuristic 2-level circuit optimizer** that, given a Boolean function (single- or multi-output) described as minterms / PLA / truth table (with optional don’t-care minterms), produces a near-minimal 2-level logic network (SOP or POS). Your optimizer must be an original implementation of a heuristic algorithm (Quine–McCluskey/ Espresso–style ideas are fine), not simply a wrapper that calls Espresso to do the work. You may use Espresso only as a **reference** tool to benchmark results.

# Formal inputs & outputs

**Inputs**

* Number of variables `n`.
* ON-set `F` = set of minterms that must be 1.
* DON’T-CARE set `D` (optional) = minterms that can be treated as either 0 or 1 when simplifying.
* OFF-set `R` is implicitly all `2^n` minterms not in `F ∪ D`.
* Format: PLA (`.pla`) is recommended; truth table / list of minterms is acceptable if stated.

**Outputs**

* A 2-level representation in SOP (sum-of-products) or POS (product-of-sums). Example SOP: `f = a'b + ac + d`.
* Optionally: write result back to `.pla`.
* Report metrics: literal count, number of product terms, and (optionally) estimated area metric for multi-output shared terms.

# Objective (what “minimize” means)

* Minimize a cost metric (choose one or more):

  * **Literal count** (primary, commonly used in VLSI).
  * **Number of product terms** (secondary).
  * For multi-output: favor **shared implicants** (count once).
* Maintain correctness: every minterm in `F` must be covered; no minterm in `R` may be covered by any selected implicant.

# Constraints & correctness conditions

* **Soundness**: final cover must cover every `F` minterm.
* **Safety**: no selected cube may cover any `R` minterm. (A candidate cube may cover `D` minterms.)
* Heuristic methods are allowed — exact optimum is not required (problem is NP-hard).
* You must document algorithm design and justify heuristic choices.

# Key definitions (formal)

* **Minterm**: an `n`-bit vector of `0/1` (e.g. `0101`) representing a single input combination.
* **Cube / implicant**: a vector over `{0,1,-}` where `-` means “don’t care” in that variable (example `1-0`).
* **Prime implicant**: an implicant that cannot be further generalized (turned more `-`) without covering an OFF minterm.
* **Essential implicant**: a prime implicant that is the only implicant covering some ON minterm.
* **Cover**: set of implicants whose union covers all ON minterms.

# High-level algorithmic tasks you must implement

1. **Parser** — read PLA / minterm list and produce `F`, `D`, `n`.
2. **Cube representation & utilities** — cover test, literal count, merge two cubes, equality, hashing.
3. **Prime implicant generation** — iterative pairwise merging (Quine–McCluskey style) but implement it heuristically and efficiently:

   * Start with `F ∪ D`.
   * Iteratively merge pairs that differ in exactly one position to produce more general cubes.
   * Keep track of “merged” vs “unmerged” cubes to extract prime candidates.
   * After merging, remove any prime that covers an OFF minterm `R`.
4. **Essential implicant identification** — map ON minterms → set of primes covering them; any prime that is unique for a minterm is essential.
5. **Heuristic set-cover** — choose remaining primes to cover uncovered ON minterms:

   * Greedy scoring: e.g. maximize `newly_covered / literal_cost` (or `newly_covered / literal_cost^α`).
   * Tie-breakers: fewest literals, fewer extra coverage, or randomization for repeated trials.
6. **Cleanup / local optimization**:

   * Absorption: remove cubes subsumed by others.
   * Literal reduction: attempt to drop literals from a cube if `F` remains fully covered and no `R` is covered.
   * Optional small local search (try replacing two cubes with one, etc.).
7. **Multi-output extension**:

   * Build global candidate set from union of all outputs’ `F ∪ D`.
   * Perform per-output covering but allow sharing of implicants (count shared ones once).
8. **Output writer & validation** — write SOP/PLA and validate coverage and safety automatically.

# Example — step-by-step (small, concrete)

Variables: `a b c` (n=3)
ON-set `F` = { `001`, `011`, `111` }
D-set `D` = { `101` }
OFF-set `R` = all other 3-bit minterms not in `F ∪ D`.

Start cubes (F ∪ D): `001`, `011`, `111`, `101`.

Merging:

* `001` & `011` differ in `b` → merge → `0-1` (covers `001`, `011`).
* `101` & `111` differ in `b` → merge → `1-1` (covers `101`, `111`).
* `0-1` & `1-1` differ in `a` → merge → `--1` (covers `001`, `011`, `101`, `111`).

`--1` is a candidate cube. It covers `D` and all `F`. Check `R`: if `--1` covers any OFF minterm (not in `F ∪ D`), it’s invalid. In this case, all minterms with `c=1` are either in `F` or `D`, so `--1` is valid → final SOP is just `c`. That’s the idea: merging using `D` may enable larger generalizations.

# Heuristic choices & scoring

* Score examples:

  * `score(c) = newly_covered(c, U) / literal_cost(c)` (simple).
  * `score(c) = newly_covered(c, U) / (literal_cost(c)**α)` with tunable `α` (e.g. α = 1).
  * You can also include a length penalty or reward sharing for multi-output.
* Greedy is fast and simple, but you should discuss limitations (not globally optimal).

# Complexity & implementation notes

* Naïve pairwise merging is O(k²) per iteration where k is #cubes — prune aggressively.
* Use bitwise encodings and integer masks for speed (store cube as a bitmask with a separate mask of which bits are “care” vs “don’t care”).
* For moderate `n` (≤ 12) and small minterm lists, Python is fine. For larger scale, C++ or optimized data structures help.

# Testing & validation (what to include in your assignment)

* **Unit tests** for: parsing, cover test, merge correctness, prime extraction, essential detection, greedy cover.
* **Benchmark cases**:

  * Small hand-crafted functions (2–5 vars) — verify by K-map.
  * Random functions (vary ON-set density and D-set size).
  * A few standard small PLAs if available.
* **Comparison**: run Espresso as reference; report literal count and product term count for both your solver and Espresso.
* **Metrics to report**: #variables, |F|, |D|, #primes generated, #terms in final cover, literal count, runtime.

# Deliverables (recommended)

* Source code with CLI: `optimize.py -i input.pla -o out.pla --metric literals`
* README explaining compilation/running steps.
* Test suite and sample PLAs.
* Report: problem statement, algorithm, heuristics chosen, experiments (tables + graphs), discussion (failure cases), conclusions.
* (Optional) scripts to compare with Espresso and generate plots.

# Common pitfalls to avoid

* Allowing implicants that cover OFF minterms (must check safety).
* Not using D properly (D can be used to merge, but final cubes must still be safe).
* Ignoring multi-output sharing (big missed area savings).
* Returning a solution that’s syntactically minimal in terms of number of terms but has a much higher literal count — report both.


