from datetime import date, timedelta
from itertools import count, compress, permutations
from functools import reduce
from operator import mul


# ---------------------------------------------------------------------------

def rotate(length, position, my_list):
    return my_list[length - position: length] + my_list[:length - position]


print(rotate(8, 4, [1, 2, 3, 4, 5, 6, 7, 8]))

# ---------------------------------------------------------------------------

surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
    print(surname)

people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
for person, age in zip(people, ages):
    print(person, age)

# ---------------------------------------------------------------------------

n = 24
remainders = []
while n > 0:
    remainder = n % 2
    remainders.append(remainder)
    n //= 2

remainders = remainders[::-1]
print(remainders)

# ---------------------------------------------------------------------------

today = date.today()
tomorrow = today + timedelta(days=1)
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20}
]
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8
    print(
        'Price for sku', product['sku'],
        'is now', product['price'])

# ---------------------------------------------------------------------------

items = [0, None, 0.0, True, 0, 7]
found = False
for item in items:
    print('scanning item', item)
    if item:
        found = True
        break

if found:
    print("Algo es verdad")
else:
    print('All items evaluate to False')


# ---------------------------------------------------------------------------

class DriverException(Exception):
    pass


people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
driver = None
for person, age in people:
    driver = (person, age)
    break
else:
    raise DriverException('Driver not found')

# ---------------------------------------------------------------------------

primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

# ---------------------------------------------------------------------------

customers = [
    dict(id=1, total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='P30'),
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
]
for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])

# ---------------------------------------------------------------------------
# Infinite counters... nice!

for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')

# ---------------------------------------------------------------------------

data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

# ---------------------------------------------------------------------------

print(list(permutations('ABC')))


# ---------------------------------------------------------------------------

def outer():
    test3 = 1

    def inner():
        test2 = 2
        print('inner:', test2)

    inner()
    print('outer', test3)


test = 0
outer()
print('global:', test)


# ---------------------------------------------------------------------------

def minimum(*n1):
    print(n1)
    if n1:
        mn = n1[0]
        for value in n1[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)


# ---------------------------------------------------------------------------

def func(*args):
    print(args)


values = (1, 2, 3, -7, 9)
func(values)
func(*values)


# ---------------------------------------------------------------------------

def func(**kwargs):
    print(kwargs)


func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))


# ---------------------------------------------------------------------------


def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', '')
    }
    print(conn_params)


connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')


# ---------------------------------------------------------------------------


def factorial(n2):
    if n2 in (0, 1):
        return 1
    result = n2
    for k in range(2, n2):
        result *= k

f5 = factorial(5)


def factorial_fun(m):
    return reduce(mul, range(1, m + 1), 1)

f_5 = factorial_fun(5)
