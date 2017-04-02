# Primes problem

to_factorise = 600851475143
biggest_factor = 1
current_factor = 1

while to_factorise > 1:
    current_factor += 1
    if to_factorise % current_factor == 0:
        to_factorise = to_factorise / current_factor
        if current_factor > biggest_factor:
            biggest_factor = current_factor
        current_factor = 1

print(biggest_factor)


