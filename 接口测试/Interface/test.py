import cPickle
import os
import sys

class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail

    def Update(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail

    def display(self):
        print "name:%s, phone:%s, mail:%s" % (self.name, self.phone, self.mail)


# begin

# file to store contact data
data = os.getcwd() + os.sep + "contacts.data"

while True:
    print "-----------------------------------------------------------------------"
    operation = raw_input("input your operation(add/delete/modify/search/all/exit):")

    if operation == "exit":
       sys.exit()

    if os.path.exists(data):
        if os.path.getsize(data) == 0:
            contacts = {}
        else:
            f = file(data)
            contacts = cPickle.load(f)
            f.close()
    else:
        contacts = {}

    if operation == "add":
        flag = False
        while True:
            name = raw_input("input name(exit to back choose operation):")
            if name == "exit":
                flag = True
                break
            if name in contacts:
                print "the name already exists, please input another or input 'exit' to back choose operation"
                continue
            else:
                phone = raw_input("input phone:")
                mail = raw_input("input mail:")
                c = Contact(name, phone, mail)
                contacts[name] = c
                f = file(data, "w")
                cPickle.dump(contacts, f)
                f.close()
                print "add successfully."
                break
    elif operation == "delete":
        name = raw_input("input the name that you want to delete:")
        if name in contacts:
            del contacts[name]
            f = file(data, "w")
            cPickle.dump(contacts, f)
            f.close()
            print "delete successfully."
        else:
            print "there is no person named %s" % name
    elif operation == "modify":
        while True:
            name = raw_input("input the name which to update or exit to back choose operation:")
            if name == "exit":
                break
            if not name in contacts:
                print "there is no person named %s" % name
                continue
            else:
                phone = raw_input("input phone:")
                mail = raw_input("input mail:")
                contacts[name].Update(name, phone, mail)
                f = file(data, "w")
                cPickle.dump(contacts, f)
                f.close()
                print "modify successfully."
                break
    elif operation == "search":
        name = raw_input("input the name which you want to search:")
        if name in contacts:
            contacts[name].display()
        else:
            print "there is no person named %s" % name
    elif operation == "all":
        for name, contact in contacts.items():
            contact.display()
    else:
        print "unknown operation"