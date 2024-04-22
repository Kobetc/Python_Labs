import sqlite3
import xml.etree.ElementTree as ET


def export_to_xml():

    connection = sqlite3.connect('.sqlite3')
    cursor = connection.cursor()

    xmlFile = open("main.xml", "wb")

    parentElement = ET.Element("root")

    cursor.execute(
        """SELECT 
                id, 
                name, 
                experience, 
                recruiter_id,
                employer_id
            FROM Applicant"""
    )

    applicants = ET.SubElement(parentElement, 'applicants')

    for row in cursor.fetchall():

        ET.SubElement(applicants, 'applicant', {
            "id": str(row[0]),
            "name": str(row[1]),
            "experience": str(row[2]),
            "recruiter_id": str(row[3]),
            "employer_id": str(row[4])
        }
        )

    ET.dump(parentElement)

    tree = ET.ElementTree(parentElement)
    tree.write(xmlFile, encoding='utf-8', xml_declaration=True)

    xmlFile.close()
