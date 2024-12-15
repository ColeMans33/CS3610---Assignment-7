from Observer import Observer
class AppClient(Observer):
    def __init__(self, id, currentVersion):
        self.version = currentVersion
        self.id = id

    def update(self, newVersion):
        print(f"Game client {self.id} has updated to version {newVersion}")
        self.version = newVersion

