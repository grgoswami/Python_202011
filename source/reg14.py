
families = [
    ('Gorde', 4),
    ('Jain', 4),
    ('Hong', 6),
    ('Wu', 4),
    ('Ouyang', 3),
    ('Sharma', 4)
    ]

print(families)
print(families[0])
print(families[0][0])
print(families[0][0][0])

print(families[2][1])

Fri_group = []
Sat_group = []
Sun_group = []
for family in families:
    print(family)
    first_char = family[0][0]
    if first_char >= 'A' and first_char <= 'G':
        # this will capture last names between A and G
        if family[1] <= 3:
            Fri_group.append(family)
        else:
            Sat_group.append(family)
    elif first_char <= 'R':
        # this will capture last names between H and R
        if family[1] <= 4:
            Sat_group.append(family)
        else:
            Sun_group.append(family)
    else:
        # this will capture last names between S and Z
        Sun_group.append(family)
        
print(Fri_group)
print(Sat_group)
print(Sun_group)

# The following are called list comprehensions
odds = [it for it in range(10) if (it % 2) == 1]
print(odds)

evens = [it for it in range(10) if (it % 2) == 0]
print(evens)

