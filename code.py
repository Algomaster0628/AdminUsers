class user():
   def __init__(self,first_name,last_name,username):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.no_login = 0
   def describe_user(self):
       print("First Name: " + self.first_name)
       print("Last Name: " + self.last_name)
       print("User Name: " + self.username)
       
   def greet_user(self):
       print("Hi," + self.username)
   def set_number_login(self):
       self.no_login +=1
       print("Number of Attempts: " + str(self.no_login))
   def reset_loginattempts(self):
       self.no_login = 0
vansh = user('vansh','gupta','algo')
vansh.describe_user()
vansh.set_number_login()
vansh.set_number_login()
vansh.set_number_login()
class admin(user):
   def __init__(self,first_name,last_name,username):
      super().__init__(first_name,last_name,username)
      self.privelages = []
   def show_privelages(self):
       for privelages in self.privelages:
         print("privelages:" + privelages)
my_user = admin('vansh','gupta','algo')
my_user.greet_user()
my_user.describe_user()
my_user.privelages = ["you can ban users","you can dismiss anyone"]
my_user.show_privelages()

