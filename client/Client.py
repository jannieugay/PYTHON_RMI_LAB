import Pyro5.api

try:
    ns = Pyro5.api.locate_ns(host="127.0.0.1", port=9100)

    p1 = Pyro5.api.Proxy(ns.lookup("l"))
    p2 = Pyro5.api.Proxy(ns.lookup("m"))
    p3 = Pyro5.api.Proxy(ns.lookup("c"))
    p4 = Pyro5.api.Proxy(ns.lookup("b"))

    print("The product name is:", p1.getName(),
          ", The price is:", p1.getPrice())

    print("The product name is:", p2.getName(),
          ", The price is:", p2.getPrice())

    print("The product name is:", p3.getName(),
          ", The price is:", p3.getPrice())

    print("The product name is:", p4.getName(),
          ", The price is:", p4.getPrice())

except Exception as e:
    print("Client side error...", e)