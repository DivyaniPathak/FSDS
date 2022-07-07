import logging
logging.basicConfig(filename="AllDataTypeTASK.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class AllDataType_C:

    def __init__(self,ad):
        self.ad=ad

    def extractlist(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.3) Try to extract all the list entity")
            op=[]
            for i in self.ad:
                if type(i)==list:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)


    def extractdict(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.4) Try to extract all the dict entity")
            op=[]
            for i in self.ad:
                if type(i)==dict:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def extracttupple(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.4) Try to extract all the tuple entity")
            op=[]
            for i in self.ad:
                if type(i)==tuple:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def extractNumericData(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.6) Try to extract all the Numeric data it may be a part of dict key and values.")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                        if type(var)==int:
                            op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int:
                            op.append(k)
                        if type(v)==int:
                            op.append(v)
                elif type(i)==int:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def sumNumericData(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.7) Try to give summation of all the numeric data.")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                        if type(var)==int:
                            op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int:
                            op.append(k)
                        if type(v)==int:
                            op.append(v)
                elif type(i)==int:
                    op.append(i)
            sum=0
            for s in op:
                sum=sum+s
            logging.info("the output is %s", sum)
        except Exception as e:
            logging.error(e)

    def oddNumericDataofList(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.8) Try to filter out all the odd values out all numeric datawhich is a part of a list.")
            op=[]
            for i in self.ad:
                if type(i)==list:
                    if i%2 != 0:
                        op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def extract_ineuron(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.9 Try to extract 'ineuron' out of this dataset.")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                        if type(var)==str:
                            if var == "ineuron":
                                op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            if k == "ineuron":
                                op.append(k)
                        if type(v)==str:
                            if v == "ineuron":
                                op.append(v)
                elif type(i)==str:
                    if i == "ineuron":
                        op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)



    def occuranceOfData(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.10) Try to find out a number of occurance of all the data.")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                       op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        op.append(k)
                        op.append(v)
                elif type(i)==int or type(i)==str:
                    op.append(i)
            occu_data=[]
            for occu in op:
                occu.append(occu,count(occu))
            logging.info("the output is %s", occu_data)
        except Exception as e:
            logging.error(e)

    def NoOfKeys(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.11) Try to find out a number of keys in dict element.")
            op=[]
            for i in self.ad:
                if type(i)==dict:
                    for k in i.keys():
                        op.append(k)
            length=len(op)
            logging.info("the output is %s", length)
        except Exception as e:
            logging.error(e)

    def extractStrings(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.12) Try to filter out all the string data.")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                        if type(var)==str:
                            op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            op.append(k)
                        if type(v)==str:
                            op.append(v)
                elif type(i)==str:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)


    def mulNumericData(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.14) Try to find out multiplication of all numeric value in the individual collection inside dataset")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                        if type(var)==int:
                            op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int:
                            op.append(k)
                        if type(v)==int:
                            op.append(v)
                elif type(i)==int:
                    op.append(i)
            mul=1
            for s in op:
                mul=mul*s
            logging.info("the output is %s", mul)
        except Exception as e:
            logging.error(e)

    def flatlist_afterunwrap(self):
        try:
            logging.info("the input data is %s", self.ad)
            logging.info("q.15) Try to unwrape all the collection inside collection and create a flat list.")
            op=[]
            for i in self.ad:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for var in i:
                        if type(var)==str:
                            op.extend(var)
                        if type(var)==int:
                            op.append(var)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            op.extend(k)
                        if type(v)==str:
                            op.extend(v)

                        if type(k) == int:
                            op.append(k)
                        if type(v) == int:
                            op.append(v)
                elif type(i)==str:
                    op.extend(i)
                elif type(i)==int:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)


all_obj = AllDataType_C([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]])
print(all_obj.extractlist())
print(all_obj.extractdict())
print(all_obj.extractlist())

print(all_obj.extracttupple())
print(all_obj.extractNumericData())
print(all_obj.sumNumericData())
print(all_obj.oddNumericDataofList())
print(all_obj.extract_ineuron())
print(all_obj.occuranceOfData())
print(all_obj.NoOfKeys())
print(all_obj.extractStrings())
print(all_obj.mulNumericData())
print(all_obj.flatlist_afterunwrap())

