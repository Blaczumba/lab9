from classes import Person, Database

import csv


class MalformedCSVError(Exception):
    pass


class CSVDataError(Exception):
    pass


def read_database_from_file(file_handle):
    reader = csv.DictReader(file_handle)
    people = []
    for row in reader:
        id = row["id"]
        name = row["name"]
        birth_date = row["birth_date"]
        me = Person(id, name, birth_date)
        people.append(me)
    data = Database(people)
    file_handle.seek(0)
    for row in reader:
        my_id = row["id"]
        father_id = row["father_id"]
        mother_id = row["mother_id"]
        father = data.get_person_by_id(father_id)
        mother = data.get_person_by_id(mother_id)
        me = data.get_person_by_id(my_id)
        me.set_mother(mother)
        me.set_father(father)
    return data


def write_database_to_file(handle, database):
    pass
