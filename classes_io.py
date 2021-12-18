from classes import Person, Database

import csv


class MalformedCSVError(Exception):
    def __init__(self):
        super().__init__("Blad")


class CSVDataError(Exception):
    pass


def read_database_from_file(file_handle):
    reader = csv.DictReader(file_handle)
    people = []
    for row in reader:
        try:
            id = row["id"]
            name = row["name"]
            birth_date = row["birth_date"]
        except KeyError:
            raise MalformedCSVError
        me = Person(id, name, birth_date)
        people.append(me)
    data = Database(people)
    file_handle.seek(0)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        my_id = row["id"]
        father_id = row["father_id"]
        mother_id = row["mother_id"]
        cond1 = father_id not in data.list_of_id()
        cond2 = mother_id not in data.list_of_id()
        if (cond1 or cond2) and mother_id != '' and father_id != '':
            raise CSVDataError
        father = data.get_person_by_id(father_id)
        mother = data.get_person_by_id(mother_id)
        me = data.get_person_by_id(my_id)
        me.set_mother(mother)
        me.set_father(father)
    return data


def write_database_to_file(file_handle, database):
    writer = csv.DictWriter(file_handle, ["id", "name", "birth_date", "father_id", "mother_id"])
    writer.writeheader()
    for person in database.people():
        id = person.id()
        name = person.name()
        birth_date = person.birth_date()
        father_id = person.father_id
