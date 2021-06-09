from seller import Seller
from customer import Customer
from product import Product
import pickle

class Shop:
        def __init__(self,shopname):
                self.__profit=0
                self.__shopname=shopname
                self.__customerfile = r'data\{}_customers.dat'.format(self.__shopname)
                self.__sellerfile = r'data\{}_sellers.dat'.format(self.__shopname)
                self.__productfile = r'data\{}_products.dat'.format(self.__shopname)
                self.__customers = []
                self.__sellers = []
                self.__products = []

        


        #######################
        # setters and getters #
        @property
        def Shopname(self):
                return self.__shopname
        
        @Shopname.setter
        def Shopname(self,name): 
                self.__shopname = name

        @property
        def Profit(self):
                return self.__profit

        @Profit.setter
        def Profit(self,profit):
                self.__profit+=profit

        @property
        def Customers(self): 
                return self.__customers

        @property
        def Sellers(self): 
                return self.__sellers
        
        @property
        def Products(self): 
                return self.__products
        
        #                     #
        #######################

        ##################################################
        # add or remove sellers or customers or products #
               
        def __add__(self, element): 
                if type(element) is Customer: 
                        if element not in self.__customers:
                                self.__customers.append(element)
                
                elif type(element) is Seller: 
                        if element not in self.__sellerfile:
                                self.__sellers.append(element)
                
                elif type(element) is Product: 
                        if element not in self.__products:
                                self.__products.append(element)
                
                else: 
                        raise ValueError('the element you want to add should be of types [product , seller , customer]')
                
                return self

        def __sub__(self, element): 
                if type(element) is Seller: 
                        if element  in self.__sellers:
                                self.__sellers.remove(element)
                
                elif type(element) is Customer: 
                        if element  in self.__customers:
                                self.__customers.remove(element)
                
                elif type(element) is Product: 
                        if element  in self.__products:
                                self.__products.remove(element)

                return self
        #                                                 #
        ###################################################

        
        ##################################################
        # helper methods to save/read data in/from files #
        def __save_sellers(self): 
                with open(self.__sellerfile, 'wb') as file:
                        pickle.dump(self.Sellers, file)

        def __read_sellers(self): 
                with open(self.__sellerfile, 'rb') as file:
                        self.__sellers = pickle.load(file)
        
        def __save_customers(self): 
                with open(self.__customerfile, 'wb') as file:
                        pickle.dump(self.Customers, file)

        def __read_customers(self): 
                with open(self.__customerfile, 'rb') as file:
                        self.__customers = pickle.load(file)

        def __save_products(self): 
                with open(self.__productfile, 'wb') as file:
                        pickle.dump(self.Products, file)

        def __read_products(self): 
                with open(self.__productfile, 'rb') as file:
                        self.__products = pickle.load(file)


        
        def save_to_file(self): 
                self.__save_sellers()
                self.__save_products()
                self.__save_customers()

        def read_from_file(self): 
                self.__read_sellers()
                self.__read_customers()
                self.__read_products()
        
        #                                                      #
        ########################################################

        def __str__(self): 
                S = '\n\n______________________________________________________________________________________________________\n\n'
                S += 'Name of the shop: {} | Profit: {}'.format(self.Shopname,self.Profit)
                S += '\n\n____________________________________________sellers___________________________________________________\n\n'        
                for i in self.Sellers:
                        S += '%s\n'%(i) 
                
                S += '\n\n____________________________________________customers___________________________________________________\n\n'        
                for i in self.Customers:
                        S += '%s\n'%(i) 

                S += '\n\n____________________________________________products___________________________________________________\n\n'        
                for i in self.Products:
                        S += '%s\n'%(i)

                S += '_______________________________________________________________________________________________________'
                return S

''' 
    to make a shop:
        shop = Shop(name of the shop)

    to make a seller:
        s = Seller(string+firstname , string_lastname , string_phonenumber_11numbers , sring_email , integer_distance_from_main_shop_in_meters)
        +you can add an address with       ## s.Address = the address ##
        +


    to make a customer:
        c = Customer(string+firstname , string_lastname , string_phonenumber_11numbers , sring_email , integer_distance_from_main_shop_in_meters)
        +you can add an address with       ## c.Address = the address ##

    to make a product:
        p = Product(product_name , product_price , numbers_of_product , product_description)
'''
