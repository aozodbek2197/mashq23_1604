# 1-mashq
class PaymentStrategy:
    def pay(self, amount): pass

class CreditCard(PaymentStrategy):
    def pay(self, amount): print(f"{amount} so'm kredit karta orqali to'landi.")

class PayPal(PaymentStrategy):
    def pay(self, amount): print(f"{amount} so'm PayPal orqali to'landi.")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy
    def process(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(CreditCard())
processor.process(1500000)
# 2-mashq
class Subscriber:
    def update(self, message): pass

class EmailSubscriber(Subscriber):
    def update(self, message):
        print(f"Email orqali: {message}")

class NewsPublisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, sub):
        self.subscribers.append(sub)
    def notify(self, message):
        for sub in self.subscribers:
            sub.update(message)

pub = NewsPublisher()
pub.subscribe(EmailSubscriber())
pub.notify("Yangi maqola chop etildi!")
# 3-mashq
class Coffee:
    def cost(self): return 10000
    def description(self): return "Oddiy kofe"

class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self): return self.coffee.cost() + 3000
    def description(self): return self.coffee.description() + " + Sut"

coffee = MilkDecorator(Coffee())
print(coffee.description(), "-", coffee.cost(), "so'm")
# 4-mashq
class Vehicle:
    def __init__(self, size): self.size = size

class ParkingSpot:
    def __init__(self, size):
        self.size = size
        self.vehicle = None
    def is_free(self): return self.vehicle is None

class ParkingLot:
    def __init__(self):
        self.spots = [ParkingSpot("small"), ParkingSpot("medium"), ParkingSpot("large")]
    
    def park(self, vehicle):
        for spot in self.spots:
            if spot.is_free() and spot.size == vehicle.size:
                spot.vehicle = vehicle
                print("Mashina joylandi!")
                return
        print("Bo'sh joy yo'q!")

lot = ParkingLot()
lot.park(Vehicle("small"))
# 5-mashq
class ChatRoom:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def broadcast(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        room.add_user(self)
    def send(self, message):
        self.room.broadcast(self, f"{self.name}: {message}")
    def receive(self, message):
        print(f"{self.name} qabul qildi: {message}")

room = ChatRoom()
u1 = User("Ali", room)
u2 = User("Vali", room)
u1.send("Salom hammaga!")
