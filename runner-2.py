import tkinter as tk
from tkinter import font  as tkfont
from tkinter.messagebox import showinfo
import sql as db

currentUser = ""
isCurator = False
isAdmin = False
currentMuseum = ""

class Controller(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.paragraph_font = tkfont.Font(family='Helvetica', size=12)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (WelcomePage, LoginPage, SignupPage, VisitorHome, CuratorHome, AdminHome, OneMuseumPage, MakeReviewPage, ViewReviews, AllMuseums, TicketHistoryPage, ReviewHistoryPage, ManageAccountPage, CuratorRequestPage, DeleteAccountPage, MyMuseumsPage, MySpecificMuseum, NewExhibitPage, AdminCurPage, NewMuseumPage, DeleteMuseumForm):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()


class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to BMTRS", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to Login Page", command=lambda: controller.show_frame("LoginPage"))
        button1.pack()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Login Page", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.button = tk.Button(self, text="Go to the welcome page", command=lambda: controller.show_frame("WelcomePage"))
        self.emailLabel = tk.Label(self, text="Email", font=controller.paragraph_font)
        self.emailEntry = tk.Entry(self, width=20)
        self.passwordLabel = tk.Label(self, text="Password", font=controller.paragraph_font)
        self.passwordEntry = tk.Entry(self, width=20, show="*")
        self.button2 = tk.Button(self, text="Login", command=lambda: LoginPage.logIn(emailEntry.get(), passwordEntry.get(), controller))
        self.button3 = tk.Button(self, text="Go to Signup Page", command=lambda: controller.show_frame("SignupPage"))
        self.button.pack()
        self.emailLabel.pack()
        self.emailEntry.pack()
        self.passwordLabel.pack()
        self.passwordEntry.pack()
        self.button2.pack()
        self.button3.pack()

    def update(self) :
        self.label.pack_forget()
        self.button.pack_forget()
        self.emailEntry.pack_forget()
        self.emailLabel.pack_forget()
        self.passwordLabel.pack_forget()
        self.passwordEntry.pack_forget()
        self.button3.pack_forget()
        self.button2.pack_forget()
        self.label = tk.Label(self, text="Login Page", font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.button = tk.Button(self, text="Go to the welcome page", command=lambda: self.controller.show_frame("WelcomePage"))
        self.emailLabel = tk.Label(self, text="Email", font=self.controller.paragraph_font)
        self.emailEntry = tk.Entry(self, width=20)
        self.passwordLabel = tk.Label(self, text="Password", font=self.controller.paragraph_font)
        self.passwordEntry = tk.Entry(self, width=20, show="*")
        self.button2 = tk.Button(self, text="Login", command=lambda: LoginPage.logIn(self.emailEntry.get(), self.passwordEntry.get(), self.controller))
        self.button3 = tk.Button(self, text="Go to Signup Page", command=lambda: self.controller.show_frame("SignupPage"))
        self.button.pack()
        self.emailLabel.pack()
        self.emailEntry.pack()
        self.passwordLabel.pack()
        self.passwordEntry.pack()
        self.button2.pack()
        self.button3.pack()

    def logIn(email, password, controller) :
        global currentUser
        if db.logIn(email, password) :
            currentUser = email
            if db.isCurator(email) :
                isCurator = True
                controller.show_frame("CuratorHome")
            else :
                controller.show_frame("VisitorHome")
        elif db.adminLogin(email, password) :
            isAdmin = True
            currentUser = email
            controller.show_frame("AdminHome")
        else :
            showinfo("Error", "Incorrect login")


class SignupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Signup Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the welcome page", command=lambda: controller.show_frame("WelcomePage"))
        emailLabel = tk.Label(self, text="Email", font=controller.paragraph_font)
        emailEntry = tk.Entry(self, width=20)
        passwordLabel = tk.Label(self, text="Password", font=controller.paragraph_font)
        passwordEntry = tk.Entry(self, width=20, show="*")
        creditCardLabel = tk.Label(self, text="Credit Card", font=controller.paragraph_font)
        creditCardEntry = tk.Entry(self, width=20)
        expMonLabel = tk.Label(self, text="Exp. Month", font=controller.paragraph_font)
        expMonEntry = tk.Entry(self, width=20)
        expYearLabel = tk.Label(self, text="Exp. Year", font=controller.paragraph_font)
        expYearEntry = tk.Entry(self, width=20)
        secCodeLabel = tk.Label(self, text="Security Code", font=controller.paragraph_font)
        secCodeEntry = tk.Entry(self, width=20)
        button2 = tk.Button(self, text="SignUp", command=lambda: SignupPage.signUp(emailEntry.get(), passwordEntry.get(), creditCardEntry.get(), expMonEntry.get(), expYearEntry.get(), secCodeEntry.get(), controller))
        button.pack()
        emailLabel.pack()
        emailEntry.pack()
        passwordLabel.pack()
        passwordEntry.pack()
        creditCardLabel.pack()
        creditCardEntry.pack()
        expMonLabel.pack()
        expMonEntry.pack()
        expYearLabel.pack()
        expYearEntry.pack()
        secCodeLabel.pack()
        secCodeEntry.pack()
        button2.pack()

    def signUp(email, password, credCard, expMon, expYear, secCode, controller) :
        if db.addNewVisitor(email, password, credCard, expMon, expYear, secCode) :
            currentUser = email
            controller.show_frame("VisitorHome")
        else :
            showinfo("Error", "Incorrect signup")


class VisitorHome(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Welcome Visitor " + currentUser, font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.museumLabel = tk.Label(self, text="Museums", font=controller.paragraph_font)
        self.museumLabel.pack()
        museumList = db.listOfMuseums()
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu1.pack()
        self.viewMusBut = tk.Button(self, text="View Museum", command=lambda: self.changePage("OneMuseumPage", self.dropVar.get()))
        self.viewMusBut.pack()
        self.viewAllMuseums = tk.Button(self, text="View All Museums", command=lambda: print("View all"))
        self.viewAllMuseums.pack()
        self.viewMyTickets = tk.Button(self, text="My Tickets", command=lambda: print("tickets"))
        self.viewMyTickets.pack()
        self.viewMyReviews = tk.Button(self, text="My Reviews", command=lambda: print("reviews"))
        self.viewMyReviews.pack()
        self.manageAccount = tk.Button(self, text="Manage Account", command=lambda: print("reviews"))
        self.manageAccount.pack()

    def changePage(self, page, museum_name) :
        global currentMuseum
        currentMuseum = museum_name
        self.controller.show_frame(page)

    def update(self) :
        self.label.pack_forget()
        self.museumLabel.pack_forget()
        self.dropMenu1.pack_forget()
        self.viewMusBut.pack_forget()
        self.viewAllMuseums.pack_forget()
        self.viewMyTickets.pack_forget()
        self.viewMyReviews.pack_forget()
        self.manageAccount.pack_forget()
        self.label = tk.Label(self, text="Welcome Visitor " + currentUser)
        self.label.pack(side="top", fill="x", pady=10)
        self.museumLabel = tk.Label(self, text="Museums")
        self.museumLabel.pack()
        museumList = db.listOfMuseums()
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu1.pack()
        self.viewMusBut = tk.Button(self, text="View Museum", command=lambda: self.changePage("OneMuseumPage", self.dropVar.get()))
        self.viewMusBut.pack()
        self.viewAllMuseums = tk.Button(self, text="View All Museums", command=lambda: self.controller.show_frame("AllMuseums"))
        self.viewAllMuseums.pack()
        self.viewMyTickets = tk.Button(self, text="My Tickets", command=lambda: self.controller.show_frame("TicketHistoryPage"))
        self.viewMyTickets.pack()
        self.viewMyReviews = tk.Button(self, text="My Reviews", command=lambda: self.controller.show_frame("ReviewHistoryPage"))
        self.viewMyReviews.pack()
        self.manageAccount = tk.Button(self, text="Manage Account", command=lambda: self.controller.show_frame("ManageAccountPage"))
        self.manageAccount.pack()


class CuratorHome(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Welcome Curator " + currentUser, font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.museumLabel = tk.Label(self, text="Museums", font=controller.paragraph_font)
        self.museumLabel.pack()
        museumList = db.listOfMuseums()
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu1.pack()
        self.viewMusBut = tk.Button(self, text="View Museum", command=lambda: self.changePage("OneMuseumPage", self.dropVar.get()))
        self.viewMusBut.pack()
        self.viewAllMuseums = tk.Button(self, text="View All Museums", command=lambda: print("View all"))
        self.viewAllMuseums.pack()
        self.viewMyTickets = tk.Button(self, text="My Tickets", command=lambda: print("tickets"))
        self.viewMyTickets.pack()
        self.viewMyReviews = tk.Button(self, text="My Reviews", command=lambda: print("reviews"))
        self.viewMyReviews.pack()
        self.manageAccount = tk.Button(self, text="Manage Account", command=lambda: print("reviews"))
        self.manageAccount.pack()
        self.mymuseBut = tk.Button(self, text="My Museums", command=lambda: print("my museum_name"))
        self.mymuseBut.pack()

    def changePage(self, page, museum_name) :
        global currentMuseum
        currentMuseum = museum_name
        self.controller.show_frame(page)

    def update(self) :
        self.label.pack_forget()
        self.museumLabel.pack_forget()
        self.dropMenu1.pack_forget()
        self.viewMusBut.pack_forget()
        self.viewAllMuseums.pack_forget()
        self.viewMyTickets.pack_forget()
        self.viewMyReviews.pack_forget()
        self.manageAccount.pack_forget()
        self.mymuseBut.pack_forget()
        self.label = tk.Label(self, text="Welcome Curator " + currentUser)
        self.label.pack(side="top", fill="x", pady=10)
        self.museumLabel = tk.Label(self, text="Museums")
        self.museumLabel.pack()
        museumList = db.listOfMuseums()
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu1.pack()
        self.viewMusBut = tk.Button(self, text="View Museum", command=lambda: self.changePage("OneMuseumPage", self.dropVar.get()))
        self.viewMusBut.pack()
        self.viewAllMuseums = tk.Button(self, text="View All Museums", command=lambda: self.controller.show_frame("AllMuseums"))
        self.viewAllMuseums.pack()
        self.viewMyTickets = tk.Button(self, text="My Tickets", command=lambda: self.controller.show_frame("TicketHistoryPage"))
        self.viewMyTickets.pack()
        self.viewMyReviews = tk.Button(self, text="My Reviews", command=lambda: self.controller.show_frame("ReviewHistoryPage"))
        self.viewMyReviews.pack()
        self.manageAccount = tk.Button(self, text="Manage Account", command=lambda: self.controller.show_frame("ManageAccountPage"))
        self.manageAccount.pack()
        self.mymuseBut = tk.Button(self, text="My Museums", command=lambda: self.controller.show_frame("MyMuseumsPage"))
        self.mymuseBut.pack()


class AdminHome(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Admin Home " + currentUser, font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.button = tk.Button(self, text="Accept Curator Request", command=lambda: self.controller.show_frame("AdminCurPage"))
        self.button.pack()
        self.button2 = tk.Button(self, text="Add Museum", command=lambda: print("2"))
        self.button2.pack()
        self.button3 = tk.Button(self, text="Delete Museum", command=lambda: print("3"))
        self.button3.pack()
        self.button4 = tk.Button(self, text="Log Out", command=lambda: logOut(self.controller))
        self.button4.pack()

    def update(self) :
        self.label.pack_forget()
        self.button.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()
        self.button4.pack_forget()
        self.label = tk.Label(self, text="Welcome Admin " + currentUser, font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.button = tk.Button(self, text="Accept Curator Request", command=lambda: self.controller.show_frame("AdminCurPage"))
        self.button.pack()
        self.button2 = tk.Button(self, text="Add Museum", command=lambda: self.controller.show_frame("NewMuseumPage"))
        self.button2.pack()
        self.button3 = tk.Button(self, text="Delete Museum", command=lambda: self.controller.show_frame("DeleteMuseumForm"))
        self.button3.pack()
        self.button4 = tk.Button(self, text="Log Out", command=lambda: logOut(self.controller))
        self.button4.pack()


def logOut(controller) :
    global currentUser
    global isCurator
    global isAdmin
    currentUser = ""
    isCurator = False
    isAdmin = False
    controller.show_frame("WelcomePage")


class OneMuseumPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = currentMuseum, font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.purchaseButton = tk.Button(self, text = "Purchase Ticket", command = lambda: self.purchasePopUp(isPurchased))
        self.purchaseButton.pack()
        self.reviewButton = tk.Button(self, text = "Review Museum", command = lambda: controller.show_frame("MakeReviewPage"))
        self.reviewButton.pack()
        self.viewReviewsButton = tk.Button(self, text = "View Others Reviews", command = lambda: controller.show_frame("ViewReviews"))
        self.viewReviewsButton.pack()
        self.exhibit = tk.Label(self, text = "", font = self.controller.title_font)
        self.exhibit.pack()
        if db.isCurator(currentUser) :
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("CuratorHome"))
        else :
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("VisitorHome"))
        self.backButton.pack()

    def update(self) :
        self.title.pack_forget()
        self.purchaseButton.pack_forget()
        self.reviewButton.pack_forget()
        self.viewReviewsButton.pack_forget()
        self.exhibit.pack_forget()
        self.backButton.pack_forget()
        exhibits = db.viewSpecificMuseum(currentMuseum)
        textInput = ""
        self.exhibit = tk.Label(self, text = "", font = self.controller.title_font)
        for row in exhibits :
            textInput += row[0] + "      " + str(row[1]) + "      " + row[2] + "\n"
        self.exhibit = tk.Label(self, text = textInput, font = self.controller.paragraph_font)
        self.title = tk.Label(self, text = currentMuseum, font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.exhibit.pack()
        self.purchaseButton = tk.Button(self, text = "Purchase Ticket", command = lambda: self.purchaseTicket(currentUser, currentMuseum))
        self.purchaseButton.pack()
        self.reviewButton = tk.Button(self, text = "Review Museum", command = lambda: self.controller.show_frame("MakeReviewPage"))
        self.reviewButton.pack()
        self.viewReviewsButton = tk.Button(self, text = "View Others Reviews", command = lambda: self.controller.show_frame("ViewReviews"))
        self.viewReviewsButton.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("VisitorHome"))
        self.backButton.pack()

    def purchaseTicket(self, user, museum) :
        if db.purchaseTicket(user, museum, 10) :
            showinfo("Purchase Info", "Thank you for Purchasing a Ticket to " + currentMuseum)
        else :
            showinfo("Purchase Info", "You already have a ticket " + currentMuseum)


class MakeReviewPage(tk.Frame):

    x = -1;

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Review for " + currentMuseum, font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.ratingLabel = tk.Label(self, text="Rating*: ", font=controller.paragraph_font)
        self.ratingLabel.pack()
        self.r1button = tk.Button(self, text = "1 Star", command=lambda: self.makeRate(1))
        self.r2button = tk.Button(self, text = "2 Star", command=lambda: self.makeRate(2))
        self.r3button = tk.Button(self, text = "3 Star", command=lambda: self.makeRate(3))
        self.r4button = tk.Button(self, text = "4 Star", command=lambda: self.makeRate(4))
        self.r5button = tk.Button(self, text = "5 Star", command=lambda: self.makeRate(5))
        self.r1button.pack()
        self.r2button.pack()
        self.r3button.pack()
        self.r4button.pack()
        self.r5button.pack()
        self.commentLabel = tk.Label(self, text="Comment: ", font=controller.paragraph_font)
        self.commentLabel.pack()
        self.commentEntry = tk.Entry(self, width=10)
        self.commentEntry.pack()
        self.submitButton = tk.Button(self, text="Submit Review", command=lambda: db.makeReview(currentUser, currentMuseum, commentEntry.get(), self.x))
        self.submitButton.pack()
        self.backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("OneMuseumPage"))
        self.backButton.pack()

    def makeRate(self, y) :
        self.x = y

    def update(self) :
        self.r1button.pack_forget()
        self.r2button.pack_forget()
        self.r3button.pack_forget()
        self.r4button.pack_forget()
        self.r5button.pack_forget()
        self.commentLabel.pack_forget()
        self.commentEntry.pack_forget()
        self.submitButton.pack_forget()
        self.backButton.pack_forget()
        self.label.pack_forget()
        self.ratingLabel.pack_forget()
        self.label = tk.Label(self, text="Review for " + currentMuseum, font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.ratingLabel = tk.Label(self, text="Rating*: ", font=self.controller.paragraph_font)
        self.ratingLabel.pack()
        self.r1button = tk.Button(self, text = "1 Star", command=lambda: self.makeRate(1))
        self.r2button = tk.Button(self, text = "2 Star", command=lambda: self.makeRate(2))
        self.r3button = tk.Button(self, text = "3 Star", command=lambda: self.makeRate(3))
        self.r4button = tk.Button(self, text = "4 Star", command=lambda: self.makeRate(4))
        self.r5button = tk.Button(self, text = "5 Star", command=lambda: self.makeRate(5))
        self.r1button.pack()
        self.r2button.pack()
        self.r3button.pack()
        self.r4button.pack()
        self.r5button.pack()
        self.commentLabel = tk.Label(self, text="Comment: ", font=self.controller.paragraph_font)
        self.commentLabel.pack()
        self.commentEntry = tk.Entry(self, width=10)
        self.commentEntry.pack()
        self.submitButton = tk.Button(self, text="Submit Review", command=lambda: self.makeReview(currentUser, currentMuseum, self.commentEntry.get(), self.x))
        self.submitButton.pack()
        self.backButton = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("OneMuseumPage"))
        self.backButton.pack()

    def makeReview(self, email, museum, comment, rate) :
        if db.makeReview(email, museum, comment, rate) :
            showinfo("Review Info", "Thank you for reviwing " + currentMuseum)
        else :
            showinfo("Review Info", "You can not review " + currentMuseum)

class ViewReviews(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = currentMuseum, font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.reviews = tk.Label(self, text = "Comment           Rating", font = self.controller.title_font)
        self.reviews.pack()
        backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("OneMuseumPage"))
        backButton.pack()

    def update(self) :
        self.title.pack_forget()
        self.reviews.pack_forget()
        self.title = tk.Label(self, text = currentMuseum, font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        review = db.viewAllReviewsForMusuem(currentMuseum)
        textInput = ""
        for row in review :
            textInput += row[0] + "           " + str(row[1]) + "\n"
        self.reviews = tk.Label(self, text = "Comment           Rating\n" + textInput, font = self.controller.paragraph_font)
        self.reviews.pack()


class AllMuseums(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = "All Museums", font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        museumList = db.listOfMuseums()
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu1.pack()
        self.viewMusBut = tk.Button(self, text="View Museum", command=lambda: self.changePage("OneMuseumPage", self.dropVar.get()))
        self.viewMusBut.pack()
        self.museumTable = tk.Label(self, text = "", font = self.controller.paragraph_font)
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("VisitorHome"))
        self.backButton.pack()

    def changePage(self, page, museum_name) :
        global currentMuseum
        currentMuseum = museum_name
        self.controller.show_frame(page)

    def update(self):
        self.museumTable.pack_forget()
        self.dropMenu1.pack_forget()
        self.viewMusBut.pack_forget()
        self.backButton.pack_forget()
        self.title.pack_forget()
        self.title = tk.Label(self, text = "All Museums", font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        data = db.viewAllMuseums()
        textInput = "Museum Name          Rating \n"
        for row in data:
            textInput += row[0] + "          " + str(row[1]) + "\n"
        self.museumTable = tk.Label(self, text = textInput, font = self.controller.paragraph_font)
        self.museumTable.pack()
        museumList = db.listOfMuseums()
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu1.pack()
        self.viewMusBut = tk.Button(self, text="View Museum", command=lambda: self.changePage("OneMuseumPage", self.dropVar.get()))
        self.viewMusBut.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("VisitorHome"))
        self.backButton.pack()


class TicketHistoryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text="My Tickets", font=self.controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        self.tickets = tk.Label(self, text = "Museum Ticket          Purchase Date         Amount\n", font = self.controller.paragraph_font)
        self.tickets.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("VisitorHome"))
        self.backButton.pack()

    def update(self):
        self.title.pack_forget()
        self.tickets.pack_forget()
        self.backButton.pack_forget()
        self.title = tk.Label(self, text="My Tickets", font=self.controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        tickets = db.viewTicketHistory(currentUser)
        textInput = ""
        for row in tickets :
            textInput += row[0] + "           " + str(row[1]) + "         " + row[2] + "\n"
        self.tickets = tk.Label(self, text = "Museum Ticket        Purchase date           Amount\n" + textInput, font = self.controller.paragraph_font)
        self.tickets.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("VisitorHome"))
        self.backButton.pack()


class ReviewHistoryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text="My Reviews", font=controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        self.reviews = tk.Label(self, text = "Museum Review          Review         Rating\n", font = self.controller.title_font)
        self.reviews.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("VisitorHome"))
        self.backButton.pack()

    def update(self):
        self.title.pack_forget()
        self.reviews.pack_forget()
        self.backButton.pack_forget()
        self.title = tk.Label(self, text="My Reviews", font=self.controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        reviews = db.viewReviewHistory(currentUser)
        textInput = ""
        for row in reviews :
            textInput += row[0] + "           " + row[1] + "           " + str(row[2]) + "\n"
        self.reviews = tk.Label(self, text = "Museum Review        Review          Rating\n" + textInput, font = self.controller.paragraph_font)
        self.reviews.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("VisitorHome"))
        self.backButton.pack()


class ManageAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = "Manage Account", font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady=10)
        self.button = tk.Button(self, text="Log Out", command=lambda: logOut(controller))
        self.button.pack()
        self.curatorButton = tk.Button(self, text = "Curator Request", command = lambda: controller.show_frame("CuratorRequestPage"))
        self.deleteButton = tk.Button(self, text = "Delete Account", command = lambda: controller.show_frame("DeleteAccountPage"))
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("VisitorHome"))
        self.curatorButton.pack()
        self.deleteButton.pack()
        self.backButton.pack()

    def update(self):
        self.button.pack_forget()
        self.title.pack_forget()
        self.curatorButton.pack_forget()
        self.deleteButton.pack_forget()
        self.backButton.pack_forget()
        self.title = tk.Label(self, text = "Manage Account", font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady=10)
        self.button = tk.Button(self, text="Log Out", command=lambda: logOut(self.controller))
        self.button.pack()
        self.curatorButton = tk.Button(self, text = "Curator Request", command = lambda: self.controller.show_frame("CuratorRequestPage"))
        self.deleteButton = tk.Button(self, text = "Delete Account", command = lambda: self.controller.show_frame("DeleteAccountPage"))
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("VisitorHome"))
        self.curatorButton.pack()
        self.deleteButton.pack()
        self.backButton.pack()


class CuratorRequestPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = "Curator Request", font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.backButton = tk.Button(self, text="Back", command = lambda: controller.show_frame("ManageAccountPage"))
        self.backButton.pack()
        museumList = db.listOfMuseums()
        self.dropVar = tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu = tk.OptionMenu(self, self.dropVar, *museumList)
        self.submitButton = tk.Button(self, text = "Submit", command = lambda: self.CuratorRequestPage.submitReq())

    def submitReq(self):
        if db.makeCuratorRequest(currentUser, self.dropVar.get()) :
            if db.checkForCurator(self.dropVar.get()) :
                showinfo("Curator Request", "Already has one but has submit")
            else :
                showinfo("Curator Request", "Submitted")
        else :
            showinfo("Curator Request", "Failed")

    def update(self):
        self.title.pack_forget()
        self.backButton.pack_forget()
        self.dropMenu.pack_forget()
        self.submitButton.pack_forget()
        self.title = tk.Label(self, text = "Curator Request", font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        museumList = db.listOfMuseums()
        self.dropVar = tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu = tk.OptionMenu(self, self.dropVar, *museumList)
        self.dropMenu.pack(side = "top", fill = "x", pady = 10)
        self.backButton = tk.Button(self, text="Back", command = lambda: self.controller.show_frame("ManageAccountPage"))
        self.submitButton = tk.Button(self, text = "Submit", command = lambda: CuratorRequestPage.submitReq(self))
        self.submitButton.pack()
        self.backButton.pack()


class DeleteAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = "Manage Account", font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.yesButton = tk.Button(self, text = "Yes, Delete it!", command = lambda: self.deleted())
        self.noButton = tk.Button(self, text = "No, Don't Delete it!", command = lambda: controller.show_frame("ManageAccountPage"))
        self.yesButton.pack()
        self.noButton.pack()
        self.t = tk.Text(self, height = 5, width = 30)

    def deleted(self):
        db.deleteVisitor(currentUser)
        self.controller.show_frame("LoginPage")

    def update(self):
        self.title.pack_forget()
        self.t.pack_forget()
        self.yesButton.pack_forget()
        self.noButton.pack_forget()
        self.title = tk.Label(self, text = "Manage Account", font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        words = "Are You Sure?\n\nDeleting your account will get rid of all of your reviews,\nticket history, and credit card information. Do you still\nwish to proceed?"
        self.t = tk.Label(self, text = words, font = self.controller.paragraph_font)
        self.t.pack()
        self.yesButton = tk.Button(self, text = "Yes, Delete it!", command = lambda: self.deleted())
        self.noButton = tk.Button(self, text = "No, Don't Delete it!", command = lambda: self.controller.show_frame("ManageAccountPage"))
        self.yesButton.pack()
        self.noButton.pack()


class MyMuseumsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text="My Museums", font=controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        self.museums = tk.Label(self, text = "Museum          Exhibit Counts         Rating\n", font = controller.title_font)
        self.museums.pack()
        self.museumList = []
        museums = db.listOfMuseums()
        for row in museums :
            self.museumList.append(row[0])
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(self.museumList[0])
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *self.museumList)
        self.dropMenu1.pack()
        self.goTobut = tk.Button(self, text = "Go to museum", command = lambda: MyMuseumsPage.changePage("MySpecificMuseum", self.dropVar.get()))
        self.goTobut.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("VisitorHome"))

    def changePage(self, page, museum_name) :
        global currentMuseum
        currentMuseum = museum_name
        self.controller.show_frame(page)

    def update(self):
        self.title.pack_forget()
        self.dropMenu1.pack_forget()
        self.goTobut.pack_forget()
        self.museums.pack_forget()
        self.backButton.pack_forget()
        self.title = tk.Label(self, text="My Museums", font=self.controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        museums = db.viewMyMuseums(currentUser)
        textInput = ""
        for row in museums :
            textInput += row[0] + "           " + str(row[1]) + "           " + str(row[2]) + "\n"
        self.museums = tk.Label(self, text = "Museum        Exhibit Counts          Rating\n" + textInput, font = self.controller.paragraph_font)
        self.museums.pack()
        self.museumList = []
        for row in museums :
            self.museumList.append(row[0])
        self.dropVar=tk.StringVar(self)
        self.dropVar.set(self.museumList[0]) # default value
        self.dropMenu1 = tk.OptionMenu(self, self.dropVar, *self.museumList)
        self.dropMenu1.pack()
        self.goTobut = tk.Button(self, text = "Go to museum", command = lambda: MyMuseumsPage.changePage(self, "MySpecificMuseum", self.dropVar.get()))
        self.goTobut.pack()
        if db.isCurator(currentUser):
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("CuratorHome"))
        else:
            self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("VisitorHome"))
        self.backButton.pack()


