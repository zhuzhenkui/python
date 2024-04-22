import itertools

def evaluate_expression(p, q, r, s):
    return not ( (p or q) and ((p or r) or s) )
print("p    |  q   | r   |    s   |  ¬(p ∨ q) ∧ ((p ∨ r) ∨ s)")
for p, q, r, s in itertools.product([True, False], repeat=4):
    result = evaluate_expression(p, q, r, s)
    print(f"{p} | {q} | {r} | {s} | {result}")