'''for i in range(1, 3):
    for j in range(60, -5):
        print(f"I={i} J={j}")

i = 1
j = 60

while j >=0:
    print(f"I={i} j={j}")
    i += 3
    j -= 5


for i in range(0.0, 2.0, 0.2):
    for j in range(1.0, 6.0):
        print(f"I={i} J={j}")

'''

i = 0.0
while i < 2.0:
    j = 1.0
    while j < 4.0:
        print(f"I={i:.1f} J={j:.1f}")
        j += 1.2
    i += 0.2
