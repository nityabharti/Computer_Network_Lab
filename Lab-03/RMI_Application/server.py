import Pyro4
import random


@Pyro4.expose
class kerberos():
    def get_fortune(self,name):
        return "Hello,{0}. Here is your fortune message:Tomorrow's lucky number is {1}.".format(name,random.randint(0,1000))
    def sum(self,a,b):
        return "{0} +{1} ={2}".format(a,b,int(a)+int(b))


#Server
daemon=Pyro4.Daemon()

# Naming Server
ns=Pyro4.locateNS()

# Location of the object
location = daemon.register(kerberos)

# regitering with naming server
ns.register("example.kerb",location)

print("Hi. Kerberos is now active.")
# goes to listening state
daemon.requestLoop()