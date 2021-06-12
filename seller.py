


class Seller:
    __slusername=100000
    def __init__(self,fname,lname,phonenumber,email,distance):
        self.__username='SL'+str(Seller.__slusername)
        if type(fname) == str:
            self.__firstname=fname
        else:
            raise ValueError('first name must be string!')

        if type(lname) == str:
            self.__lastname=lname
        else:
            raise ValueError('last name must be string!')
        
        if len(phonenumber) == 11:
            for i in phonenumber:
                if Seller.__isInt(i) == False:
                    raise ValueError('enter phone number correctlly!')
            self.__phonenumber=phonenumber
        else:
            raise ValueError('enter phone number correctlly!')
        self.__email=email
        self.__address=[]
        self.__wallet=0
        self.__products=[]
        if Seller.__isInt(distance) == True:
            self.__distance=distance
        else:
            raise ValueError('enter integers as distance!')

        Seller.__slusername+=1
    ##################
    # helper methods #
    def __isInt(x):
        try: 
            int(x)
            return True
        except:
            return False
        
     def __wallet_transactions(self,add_or_sub,amount):
        if add_or_sub == 'add':
            self.__wallet += amount
        elif add_or_sub == 'sub':
            self.__wallet -= amount


    def add_to_wallet(self,amount):
        self.__wallet_transactions('add',amount)

    def sub_from_wallet(self,amount):
        if self.__wallet >= amount:
            self.__wallet_transactions('sub',amount)
        else:
            raise ValueError('entered amount is more than your balance')

    ######################

    

    #######################
    # setters and getters #

    @property
    def Username(self):
        return self.__username
 
    @property
    def Distance(self):
        return self.__distance

    @Distance.setter
    def Distance(self,dis):
        self.__distance = dis

    @property
    def Firstname(self):
        return self.__firstname

    @Firstname.setter
    def Firstname(self,newname):
        self.__firstname=newname

    @property
    def Lastname(self):
        return self.__lastname

    @Lastname.setter
    def Lastname(self,newname):
        self.__lastname=newname

    @property
    def Phone(self):
        return self.__phonenumber

    @Phone.setter
    def Phone(self,newphonen):
        self.__phonenumber=newphonen

    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self,newemail):
        self.__email=newemail

    @property
    def Address(self):
        return self.__address

    @Address.setter
    def Address(self,newaddress):
        self.__address.append(newaddress)

    @property
    def Password(self):
        return self.__password

    @Password.setter
    def Password(self,newpass):
        self.__password=newpass

    @property
    def Products(self):
        return self.__products

    @Products.setter
    def Products(self,newproduct):
        self.__products.append(newproduct)

    @property
    def Wallet(self):
        return self.__wallet


    #                      #
    ########################




    def __str__(self): 
        s = '\n\n______________________________________________________________________________________________________\n\n'
        s += 'Username: {} | fullname: {} {} |  phone: {} | email: {} | balance: {} | distance: {}'\
            .format(self.Username,self.Firstname, self.Lastname, self.Phone, self.Email, self.Wallet,self.Distance)
        s += '\naddress:\n {}'.format(self.Address)
        s += '\n\n____________________________________________products___________________________________________________\n\n'        
        for i in self.Products:
            s += '%s\n'%(i) 

        s += '_______________________________________________________________________________________________________'
        return s
    
