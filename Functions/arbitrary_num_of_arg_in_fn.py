# let's create a fn that accepts Size and random values like toppings
                    # *args - python treats random/arbitrary arguments like TUPLES
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following tippings:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza(16,"crap 1")
make_pizza(10,"crap 1","crap 2","crap 3","crap 4")