import Pyro4
# Client
kerberos=Pyro4.Proxy("PYRONAME:example.kerb")

name= input("what is your name? ")
print(kerberos.get_fortune(name))


a,b= input("Enter 'a','b' to get it sum: ").split(' ')
print(kerberos.sum(a,b))
