# Python RMI Lab (Pyro5)

A Python translation of a Java RMI project using **Pyro5** (Python Remote Objects).

| Python file  | Java equivalent                                   |
|--------------|---------------------------------------------------|
| `product.py` | `Product.java` (remote interface / contract)      |
| `server.py`  | `Server.java`, `ProductImpl.java`, `ServerImpl.java` |
| `client.py`  | `Client.java`                                     |

## How it works
- `ServerImpl` is published on `localhost:9080'under the object id `product.server`
  (the counterpart of binding a stub in the RMI registry).
- `ProductImpl` objects are registered with the daemon and returned to the client
  as **remote references** (auto-proxies), like returning a `Remote` stub in Java.
- The client creates a `Pyro5.api.Proxy` from the URI and calls methods as if local.



## How to start
#python -m pip install Pyro5
# python -m Pyro5.nameserver -n 127.0.0.1 -p 9100


## Requirements
- Python 3.8+
- Pyro5

```bash
pip install -r requirements.txt
```

## Run
Open **two terminals** in this folder.

**Terminal 1 - server**
```bash
python server.py
```

**Terminal 2 - client**
```bash
python client.py
```

Start the server first. Stop it with `Ctrl+C`.

## Expected output
Server terminal shows the URI and each call (`list_products`, `get_product`, ...).
Client terminal prints the product list, the details, the added product, and the
handled "missing product" error.

## Screenshots
Add your server and client terminal screenshots to a `screenshots/` folder and
reference them here.
