import logging
logging.basicConfig(filename="listTASK.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class list_C:

    def __init__(self,ls):
        self.ls=ls

    def rev_list(self):
        try:
            logging.info("#1 . Try to reverse a list")
            logging.info("the input list is %s", self.ls )
            op=self.ls[::-1]
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)


    def access_234(self):
        try:
            logging.info("#2. try to access 234 out of this list")
            logging.info("the input list is %s", self.ls )
            op = self.ls[7][0]
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def access_234_withloop(self):
        try:
            logging.info("#2. try to access 234 out of this list using loop")
            logging.info("the input list is %s", self.ls )
            op=[]
            for i in self.ls:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for var in i:
                            if var == 234:
                                op.append(var)
                if type(i) == int:
                    if i == 234:
                        op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def access_456(self):
        try:
            logging.info("#2. try to access 456 out of this list")
            logging.info("the input list is %s", self.ls )
            op = self.ls[5][1]
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def access_456_withloop(self):
        try:
            logging.info("#2. try to access 456 out of this list using loop")
            logging.info("the input list is %s", self.ls )
            op=[]
            for i in self.ls:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for var in i:
                            if var == 456:
                                op.append(var)
                if type(i) == int:
                    if i == 456:
                        op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def extract_sublist(self):
        op = []
        try:
            logging.info("#2. try to extract list out of this list")
            logging.info("the input list is %s", self.ls )
            for i in self.ls:
                if type(i)==list:
                    op.append(i)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

class dict_C:

    def __init__(self,dt):
        self.dt=dt

    def extractsudh_usingloop(self):
        try:
            logging.info("#5 . Try to extract 'sudh' using loop")
            logging.info("the input list is %s", self.dt)
            op=[]
            for i in self.dt:
                if type(i)==dict:
                    for v in i.values():
                        if v == "sudh":
                            op.append(v)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def extractKeys(self):
        try:
            logging.info("#6 . Try to list all the key in dict element avaible in list")
            logging.info("the input list is %s", self.dt)
            op=[]
            for i in self.dt:
                if type(i)==dict:
                    for k in i.keys():
                        op.append(k)
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)

    def extractValues(self):
        try:
            logging.info("#6 . Try to list all the Values in dict element avaible in list")
            logging.info("the input list is %s", self.dt)
            op=[]
            for i in self.dt:
                if type(i)==dict:
                    op.append(i.values())
            logging.info("the output is %s", op)
        except Exception as e:
            logging.error(e)




#list_obj=list_C([3,4,5,8,7, [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,9) ,{'key1':'sudh' , 234 : [23,45,656]}])
list_obj=list_C([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]])
print(list_obj.rev_list())
print(list_obj.access_234())
print(list_obj.access_234_withloop())
print(list_obj.access_456())
print(list_obj.access_456_withloop())
print(list_obj.extract_sublist())

dict_obj=dict_C([3,4,5,8,7, [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,9) ,{'key1':'sudh' , 234 : [23,45,656]}])
print(dict_obj.extractsudh_usingloop())
print(dict_obj.extractKeys())
print(dict_obj.extractValues())