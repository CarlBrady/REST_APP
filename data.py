student_data = {}


def setup():
    from schema import Student

    global student_name_data, student_id_data, student_dob_data

    disco_Stu = Student(
        id="1999",
        name="Disco Stu",
        dob="10/01/1964",
    )
    dob_By = Student(
        id="1998",
        name="Dobby",
        dob="10/01/1964",
    )
    tu_Pac = Student(
        id="1997",
        name="Tupac",
        dob="10/01/1970",
    )
    gerry_Adams = Student(
        id="1996",
        name="Gerry Adams",
        dob="04/12/1958",
    )
    gan_Dalf = Student(
        id="1995",
        name="Gandalf",
        dob="01/01/100",
    )

    student_id_data = {
        "1999" : disco_Stu,
        "1998" : dob_By,
        "1997" : tu_Pac,
        "1996" : gerry_Adams,
        "1995" : gan_Dalf
        }
    student_name_data = {
        "Disco Stu" : disco_Stu,
        "Dobby" : dob_By,
        "Tupac" : tu_Pac,
        "Gerry Adams" : gerry_Adams,
        "Gandalf" : gan_Dalf
        }
    student_dob_data = {
        "10/01/1964" : disco_Stu,
        "10/01/1964" : dob_By,
        "10/01/1970" : tu_Pac,
        "04/12/1958" : gerry_Adams,
        "01/01/100" : gan_Dalf
        }

def get_name(name):
    return student_name_data.get(name)
def get_dob(dob):
    return student_dob_data.get(dob)
def get_id(id):
    return student_id_data.get(id)
