class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self  # регистрируем в реестре


def create_person_list(people: list[dict]) -> list[Person]:
    # На случай многократных вызовов — очищаем реестр
    Person.people.clear()

    instances: list[Person] = []

    # Проход 1: создаём объекты Person (без супругов)
    for d in people:
        instances.append(Person(d["name"], d["age"]))

    # Проход 2: проставляем ссылки супругов (атрибут создаём только если значение не None)
    for d in people:
        p = Person.people[d["name"]]
        if "wife" in d and d["wife"] is not None:
            p.wife = Person.people[d["wife"]]          # type: ignore[attr-defined]
        if "husband" in d and d["husband"] is not None:
            p.husband = Person.people[d["husband"]]    # type: ignore[attr-defined]

    return instances
