import logging
logging.basicConfig(filename="OOPSTASK2.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')


class ineuron:
    try:
        logging.info(" THIS IS ABSTRACT and ENCAPSULATION CONCEPT OF OOPS")

        _company_location='Banglore'
        timing_for_support='AM to PM'
        __companylogo="NO shortcut to success"

        def __init__(self,name,id,city,ph_no,email_id,salary,enrolled_course):
            self.name=name
            self._id=id #protected var
            self.city=city
            self.ph_no=ph_no
            self.email_id=email_id
            self.__salary=salary #private var
            self.enrolled_course=enrolled_course

        def e_details(self):
            logging.info(f"ineuron student details are : NAME is {self.name} , ID is {self._id}, contact_NO is {self.ph_no} ,mail_id is {self.email_id} and  City is {self.city}")

        def enrol_course(self):
            logging.info("enrolled course of student is %s", self.enrolled_course)

        def course_available(self):
            logging.info("Available courses are 1. FSDS 2. DA 3. Basic JAVA 4. BAsic python etc")

        def company_tagline(self):
            logging.info("Company Logo is %s", self.__companylogo)

        def modify_company_tagline(self,newlogo):
            logging.info("Implementing the concept of ENCAPSULATION")
            self.__companylogo = newlogo
            logging.info("Company Logo has been changed")

        def support_timing(self):
            logging.info("Ineuron supports is %s", self.timing_for_support)

        def comp_location(self):
            logging.info("Ineuron office is located at %s", self._company_location)

        def getsalary(self):
            logging.info("Implementing the concept of abstraction")
            logging.info("Employee salary is %s", self.__salary)

        def modifysalary(self,new_salary):
            logging.info("Implementing the concept of ENCAPSULATION")
            self.__salary = new_salary
            logging.info("Salary has been modified")

    except Exception as e:
        logging.error(e)

iern=ineuron("divyani",101,"katni",4545454545,"divyani.pathak@gmail.com","15L","FSDS")
iern.e_details()
iern.course_available()
iern.enrol_course()
iern.getsalary()
iern.modifysalary("20L")
iern.getsalary()

iern.support_timing()
iern.comp_location()
iern.company_tagline()
iern.modify_company_tagline("Hardwork is key to success")
iern.company_tagline()