class MySpecificMuseum(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = currentMuseum, font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.addExhibitButton = tk.Button(self, text = "Add Exhibit", command = lambda: controller.show_frame("NewExhibitPage"))
        self.addExhibitButton.pack()
        self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("MyMuseumsPage"))
        self.backButton.pack()
        self.exhibit = tk.Label(self, text = "", font = self.controller.title_font)
        dropVar=tk.StringVar(self)
        dropVar.set("-")
        exhibitList = ["-"]
        self.dropMenu1 = tk.OptionMenu(self, dropVar, *exhibitList)
        self.removeButton = tk.Button(self, text = "Remove ", command = lambda: self.removeFunc(currentMuseum, row[0]))

    def update(self):
        self.backButton.pack_forget()
        self.title.pack_forget()
        self.addExhibitButton.pack_forget()
        self.exhibit.pack_forget()
        self.removeButton.pack_forget()
        self.dropMenu1.pack_forget()
        exhibits = db.viewSpecificMuseum(currentMuseum)
        textInput = ""
        exhibitList = []
        self.exhibit = tk.Label(self, text = "", font = self.controller.title_font)
        for row in exhibits :
             textInput += row[0] + "      " + str(row[1]) + "      " + row[2] + "\n"
             exhibitList.append(row[0])
        self.exhibit = tk.Label(self, text = textInput, font = self.controller.paragraph_font)
        self.title = tk.Label(self, text = currentMuseum, font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.exhibit.pack()
        dropVar=tk.StringVar(self)
        if exhibitList :
            dropVar.set(exhibitList[0])
        else :
            dropVar.set("-")
            exhibitList.append("-")
        self.dropMenu1 = tk.OptionMenu(self, dropVar, *exhibitList)
        self.dropMenu1.pack()
        self.removeButton = tk.Button(self, text = "Remove", command = lambda: self.removeFunc(currentMuseum, dropVar.get()))
        self.removeButton.pack()
        self.addExhibitButton = tk.Button(self, text = "Add Exhibit", command = lambda: self.controller.show_frame("NewExhibitPage"))
        self.addExhibitButton.pack()
        self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("MyMuseumsPage"))
        self.backButton.pack()

    def removeFunc(self, museum, exhibit):
        if "-" is not exhibit :
            db.deleteExhibit(museum, exhibit)
            showinfo("Alert", "You have successfully removed " + exhibit + "\nfrom the museum " + museum)
            self.controller.show_frame("MySpecificMuseum")


class NewExhibitPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="New Exhibit Form", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.nameLabel = tk.Label(self, text="Name*: ", font=controller.paragraph_font)
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self, width=10)
        self.nameEntry.pack()
        self.yearLabel = tk.Label(self, text="Year*: ", font=controller.paragraph_font)
        self.yearLabel.pack()
        self.yearEntry = tk.Entry(self, width=10)
        self.yearEntry.pack()
        self.linkLabel = tk.Label(self, text="Link to More Information: ",  font=controller.paragraph_font)
        self.linkLabel.pack()
        self.linkEntry = tk.Entry(self, width=10)
        self.linkEntry.pack()
        self.submitButton = tk.Button(self, text="Submit Exhibit", command=lambda: NewExhibitPage.add(currentMuseum, nameEntry.get(), yearEntry.get(), linkEntry.get()))
        self.submitButton.pack()
        self.backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("MySpecificMuseum"))
        self.backButton.pack()

    def add(museum, name, year, link) :
        if db.addExhibit(museum, name, year, link) :
            showinfo("Adding Exhibit", "Success")
        else :
            showinfo("Adding Exhibit", "Failed")

    def update(self) :
        self.label.pack_forget()
        self.nameLabel.pack_forget()
        self.nameEntry.pack_forget()
        self.yearLabel.pack_forget()
        self.yearEntry.pack_forget()
        self.linkLabel.pack_forget()
        self.linkEntry.pack_forget()
        self.submitButton.pack_forget()
        self.backButton.pack_forget()
        self.label = tk.Label(self, text="New Exhibit Form", font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.nameLabel = tk.Label(self, text="Name*: ", font=self.controller.paragraph_font)
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self, width=10)
        self.nameEntry.pack()
        self.yearLabel = tk.Label(self, text="Year*: ", font=self.controller.paragraph_font)
        self.yearLabel.pack()
        self.yearEntry = tk.Entry(self, width=10)
        self.yearEntry.pack()
        self.linkLabel = tk.Label(self, text="Link to More Information: ",  font=self.controller.paragraph_font)
        self.linkLabel.pack()
        self.linkEntry = tk.Entry(self, width=10)
        self.linkEntry.pack()
        self.submitButton = tk.Button(self, text="Submit Exhibit", command=lambda: NewExhibitPage.add(currentMuseum, self.nameEntry.get(), self.yearEntry.get(), self.linkEntry.get()))
        self.submitButton.pack()
        self.backButton = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("MySpecificMuseum"))
        self.backButton.pack()


class AdminCurPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text="Curator Requests", font=controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        dropVar = tk.StringVar(self)
        dropVar.set("-")
        self.curReqs = tk.Label(self, text = "", font = self. controller.title_font)
        curReqList = ["-"]
        self.dropMenu1 = tk.OptionMenu(self, dropVar, *curReqList)
        self.acceptButton = tk.Button(self, text="Accept", command=lambda : acceptReq(dropVar))
        self.acceptButton.pack()
        self.rejectButton = tk.Button(self, text="Reject", command=lambda : rejectRequest(dropVar))
        self.backButton = tk.Button(self, text="Back", command=lambda : controller.show_frame("AdminHome"))
        self.backButton.pack()

    def update(self):
        self.backButton.pack_forget()
        self.title.pack_forget()
        self.acceptButton.pack_forget()
        self.rejectButton.pack_forget()
        self.dropMenu1.pack_forget()
        curReqs = db.viewCuratorRequests()
        textInput = ""
        curReqList = []
        self.curReqs = tk.Label(self, text = "", font = self.controller.title_font)
        for row in curReqs:
            textInput = row[0] + "===" + row[1]
            curReqList.append(textInput)
        self.title = tk.Label(self, text="Curator Requests", font=self.controller.title_font)
        self.title.pack(side="top", fill ="x", pady=10)
        self.curReqs.pack()
        dropVar=tk.StringVar(self)
        if curReqList:
            dropVar.set(curReqList[0])
        else:
            dropVar.set("-")
            curReqList.append("-")
        self.dropMenu1 = tk.OptionMenu(self, dropVar, *curReqList)
        self.dropMenu1.pack()
        self.acceptButton = tk.Button(self, text="Accept", command=lambda : AdminCurPage.acceptReq(self, dropVar.get()))
        self.acceptButton.pack()
        self.rejectButton = tk.Button(self, text="Reject", command=lambda : AdminCurPage.rejectReq(self, dropVar.get()))
        self.rejectButton.pack()
        self.backButton.pack()

    def acceptReq(self, dropVar ):
        dvlist = dropVar.split("===")
        if len(dvlist) != 2 :
            return
        if db.acceptCuratorRequest(dvlist[0].strip(), dvlist[1].strip()):
            showinfo("Approval", "You have successfully added user " + dvlist[0].strip() + " as the curator for museum " + dvlist[1].strip() + "!")
            self.controller.show_frame("AdminCurPage")
        else:
            showinfo("Approval", "Acceptance Failed")

    def rejectReq(self, dropVar):
        dvlist = dropVar.split("===")
        if len(dvlist) != 2 :
            return
        if db.rejectCuratorRequest(dvlist[0].strip(), dvlist[1].strip()):
            showinfo("Rejection", "You have successfully rejected user " + dvlist[0].strip() + " as the curator for museum " + dvlist[1].strip() + "!")
            self.controller.show_frame("AdminCurPage")
        else:
            showinfo("Rejection", "Rejection Failed")


class NewMuseumPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="New Museum Form", font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.nameLabel = tk.Label(self, text="Name*: ", font=self.controller.paragraph_font)
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self, width=10)
        self.nameEntry.pack()
        self.submitButton = tk.Button(self, text="Submit Exhibit", command=lambda: NewMuseumPage.addMus(self, self.nameEntry.get(), None))
        self.submitButton.pack()
        self.backButton = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("AdminHome"))
        self.backButton.pack()

    def addMus(self, name, email) :
        if db.addNewMuseum(name, email) :
            showinfo("Addition", "You have successfully added " + name + "!")
            self.controller.show_frame("NewMuseumPage")
        else :
            showinfo("Addition", "You have failed at adding " + name + "!")

    def update(self) :
        self.label.pack_forget()
        self.nameLabel.pack_forget()
        self.nameEntry.pack_forget()
        self.submitButton.pack_forget()
        self.backButton.pack_forget()
        self.label = tk.Label(self, text="New Museum Form", font=self.controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.nameLabel = tk.Label(self, text="Name*: ", font=self.controller.paragraph_font)
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self, width=10)
        self.nameEntry.pack()
        self.submitButton = tk.Button(self, text="Submit Exhibit", command=lambda: NewMuseumPage.addMus(self, self.nameEntry.get(), None))
        self.submitButton.pack()
        self.backButton = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("AdminHome"))
        self.backButton.pack()


