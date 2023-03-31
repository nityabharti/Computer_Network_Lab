import Pyro4

@Pyro4.expose

class Warehouse:
    def __init__(self):
        self.items=["pocox3","boat earphhones","acer","Mi charger","USpolo watch"]
        
    def list_contents(self):
        return self.items

    def take(self,name,item):
        self.items.remove(item)
        print("{0} took the {1}".format(name,item))
    
    def store(self,name,item):
        self.items.append(item)
        print("{0} stored the {1}".format(name,item))

def main():
        Pyro4.Daemon.serveSimple(
            {
                Warehouse: "example.warehouse"
            },
            ns = True)

if __name__=="__main__":
    main()