import sys
import Pyro4
from person import Person

warehouse = Pyro4.Proxy("PYRONAME:example.warehouse")
janet = Person("pradeep")
henry = Person("shiva")
janet.visit(warehouse)
henry.visit(warehouse)