import logging
logging.basicConfig(filename="OOPSTASK1.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class ineuron_stu:
    try:
        def __init__(self,name,id,ph_no,email_id):
            self.name=name
            self.id=id
            self.ph_no=ph_no
            self.email_id=email_id

        def show_details(self):
            logging.info(f"ineuron student details are : NAME is {self.name} , ID is {self.id}, contact_NO is {self.ph_no} , and mail_id is {self.email_id} ")

    except Exception as e:
        logging.error(e)


class Course(ineuron_stu):
    def course_available(self):
        logging.info(" there are N number of courses available at ineuron for student. Please refer Dashboard for more details")

class Internship(Course):

    logging.info("this is MULTI-LEVEL inheritance example")
    def job_gurantee(self):
        logging.info("there is 1 year intership provided in FSDS course")

intsip=Internship("Pathak",505,7878787878,"pathak@ineurom.ai")
intsip.show_details()
intsip.course_available()
intsip.job_gurantee()

######################################################################################################################

class ineuron_Engineer():

    __salary="15L"

    try:
        def show_salary(self):
            logging.info("Engineer salary is equal to %s", ineuron_Engineer.__salary)

        def engineer_details(self):
            logging.info(f"Engineer section details are : UNIT is 'OPS' and technology is 'Python'")

    except Exception as e:
        logging.error(e)



class ineuron_Architech():

    __salary="30L"

    try:
        def show_salary(self):
            logging.info("Architech salary is equal to %s", ineuron_Architech.__salary)

        def arch_details(self):
            logging.info(f"Architech section details are : UNIT is GLOBAL, and technology is DATA SCIENCE")

    except Exception as e:
        logging.error(e)


class Job_referall(ineuron_Engineer,ineuron_Architech):

    logging.info("this is multiple level inheritance example")
    def open_position(self):
        logging.info("In ineuron, there are openings available for Eng and architech")

JR=Job_referall()
JR.show_salary()
JR.engineer_details()
JR.arch_details()


