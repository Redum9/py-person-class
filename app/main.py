class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    instances = [Person(d["name"], d["age"]) for d in people]

    for d in people:
        p = Person.people[d["name"]]
        if "wife" in d and d["wife"] is not None:
            p.wife = Person.people[d["wife"]]
        if "husband" in d and d["husband"] is not None:
            p.husband = Person.people[d["husband"]]
    return instances
