from datetime import datetime

class Module:
    def __init__(self, name, ram, storage, version, owner_name, purchase_date):
        self.name = name
        self.ram = ram
        self.storage = storage
        self.version = version
        self.owner_name = owner_name
        self.purchase_date = purchase_date  # format: "DD-MM-YYYY"

    def print_ram(self):
        print(f"RAM: {self.ram}")

    def print_owner_name(self):
        print(f"Owner Name: {self.owner_name}")

    def calculate_days_since_purchase(self):
        purchase = datetime.strptime(self.purchase_date, "%d-%m-%Y")
        today = datetime.today()
        difference = today - purchase
        print(f"Days since purchase: {difference.days}")

    def display_info(self):
        print("Module Information:")
        print(f"Name: {self.name}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print(f"Version: {self.version}")
        print(f"Owner: {self.owner_name}")
        print(f"Purchased On: {self.purchase_date}")

# Example usage
module1 = Module(
    name="SmartModuleX",
    ram="8GB",
    storage="256GB",
    version="1.2.3",
    owner_name="Sarthak Bankar",
    purchase_date="01-02-2003"
)

module1.print_ram()
module1.print_owner_name()
module1.calculate_days_since_purchase()
module1.display_info()
