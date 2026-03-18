import random

random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))



print(random.randint(1, 100))
print(random.randint(1, 100))



# seeded generator
rng_seeded = random.Random(42)

print(rng_seeded.randint(1, 100))
print(rng_seeded.randint(1, 100))

# unseeded (system random)
rng_true = random.Random()

print(rng_true.randint(1, 100))
print(rng_true.randint(1, 100))