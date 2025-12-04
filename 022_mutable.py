# mutable example - value itself changes
spice_mix = set()
print(f"Initial spice mix ID: {id(spice_mix)}")

spice_mix.add("Ginger")
print(f"spice mix id now: {id(spice_mix)}")

spice_mix.add("Cardamom")
print(f"spice mix id now: {id(spice_mix)}")

# immutable example - value doesn't change, only the reference changes
sugar_amount = 2
print(f"ID for 2: {id(sugar_amount)}")
print(f"ID for 2: {id(2)}")

sugar_amount = 12
print(f"ID now for 12: {id(sugar_amount)}")
print(f"ID for 12: {id(12)}")