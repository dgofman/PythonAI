
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
    print(i, num)

numbers = [4, 2, 1, 6, 9, 7]
def square(x):
    return x*x

print(list(map(square, numbers)))

numbers = [4, 2, 1, 6, 9, 7]
def is_odd(x):
    return bool(x % 2)

print(list(filter(is_odd, numbers)))

print([x for x in numbers if is_odd(x)])

def get_name_and_decades(name, age):
    print("My name is {} and I'm {:.5f} decades old.".format(name, age / 10))
    print(f"My name is {name} and I'm {age / 10:.5f} decades old.")

get_name_and_decades("Maria", 31)


print(sorted([6,5,3,7,2,4,1]))

print(sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True))

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
print(sorted(animals, key=lambda animal: animal['age']))


import random
all_words = "all the words in the world".split()
def get_random_word():
    return random.choice(all_words)

def get_unique_words():
    words = set()
    for _ in range(1000):
        words.add(get_random_word())
    return words
print(get_unique_words())


print(sum(i for i in range(1, 4)))
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
print(cowboy.get('name', 'The Man with No Name'))
print(cowboy.setdefault('name', 'The Man with No Name'))

from collections import defaultdict
student_grades = defaultdict(list)
grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]
for name, grade in grades:
    student_grades[name].append(grade)
print(student_grades)

from collections import Counter
words = "if there was there was but if there was not there was not".split()
print(Counter(words))


def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index + 1]
    yield weekdays[index + 2]
day = testgen(0)
print(next(day), next(day))
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([(x,weekdays.count(x)) for x in set(weekdays)])