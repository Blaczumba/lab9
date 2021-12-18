from datetime import date


class Person:
    def __init__(self, id=None, name=None, birth_date=None, father=None, mother=None):
        self._id = id
        self._name = name
        self._birth_date = date.fromisoformat(birth_date)
        self._mother = mother
        self._father = father
        if mother is not None:
            mom_children = mother.children()
            mom_children.append(self)
        if father is not None:
            father_children = father.children()
            father_children.append(self)
        self._children = []

    def set_father(self, person):
        if person is None:
            return
        self._father = person
        father_children = person.children()
        if self not in father_children:
            father_children.append(self)

    def set_mother(self, person):
        if person is None:
            return
        self._mother = person
        mother_children = person.children()
        if self not in mother_children:
            mother_children.append(self)

    def id(self):
        return self._id

    def name(self):
        return self._name

    def birth_date(self):
        return self._birth_date

    def mother(self):
        return self._mother

    def father(self):
        return self._father

    def children(self):
        return self._children


class Database:
    def __init__(self, people=None):
        self._list_of_id = []
        self._people = []
        if people is not None:
            for human in people:
                self.add_person(human)

    def add_person(self, person):
        self._people.append(person)
        self._list_of_id.append(person.id())

    def get_person_by_id(self, id):
        for person in self._people:
            if person.id() == id:
                return person

    def people(self):
        return self._people

    def list_of_id(self):
        return self._list_of_id
