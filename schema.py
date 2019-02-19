from collections import OrderedDict

from pyignite import Client, GenericObjectMeta
from pyignite.datatypes import *


class SimilarProduct(metaclass=GenericObjectMeta, schema=OrderedDict([
        ('first_name', String),
        ('last_name', String),
        ('age', IntObject),
])):
    pass


client = Client()
client.connect('localhost', 10800)

person_cache = client.get_or_create_cache('person')

person_cache.put(
        1, Person(first_name='Ivan', last_name='Ivanov', age=33)
)

person = person_cache.get(1)
print(person.__class__.__name__)
# Person

print(person.__class__ is Person)
# True if `Person` was registered automatically (on writing)
# or manually (using `client.register_binary_type()` method).
# False otherwise

print(person)
# Person(first_name='Ivan', last_name='Ivanov', age=33, version=1)

client.register_binary_type(Person)

Person = person.__class__
