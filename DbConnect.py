try:
    import sqlite3
except ImportError:
    print("Import not successful")

db = sqlite3.connect("FirstDb.db")

def create():
    # Creates a table called Admin
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Admin(Name text,Age int)")
    # Finalize the changes
    db.commit()

def add(Name,age):
    # Adds a record to the table
    db.row_factory=sqlite3.Row
    db.execute("insert into Admin(Name,Age) values (?,?)",(Name,age))
    # Finalize the changes
    db.commit()
    print("Insertion succesful!!!\n")

def show():
    # Shows the data in the table 'Admin'
    Data=db.execute("select * from Admin")
    print("Name\tAge")
    for row in Data:
        print("{}\t{}".format(row["Name"],row["Age"]))
    print("\n")

def deleteData(name):
    # Delete a record
    db.row_factory = sqlite3.Row
    db.execute("delete from Admin where Name='{}'".format(name))
    db.commit()
    print("Record deleted")

def updateAge(name,age):
    # Update the age of a record
    db.row_factory=sqlite3.Row
    db.execute("Update Admin set Age={} where Name='{}'".format(age,name))
    db.commit()
    print("Record updated")

def main():
    # Create table to work with at start
    create()
    try:
        while 1:
            # Ask for which operation the user wants to perform
            opt=int(input("Enter what u want to do:\n 0.Exit\t1.Add\t2.Show table data\t3.Delete\t4.Update\n"))
            if(opt==1):
                N=input("Enter the name:\n")
                A=int(input("Enter age:\n"))
                add(N,A)
            elif(opt==2):
                show()
            elif(opt==3):
                de=input("Enter the name:")
                deleteData(de)
            elif(opt==4):
                N = input("Enter the name:\n")
                A = int(input("Enter the new age:\n"))
                updateAge(N,A)
            elif(opt==0):
                break
            else:
                print("Invalid operation\n")
    except ValueError:
        print("Invalid value type\n")
    except IOError:
        print("Input/Output error ocurred\n")
    finally:
        print("Thank you for trying this program\n")


if __name__ == '__main__':main()
