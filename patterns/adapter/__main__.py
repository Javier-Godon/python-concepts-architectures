from patterns.adapter.via_inheritance import Target, Adaptee, Adapter, client_code

print("Client: I can work just fine with the Target objects:")
target = Target("message")
client_code(target)
print("\n")

adaptee = Adaptee("message")
print("Client: The Adaptee class has a weird interface. "
      "See, I don't understand it:")
print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

print("Client: But I can work with it via the Adapter:")
adapter = Adapter("message")
client_code(adapter)
