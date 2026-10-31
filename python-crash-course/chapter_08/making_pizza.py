import pizzas

pizzas.make_pizza(16, 'pepperoni')
pizzas.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

from pizzas import make_pizza

pizzas.make_pizza(16, 'pepperoni')
pizzas.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

from pizzas import make_pizza as mp
