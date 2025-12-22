branch_a_products = {"bread","milk","butter","jam"}
branch_b_products = {"bread","cheese","butter","ketchup"}

print(branch_a_products)
print(branch_b_products)

union = branch_a_products | branch_b_products
print(union)

print(branch_a_products & branch_b_products)

print(branch_a_products - branch_b_products)

print("ketchup" in branch_a_products)

essential_items = frozenset(["milk","bread","ketchup"])
print(essential_items)