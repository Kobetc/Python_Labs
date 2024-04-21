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
                (SELECT name FROM Employer WHERE Applicant.employer_id  = Employer.id), 
                (SELECT companyName FROM Employer WHERE Applicant.employer_id  = Employer.id), 
                (SELECT name FROM Recruiter WHERE Applicant.recruiter_id  = Recruiter.id) 
            FROM Applicant"""
    )

    applicants = ET.SubElement(parentElement, 'applicants')

    for row in cursor.fetchall():

        applicant = ET.SubElement(applicants, 'applicant')

        ET.SubElement(applicant, "id", id=str(row[0]))
        ET.SubElement(applicant, "name", name=str(row[1]))
        ET.SubElement(applicant, "experience", experience=str(row[2]))
        ET.SubElement(applicant, "employerName", employerName=str(row[3]))
        ET.SubElement(applicant, "companyName", companyName=str(row[4]))
        ET.SubElement(applicant, "recruiterName", recruiterName=str(row[5]))

    ET.dump(parentElement)

    tree = ET.ElementTree(parentElement)
    tree.write(xmlFile, encoding='utf-8', xml_declaration=True)

    xmlFile.close()
