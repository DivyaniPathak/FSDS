import logging
logging.basicConfig(filename="OOPSTASK3.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class FSDS:
    try:
        def intern(self):
            logging.info("this FSDS course has 1 year internship available")
    except Exception as e:
        logging.error(e)

class DataAnalytics:
    try:
        def intern(self):
            logging.info("this DA course has not 1 year internship available")
    except Exception as e:
        logging.error(e)

#driving code
def internship(a):
    a.intern()

DS=FSDS()
DA=DataAnalytics()

internship(DS)
internship(DA)