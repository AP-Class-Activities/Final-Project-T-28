class Product:
    __prid=100000
    def __init__(self,prname,prprice,prstock,prdesc):
        self.__prID='PR'+str(Product.__prid)
        self.__prname=prname
        if type(prprice)!= int:
            raise ValueError('price should be integer numbers!')
        if type(prprice) is not int:
            raise ValueError('enter the price correctlly!')
        else:
            self.__prprice=prprice
        if type(prstock) is int:
            self.__prstock=prstock
        else:
            raise ValueError('enter integer number!')
        self.__prdesc=prdesc
        self.__comments=[]
        
        Product.__prid+=1


    #######################
    # setters and getters #
    
    @property
    def Comments(self):
        return self.__comments

    @Comments.setter
    def Comments(self,newcomment):
        self.__comments.append(newcomment)

    @property
    def ID(self):
        return self.__prID

    @property
    def Name(self):
        return self.__prname

    @Name.setter
    def Name(self,newname):
        self.__prname=newname

    @property
    def Price(self):
        return self.__prprice

    @Price.setter
    def Price(self,newprice):
        if type(newprice)!= int:
            raise ValueError('price should be integer')
        self.__prprice=newprice

    @property
    def Description(self):
        return self.__prdesc

    @Description.setter
    def Description(self,newdesc):
        self.__prdesc=newdesc

    @property
    def Stock(self):
        return self.__prstock
    
    @Stock.setter
    def Stock(self,newstock):
        self.__prstock=newstock

    #                   #
    #####################

    def __str__(self): 
        s = '\n\n______________________________________________________________________________________________________\n\n'
        s += 'ID: {} | name: {} | price: {} '\
            .format(self.ID,self.Name, self.Price)
        s += '\n\ndescription: \n {}'.format(self.Description)
        s += '\n\n____________________________________________comments___________________________________________________\n\n' 
        for i in self.Comments:
            s += '%s\n'%(i) 
        s += '\n\n_______________________________________________________________________________________________________\n\n'
        return s