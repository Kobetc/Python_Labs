import sqlite3
import xml.etree.ElementTree as ET


def import_to_xml():

    connection = sqlite3.connect('.sqlite3')
    cursor = connection.cursor()

    tree = ET.parse("main.xml")
    root = tree.getroot()

    applicants = []

    for child in root[0]:

        name = child.get('name')
        experience = int(child.get('experience')) if child.get(
            'experience') != 'None' else None
        recruiter_id = int(child.get('recruiter_id')) if child.get(
            'recruiter_id') != 'None' else None
        employer_id = int(child.get('employer_id')) if child.get(
            'employer_id') != 'None' else None

        applicants.append((None, name, experience, recruiter_id, employer_id))

    cursor.executemany(
        "INSERT INTO Applicant VALUES(?, ?, ?, ?, ?)", applicants)

    connection.commit()
