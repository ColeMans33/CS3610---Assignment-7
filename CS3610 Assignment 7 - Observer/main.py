from Subject import Subject
from AppClient import AppClient
app_server = Subject()

user1 = AppClient(app_server.getNextID(), app_server.getVersion())
user2 = AppClient(app_server.getNextID(), app_server.getVersion())
user3 = AppClient(app_server.getNextID(), app_server.getVersion())

app_server.attach(user1)
app_server.attach(user2)
app_server.attach(user3)

app_server.pushUpdate("Version 2")
