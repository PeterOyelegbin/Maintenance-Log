# Maintenance Log
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3 as db
import time

#=======================================================Database======================================================================
con = db.connect('Catalog.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS USER (
            Organization text,
            Date_Established text,
            UserName text,
            Password text
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS SCHEDULE (
            Name text,
            Phone_Number integer,
            Address text,
            Maintenance_date text
            )''')
cur.close()
con.commit()
con.close()

def about():
    dialog = QDialog()
    dialog.setWindowTitle('About')
    dialog.setFont(QFont('Arial Bold', 10))
    dialog.setFixedSize(250,340)
    vb = QVBoxLayout(dialog)
    fme = QFrame()
    vb.addWidget(fme)
    grid = QGridLayout(fme)
    image = QPixmap("C:/Users/Hp/Pictures/GUI Tools/Maintenance Personnel.png")
    iproduct = QLabel()
    iproduct.setPixmap(image)
    iproduct.setScaledContents(True)
    iproduct.setFixedSize(70,50)
    grid.addWidget(iproduct, 0,0)
    
    product = QLabel('Maintenance\nLog 2.0')
    product.setFont(QFont('Forte', 18))
    product.setStyleSheet('color:magenta;')
    grid.addWidget(product, 0,1)

    frame = QGroupBox('Developed by:')
    vb.addWidget(frame)
    form = QFormLayout(frame)
    icon = QPixmap("C:/Users/Hp/Pictures/Clip-art/OYETEK Logo.png")
    Company = QLabel()
    Company.setPixmap(icon)
    Company.setScaledContents(True)
    Company.setFixedSize(70,50)

    company = QLabel('OYETEK')
    form.addRow(Company,company)
    
    details = QLabel('Mobile:        08188066398 \n\nWhatsApp:   08174071289 \n\nInstagram:   official_oyetek \n\n© 2020')
    form.addRow(details)

    close = QPushButton('Close', clicked=dialog.close)
    vb.addWidget(close)
    dialog.exec_()

def terms():
    file = open('Terms and Conditions.txt', 'r').read()
    dialog = QDialog()
    dialog.setWindowTitle('Terms & Conditions')
    dialog.setFont(QFont('Arial Bold', 10))
    dialog.setFixedSize(350,470)
    vb = QVBoxLayout(dialog)
    txt = QTextEdit()
    txt.setText(str(file))
    txt.setReadOnly(True)
    vb.addWidget(txt)

    close = QPushButton('Close', clicked=dialog.close)
    vb.addWidget(close)
    dialog.exec_()

def signup_page():
    stack.setCurrentWidget(P2)

def login_page():
    stack.setCurrentWidget(P3)

def createuser():
    if len(user.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Username has no entry!")
    elif len(pwd.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Password has no entry!")
    elif cpwd.text() != pwd.text():
        QMessageBox.warning(win, 'Warning', 'Warning!: Unmatched password,\n retry!')
    else:
        con = db.connect('Catalog.db')
        cur = con.cursor()
        find_user = ("SELECT * FROM USER WHERE UserName = ?")
        cur.execute(find_user, [(user.text())])
        if cur.fetchall():
            QMessageBox.critical(win, 'Error Message', "Error: Username Taken")
        else:
            cur.execute("insert into USER values(?, ?, ?, ?)",
                    (org.text(),est.text(),user.text(),pwd.text()))
            cur.close()
            con.commit()
            con.close()
            time.sleep(0.25)
            stack.setCurrentWidget(P4)
            org.clear(),est.clear(),user.clear(),pwd.clear(),cpwd.clear()
    
def login():
    con = db.connect('Catalog.db')
    cur = con.cursor()
    find_user = ("SELECT * FROM USER WHERE UserName = ? AND Password = ?")
    cur.execute(find_user,[user2.text(),pwd2.text()])
    results = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    if results:
        for i in results:
            time.sleep(0.25)
            stack.setCurrentWidget(P4)
            user2.clear(),pwd2.clear()
    else:
        QMessageBox.critical(win, 'Error Message', "Error: Username or password\n not recognized!")

def back():
    stack.setCurrentWidget(P1)

def add():
    if len(name.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Name has no entry!")
    elif len(phone_number.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Phone Number has no entry!")
    elif len(address.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Address has no entry!")
    elif len(maintenance_date.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Maintenance Date has no entry!")
    else:
        con = db.connect('Catalog.db')
        cur = con.cursor()
        find_user = ("SELECT * FROM SCHEDULE WHERE Name = ?")
        cur.execute(find_user, [name.text()])
        if cur.fetchall():
            QMessageBox.critical(win, 'Error Message', "Error: Name already exist!")
        else:
            cur.execute("insert into SCHEDULE values(?, ?, ?, ?)",(name.text(),
                        phone_number.text(),address.text(),maintenance_date.text()))
            cur.close()
            con.commit()
            con.close()
            QMessageBox.information(win, "Status", "Schedule Successfully Saved")
            name.clear(),phone_number.clear(),address.clear(),maintenance_date.clear()

def fetchdata():
    con = db.connect('Catalog.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM SCHEDULE")
    list0 = str(cur.fetchall())
    cur.close()
    con.commit()
    con.close()
    text.clear()
    text.setText(list0)

def updatedata():
    if len(Ename.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Name has no entry!")
    elif len(Emaintenance_date.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Maintenance Date has no entry!")
    else:
        con = db.connect('Catalog.db')
        cur = con.cursor()
        find_user = ("SELECT * FROM SCHEDULE WHERE Name = ?")
        cur.execute(find_user, [Ename.text()])
        if not cur.fetchall():
            QMessageBox.critical(win, 'Error Message', "Error: Schedule does not exist!")
        else:
            cur.execute("UPDATE SCHEDULE SET Maintenance_Date = ? WHERE Name = ?",(Emaintenance_date.text(),Ename.text()))
            cur.close()
            con.commit()
            con.close()
            QMessageBox.information(win, 'Status', 'Schedule Updated!')
            Ename.clear(),Emaintenance_date.clear()

def removedata():
    if len(nme.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Name has no entry!")
    elif len(phn.text()) < 1:
        QMessageBox.critical(win, 'Error Message', "Error: Phone number has no entry!")
    else:
        con = db.connect('Catalog.db')
        cur = con.cursor()
        find_user = ("SELECT * FROM SCHEDULE WHERE Name = ? AND Phone_Number = ?")
        cur.execute(find_user, (nme.text(),phn.text()))
        if not cur.fetchall():
            QMessageBox.critical(win, 'Error Message', "Error: Schedule does not exist!")
        else:
            Del = QMessageBox.question(win, 'Delete', 'Are you sure?')
            if Del == QMessageBox.No:
                QMessageBox.information(win, 'Status', 'Schedule not deleted!')
            else:
                cur.execute("DELETE FROM SCHEDULE WHERE Name = ? AND Phone_Number = ?", (nme.text(),phn.text()))
                cur.close()
                con.commit()
                con.close()
                QMessageBox.information(win, 'Status', 'Schedule Deleted!')
                nme.clear(),phn.clear()

def job_schedule():
    con = db.connect('Catalog.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM SCHEDULE")
    lists = cur.fetchall()
    today = time.strftime('%d-%B')
    flag = 0
    for data in lists:
        if today in data:
            flag = 1
            QMessageBox.information(win, 'Notification', "Today's maintenance schedule is: \n"+str(data))
    if flag == 0:
        QMessageBox.information(win, 'Notification', 'No maintenance job scheduled for today!')
    cur.close()
    con.commit()
    con.close()


#=====================================================Graphical User Interface========================================================
app = QApplication([])
app.setStyle('Fusion')

# Set Window and Widget Color
qp = QPalette()
qp.setColor(QPalette.Window, Qt.yellow)
qp.setColor(QPalette.Button, Qt.blue)
app.setPalette(qp)

magenta = (QPalette(QColor(Qt.magenta)))
green = (QPalette(QColor(Qt.green)))
gray = (QPalette(QColor(Qt.gray)))
red = (QPalette(QColor(Qt.red)))

# Create Window
win = QWidget()
win.setFixedSize(600,400) #resize
win.setWindowTitle('Maintenance Log 2.0')
win.setWindowIcon(QIcon("C:/Users/Hp/Pictures/GUI Tools/Maintenance Personnel.png"))
win.setFont(QFont('Arial Bold', 16))

# Create Main Menu
vb = QVBoxLayout(win)
bar = QMenuBar()
bar.setNativeMenuBar(False)
vb.addWidget(bar)
Menu = bar.addMenu('⁞⁞⁞')

# Add Menu Button    
About = QAction("About", triggered=about)
Menu.addAction(About)

Quit = QAction("Quit", triggered=win.close)
Quit.setShortcut('Ctrl+Q')
Quit.setStatusTip('Exit application')
Menu.addAction(Quit)

job_schedule()

# Set Page Widget
stack = QStackedWidget()
P1 = QWidget()
P2 = QWidget()
P3 = QWidget()
P4 = QWidget()
stack.addWidget(P1)
stack.addWidget(P2)
stack.addWidget(P3)
stack.addWidget(P4)
vb.addWidget(stack)

#=========================Page 1 interface==========================
grid = QGridLayout(P1)
Product = QLabel("Maintenance Log 2.0")
Product.setFont(QFont('Arial Black', 26))
Product.setStyleSheet('color:magenta;')
grid.addWidget(Product, 0,0,1,2)

# Add image
image = QPixmap("C:/Users/Hp/Pictures/GUI Tools/Maintenance Personnel.png")
Home = QLabel()
Home.setPixmap(image)
Home.setScaledContents(True)
grid.addWidget(Home, 1,0,1,2)

# Add Button Widget
Create = QPushButton('Create User', clicked=signup_page)
Create.setPalette(magenta)
log_in = QPushButton("Log In >>", clicked=login_page)
log_in.setPalette(magenta)
grid.addWidget(Create, 2,0)
grid.addWidget(log_in, 2,1)

#=========================Page 2 interface==========================
# Add Label Widget
vb = QVBoxLayout(P2)
sign_up = QGroupBox("Sign up")
vb.addWidget(sign_up)
form = QFormLayout(sign_up)
Org = QLabel("Organization: ")
Est = QLabel("Date Established: ")
User = QLabel("UserName: ")
Pwd = QLabel("Password: ")
CPwd = QLabel("Confirm Pwrd: ")
TC = QLabel("read terms and condition >>")

# Add Entry Widget
org = QLineEdit()
form.addRow(Org,org)
est = QLineEdit()
form.addRow(Est,est)
user = QLineEdit()
form.addRow(User,user)
pwd = QLineEdit()
pwd.setEchoMode(QLineEdit.Password)
form.addRow(Pwd,pwd)
cpwd = QLineEdit()
cpwd.setEchoMode(QLineEdit.Password)
form.addRow(CPwd,cpwd)

# Add Button Widget
tc = QLabel("<A href='www.here.com'>here</a>")
tc.linkActivated.connect(terms)
tc.setFont(QFont('Elephant', 20))
tc.setStyleSheet('color:blue;')
form.addRow(TC,tc)
Create = QPushButton('Create User', clicked=createuser)
Create.setPalette(green)
Back = QPushButton('Back', clicked=back)
Back.setPalette(gray)
form.addRow(Back,Create)

#=========================Page 3 interface==========================
# Add Label Widget
vb = QVBoxLayout(P3)
Log_in = QGroupBox("Log in")
vb.addWidget(Log_in)
form = QFormLayout(Log_in)
User2 = QLabel("UserName: ")
Pwd2 = QLabel("Password: ")
Info = QLabel("By using this product, you accept the\n terms and condition governing the use\n of this product.")
Info.setFont(QFont('Elephant', 20))
Info.setStyleSheet('color:green;')
Info.setAlignment(Qt.AlignCenter)

# Add Entry Widget
user2 = QLineEdit()
form.addRow(User2,user2)
pwd2 = QLineEdit()
pwd2.setEchoMode(QLineEdit.Password)
form.addRow(Pwd2,pwd2)
form.addRow(Info)

# Add Button Widget
log_in = QPushButton("Log In >>", clicked=login)
Back = QPushButton('Back', clicked=back)
Back.setPalette(gray)
form.addRow(Back,log_in)

#=========================Page 4 interface==========================
vb = QVBoxLayout(P4)
# Create tabs
tabs = QTabWidget()
tab1 = QWidget()
tabs.addTab(tab1,"Add")
tab2 = QWidget()
tabs.addTab(tab2,"Update/Fetch")
tab3 = QWidget()
tabs.addTab(tab3,"Delete/Log Out")
vb.addWidget(tabs)

#-------------------Tab1 in Page 4------------------
form = QFormLayout(tab1)
# Add Label Widget
Name = QLabel("Name: ")
Phone_Number = QLabel("Phone Number: ")
Address = QLabel("Address: ")
Maintenance_Date = QLabel("Maintenance Date: ")

# Add Entry Widget
name = QLineEdit()
form.addRow(Name,name)
phone_number = QLineEdit()
form.addRow(Phone_Number,phone_number)
address = QLineEdit()
form.addRow(Address,address)
maintenance_date = QLineEdit()
maintenance_date.setPlaceholderText('01-January')
form.addRow(Maintenance_Date,maintenance_date)

# Add Button Widget
Add = QPushButton("Add Schedule", clicked=add)
Add.setPalette(green)
form.addRow(Add)

#-----------------Tab2 in Page 3------------------
vb = QVBoxLayout(tab2)
frame = QFrame()
vb.addWidget(frame)
form = QFormLayout(frame)
# Add Label Widget
EName = QLabel("Name: ")
EMaintenance_Date = QLabel("Maintenance Date: ")

# Add Entry Widget
Ename = QLineEdit()
form.addRow(EName,Ename)
Emaintenance_date = QLineEdit()
Emaintenance_date.setPlaceholderText('09-February')
form.addRow(EMaintenance_Date,Emaintenance_date)

# Add Button Widget
Update = QPushButton("Update Schedule", clicked=updatedata)
Update.setPalette(magenta)
form.addRow(Update)


frame2 = QFrame()
vb.addWidget(frame2)
form = QFormLayout(frame2)
# Add Entry Widget
text = QTextEdit()
text.resize(600,270)

# Add Button Widget
fetch = QPushButton("Fetch All", clicked=fetchdata)
form.addRow(text)
form.addRow(fetch)

#-----------------Tab3 in Page 3-----------------
form = QFormLayout(tab3)
# Add Label Widget
Nme = QLabel("Name: ")
Phn = QLabel("Phone Number: ")
Info = QLabel("WARNING!: Any data deleted can not\n be retrived, be careful to delete any data\n if not sure!")
Info.setFont(QFont('Elephant', 20))
Info.setStyleSheet('color:red;')
Info.setAlignment(Qt.AlignCenter)

# Add Entry Widget
nme = QLineEdit()
form.addRow(Nme,nme)
phn = QLineEdit()
form.addRow(Phn,phn)

# Add Button Widget
delete = QPushButton("Delete Schedule", clicked=removedata)
delete.setPalette(red)
log_out = QPushButton("<< Log Out", clicked=back)
log_out.setPalette(magenta)
form.addRow(Info)
form.addRow(log_out,delete)


win.show()
app.exec_()
