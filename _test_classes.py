from classes import (Person, Database)


def test_person_create_without_family():
    person = Person('1', 'Jan Kowalski', '2000-03-01')

    assert person.id() == '1'
    assert person.name() == 'Jan Kowalski'
    assert person.birth_date() == '2000-03-01'
    assert person.mother() is None
    assert person.father() is None
    assert len(person.children()) == 0


def test_person_create_with_family():
    mother = Person()
    father = Person()

    person = Person('1', 'Jan Kowalski', '2000-03-01', father, mother)

    assert person.id() == '1'
    assert person.name() == 'Jan Kowalski'
    assert person.birth_date() == '2000-03-01'
    assert person.mother() is mother
    assert person.father() is father
    assert len(person.children()) == 0
    assert person in mother.children()
    assert person in father.children()


def test_person_set_father():
    father = Person()
    person = Person()

    person.set_father(father)

    assert person.father() is father
    assert person in father.children()


def test_person_set_mother():
    mother = Person()
    person = Person()

    person.set_mother(mother)

    assert person.mother() is mother
    assert person in mother.children()


def test_database():
    people = [Person('1'), Person('2')]
    database = Database(people)

    assert len(database.people()) == 2
    assert all(person in database.people() for person in people)
    assert database.get_person_by_id('1') is people[0]
    assert database.get_person_by_id('2') is people[1]


def test_database_add_person():
    people = [Person('1'), Person('2')]
    database = Database(people)

    person = Person('3')

    database.add_person(person)

    assert len(database.people()) == 3
    assert person in database.people()
    assert database.get_person_by_id('3') is person