class DeleteMuseumForm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = "Delete Museum Form", font = controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        self.deleteButton = tk.Button(self, text = "Delete Museum", command = lambda: db.deleteMuseum(value))
        self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("AdminHome"))
        self.deleteButton.pack()
        self.backButton.pack()
        self.museumEntry = tk.Entry(self, text="", width=10)
        self.dropVar = tk.StringVar(self)
        self.dropVar.set("-")
        museumList = ["-"]
        self.dropMenu = tk.OptionMenu(self, self.dropVar, *museumList)

    def update(self):
        self.title.pack_forget()
        self.museumEntry.pack_forget()
        self.dropMenu.pack_forget()
        self.deleteButton.pack_forget()
        self.backButton.pack_forget()
        self.title = tk.Label(self, text = "Delete Museum Form", font = self.controller.title_font)
        self.title.pack(side = "top", fill = "x", pady = 10)
        museumList = db.listOfMuseums()
        self.dropVar = tk.StringVar(self)
        self.dropVar.set(museumList[0])
        self.dropMenu = tk.OptionMenu(self, self.dropVar, *museumList, command = lambda: v.set(currentMuseum))
        self.dropMenu.pack()
        self.deleteButton = tk.Button(self, text = "Delete Museum", command = lambda: DeleteMuseumForm.delMuse(self, self.dropVar.get()))
        self.backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame("AdminHome"))
        self.deleteButton.pack()
        self.backButton.pack()

    def delMuse(self, name) :
        if db.deleteMuseum(name) :
            showinfo("Deletation", "You have successfully deleted " + name + "!")
            self.controller.show_frame("DeleteMuseumForm")
        else :
            showinfo("Addition", "You have failed at delted " + name + "!")


if __name__ == "__main__":
    app = Controller()
    app.title("BMTRS")
    app.geometry("750x500")
    app.mainloop()