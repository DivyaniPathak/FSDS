import logging
logging.basicConfig(filename="stringTASK.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class StrC :
    def __init__(self,strIP):
        self.strIP1=strIP

    def extractdata(self):
        try:
            logging.info("The given string is %s", self.strIP1)
            logging.info("1. Try to extract data from index one to index 300 with a jump of 3")
            op = self.strIP1[0:300:3]
            logging.info("The output is %s", op)
        except Exception as e:
            logging.error(e)

    def reverseSTR(self):
        try:
            logging.info("The given string is %s", self.strIP1)
            logging.info("2. Try to reverse a string without using reverse function")

            op = self.strIP1[::-1]
            logging.info("The output is %s", op)
        except Exception as e:
            logging.error(e)
    def splitAFTERupper(self):
        try:
            logging.info("The given string is %s", self.strIP1)
            logging.info("3. Try to split a string after conversion of entire string in uppercase")
            op = self.strIP1.upper().split(" ")
            logging.info("The output is %s", op)
        except Exception as e :
            logging.error(e)

    def convert_to_lower(self):
        try:
            logging.info("The given string is %s", self.strIP1)
            logging.info("4. try to convert the whole string into lower case")
            op = self.strIP1.lower()
            logging.info("The output is %s", op)
        except Exception as e :
            logging.error(e)


    def convert_to_capitalize(self):
        try:
            logging.info("The given string is %s", self.strIP1)
            logging.info("5 . Try to capitalize the whole string")
            op = self.strIP1.capitalize()
            logging.info("The output is %s", op)
        except Exception as e :
            logging.error(e)

    def convert_to_expandtabs(self,str1):
        try:
            logging.info("The given string is %s", str1)
            logging.info("7. Try to give an example of expand tab")
            op = str1.expandtabs()
            logging.info("The output is %s", op)
        except Exception as e :
            logging.error(e)

    def convert_using_strip(self,str1):
        try:
            logging.info("The given string is %s", str1)
            logging.info("8 . Give an example of strip , lstrip and rstrip")
            op1 = str1.strip()
            op2 = str1.lstrip()
            op3 = str1.rstrip()
            logging.info("The output is %s %s %s", op1, op2, op3)
        except Exception as e :
            logging.error(e)

    def convert_using_replace(self,str1):
        try:
            logging.info("The given string is %s", str1)
            logging.info("9. Replace a string charecter by another charector by taking your own example")
            op = str1.replace("Hi","Hello")
            logging.info("The output is %s ", op)
        except Exception as e :
            logging.error(e)




#############################################################Function Call
s1=StrC("this is My First Python programming class and i am learNING python string and its function")
print(s1.extractdata())
print(s1.reverseSTR())
print(s1.splitAFTERupper())
print(s1.convert_to_lower())
print(s1.convert_to_capitalize())
print(s1.convert_to_expandtabs("How\tare\tyou"))
print(s1.convert_using_strip("     Divyani    "))
print(s1.convert_using_replace("Hi Shruti"))



