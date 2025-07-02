class chatbook:
    __user_id=0
    def __init__(self):
        self.id=chatbook.__user_id #only class can acces this
        chatbook.__user_id +=1
        self.__name= 'default username'
        self.user_id=0
        self.user_id+=1
        self.username = ''
        self.password = ''
        self.loggedin = False
       # self.menu()

#static method
    def get_id():
        return chatbook.__user_id

#static method
    def set_id(val):
        chatbook.__user_id=val

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name= value



    def menu(self):
        user_input = input("""welcome to chatbook !! How would you like to proceed?
                           1.press 1 to signup
                           2.press 2 to signin
                           3.press 3 to write a post
                           4.press 4 to message a freind
                           5.press any other key to exit 
                           
                           """)
        if user_input == "1":
           self.signup()
        elif user_input == "2":
           self.signin()
        elif user_input =="3":
           self.sendmsg()
        elif user_input =="4":
           self.my_post()
        else:
           exit()


    def signup(self):
        email = input("eneter your email here -->")
        pwd = input("setup your password here -->")
        self.username = email
        self.password = pwd
        print("you have signed up succesfully !!")
        print("\n")
        self.menu()

    def signin(self):
      if self.username=='' and self.password=='' :
            print("please signup first by pressing 1 in the main menu")
      else:
          username = input("eneter your email/username here -->")
          pwd = input("eneter your password here -->")
          if self.username == username and self.password == pwd :
             print('you have signed in successfully !!')
             self.loggedin = True
          else:
             print("please input correcrt credentials..")
      print('\n')
      self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt= input("enter your message here -->")
            print(f"following content has been posted--> {txt}")
        else:
            print("you need to sign in first to post something....")
        print("\n") 
        self.menu()
    def sendmsg(self):
       if self.loggedin==True:
            txt= input("enter your message here -->")
            frnd=input("whom to send the msg-->")
            print(f"your msg is sent to {frnd}")
       else:
            print("you need to sign in first to post something....")
       print("\n") 
       self.menu()

   
obj = chatbook()
#print(obj._chatbook__name)#to acces private


