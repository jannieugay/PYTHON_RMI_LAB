import Pyro5.api
from ProductImpl import ProductImpl

print("Server has been started...")

daemon = Pyro5.api.Daemon(host="127.0.0.1")
ns = Pyro5.api.locate_ns(host="127.0.0.1", port=9100)

p1 = ProductImpl("Laptop", "Lenovo Laptop",20000)
p2 = ProductImpl("Mobile", "Mi mobile", 500)
p3 = ProductImpl("Power Charger", "Lenovo Charger", 900)
p4 = ProductImpl("MotorBike", "Yamaha Biker",100)

uri1 = daemon.register(p1)
uri2 = daemon.register(p2)
uri3 = daemon.register(p3)
uri4 = daemon.register(p4)

ns.register("l", uri1)
ns.register("m", uri2)
ns.register("c", uri3)
ns.register("b", uri4)

print("Exporting and binding of Objects has been completed...")

daemon.requestLoop()


# python -m pip install Pyro5
# python -m Pyro5.nameserver -n 127.0.0.1 -p 9100
# python Server.py
# python Client.py