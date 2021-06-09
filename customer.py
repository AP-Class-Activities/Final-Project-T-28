class Customer:
    __cuusername=100000
    def __init__(self,fname,lname,phonenumber,email,distance):
        self.__username='CU'+str(Customer.__cuusername)
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
                if Customer.isInt(i) == False:
                    raise ValueError('enter phone number correctlly!')
            self.__phonenumber=phonenumber
        else:
            raise ValueError('enter phone number correctlly!')
        self.__email=email
        self.__address=[]
        self.__favorites=[]
        self.__shoppinglist=[]
        self.__boughtproducts=[]
        self.__vallet=0
        if Customer.__isInt(distance) == True:
            self.__distance=distance
        else:
            raise ValueError('enter integers as distance!')

        Customer.__cuusername+=1

    #############################################################
    # helper method to check if a string is all made of integers#
    def __isInt(x):
        try: 
            int(x)
            return True
        except:
            return False

    ########################
    
    
    #########################
    ## setters and getters ##

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
    def Shoppinglist(self):
        return self.__shoppinglist
    
    @Shoppinglist.setter
    def Shoppinglist(self,newproduct):
        self.__shoppinglist.append(newproduct)

    @property
    def Favorites(self):
        return self.__favorites

    @Favorites.setter
    def Favorites(self,newFavorite):
        self.__favorites.append(newFavorite)

    @property
    def Boughtproducts(self):
        return self.__boughtproducts

    @Boughtproducts.setter
    def Boughtproducts(self,newproduct):
        self.__boughtproducts.append(newproduct)


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
    def Vallet(self):
        return self.__vallet

    @Vallet.setter
    def Vallet(self,transaction,amount):
        if transaction == 'add':
            self.__vallet += amount
        else:
            if amount <= self.__vallet:
                self.__vallet -= amount
            else:
                raise Exception('entered amount is more than your balance!')


    @property
    def Password(self):
        return self.__password

    @Password.setter
    def Password(self,newpass):
        self.__password=newpass

    #                          #
    ############################

    def __iadd__(self,amount):
        self.__vallet += amount

    def __isub__(self,amount):
        self.__vallet -= amount



    def __str__(self): 
        s = '\n\n______________________________________________________________________________________________________\n\n'
        s += 'fullname: {} {} |  phone: {} | email: {} | balance: {}'\
            .format(self.Firstname, self.Lastname, self.Phone, self.Email, self.Vallet)
        s += '\n\n____________________________________________addresses___________________________________________________\n\n'
        for i in self.Address:
            s += '%s\n'%(i) 
        
        s += '\n\n____________________________________________products___________________________________________________\n\n'        
        for i in self.BoughtProducts:
            s += '%s\n'%(i) 

        s += '_______________________________________________________________________________________________________'
        return s