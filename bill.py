from tkinter import *
import time
from tkinter import messagebox
import os
from random import randint
root = Tk()
root.geometry("1012x500+0+0")
root.configure(bg='black')
root.title("Dugout Restaurant Billing")
bg = PhotoImage(file = "Restaurant.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)
Tops = Frame(root, width=1350, height=50, bd=4,bg='black', relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root,width=1350, height=50, bd=4, bg='black',relief="raise")
Bottoms.pack(side=BOTTOM)
f1 = Frame(root, width=900, height=650,bd=4,relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=900, height=330,bd=1,relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=1, relief="raise")
f2a.pack(side=BOTTOM)
f1aa = Frame(f1a, width=450, height=430, bd=2, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=450, height=430, bd=2, relief="raise")
f1ab.pack(side=RIGHT)
f2aa = Frame(f2a, width=450, height=330,bd=2, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330,bd=2, relief="raise")
f2ab.pack(side=LEFT)
# # f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
# # f2.pack(side=BOTTOM)
lblInfo = Label(Tops, font=('arial', 20),bg='green',fg='white', text="Restaurant Billing System",anchor='w')
lblInfo.grid(row=0, column=0)
btInfo = Label(Bottoms, font=('arial', 20),bg='green',fg='white',bd=1, text="*COPYRIGHT-encripted**",anchor='w')
btInfo.grid(row=1, column=0)
# # # ==============================Variables=====================
PaymentRef = StringVar()
idly = StringVar()
biryani = StringVar()
paneer_butter_masala = StringVar()
nimbu_pani = StringVar()
masala_bhindi = StringVar()
costidly = StringVar()
costbiryani = StringVar()
costpaneer_butter_masala = StringVar()
costnimbu_pani = StringVar()
costmasala_bhindi = StringVar()
dateRef = StringVar()
subTotal = StringVar()
vat = StringVar()
totalPrice = StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y"))
operator = ""
vat.set(0)
idly.set(0)
biryani.set(0)
paneer_butter_masala.set(0)
nimbu_pani.set(0)
masala_bhindi.set(0)
subTotal.set(0)
totalPrice.set(0)
costidly.set(30)
costbiryani.set(180)
costnimbu_pani.set(20)
costpaneer_butter_masala.set(180)
costmasala_bhindi.set(100)
# # # =============================Functions==================
x = ''
def tPrice():
    cBprice = int(costidly.get())
    bBprice = int(costbiryani.get())
    fFprice = int(costpaneer_butter_masala.get())
    sDprice = int(costnimbu_pani.get())
    aAprice = int(costmasala_bhindi.get())
    cBno = int(idly.get())
    bBno = int(biryani.get())
    fFno = int(paneer_butter_masala.get())
    sDno = int(nimbu_pani.get())
    aAno = int(masala_bhindi.get())
    tempVat = int(vat.get())
    subPrice = (cBprice * cBno + bBprice * bBno + fFprice * fFno + sDprice * sDno + aAprice * aAno)
    totalCost = str('%d' % subPrice)
    totalCostwithVat = str('%d' % (subPrice + (subPrice * tempVat) / 100))
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)
def iExit():
    qexit = messagebox.askyesno("WARNING!", "Are You Sure, Do you want to exit?")
    if qexit > 0:
        root.destroy()
        return
m = ''        
def reset():
    global m
    m = m + '1'
    PaymentRef.set("")
    idly.set(0)
    biryani.set(0)
    paneer_butter_masala.set(0)
    nimbu_pani.set(0)
    masala_bhindi.set(0)
    vat.set(0)
    subTotal.set(0)
    totalPrice.set(0)
y = randint(1, 9999)    
def refNo():
    global y
    randomRef = str(y)
    PaymentRef.set("BILL " + randomRef)
path = 'E:\python\documents'     
def create_bill():
    global y
    refno = str(y)
    pakodi = refno + ".txt"
    global path
    with open(os.path.join(path, pakodi),"w") as file1:
        toFile = output()
        file1.write(toFile)
    qmsg = messagebox.showinfo("Information","Bill Generated") 
def output():
    global y
    refno = str(y)
    list0 = "\t\t\t\t\tReference No. : " + refno
    # list02='\t\t\t\tEmailID :'+emailID.get()+'@gmail.com'
    list1 = "\n\n" + "Item\t\t\tQuantity\t\tCost\n"
    list7 = "____\t\t\t_______\t\t        ____\n\n"
    list2 = "Idly\t\t\t" + idly.get() + "\t\t\t" + str(int(idly.get()) * int(costidly.get())) + "\n"
    list3 = "Biryani\t\t\t" + biryani.get() + "\t\t\t" + str(int(biryani.get()) * int(costbiryani.get())) + "\n"
    list4 = "PaneerButterMasala\t" + paneer_butter_masala.get() + "\t\t\t" + str(
        int(costpaneer_butter_masala.get()) * int(paneer_butter_masala.get())) + "\n"
    list5 = "NimbuPani\t\t" + nimbu_pani.get() + "\t\t\t" + str(
        int(nimbu_pani.get()) * int(costnimbu_pani.get())) + "\n\n"
    list6 = "\t\t\t   " + "total     = Rs " + subTotal.get() + "/-" + "\n"
    list8 = "\t\t\t   " + "Vat       = Rs " + str(int(totalPrice.get()) - int(subTotal.get())) + "/-" + "\n"
    list9 = "\t\t\t   " + "GrandTotal= Rs " + totalPrice.get()[:] + "/-" + "\n"
    String = list0 + list1 + list7 + list2 + list3 + list4 + list5 + list6 + list8 + list9
    return String 

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
# # # ==================================Order Info===========================
lblRef = Label(f1aa, font=('arial', 14), fg="white",bg='black', text="Reference No", bd=2, justify='left')
lblRef.grid(row=0, column=0)
txtRef = Entry(f1aa, font=('arial', 14), textvariable=PaymentRef, bd=2, insertwidth=2, justify='left')
txtRef.grid(row=0, column=1)
txtRef.focus()
# # # --------------
lblCb = Label(f1aa, font=('arial', 14),fg='green',text="Idly", bd=2, justify='left')
lblCb.grid(row=1, column=0)
txtCb = Entry(f1aa, font=('arial', 14), fg="white",bg='black',textvariable=idly, bd=2, insertwidth=2, justify='left')
txtCb.grid(row=1, column=1)
# # --------------
lblBb = Label(f1aa, font=('arial', 14),fg='green',text="Biryani", bd=2, justify='left')
lblBb.grid(row=2, column=0)
txtBb = Entry(f1aa, font=('arial', 14),fg="white",bg='black', textvariable=biryani, bd=2, insertwidth=2, justify='left')
txtBb.grid(row=2, column=1)
# # --------------
lblFf = Label(f1aa, font=('arial', 14), fg='green',text="Paneer butter masala", bd=2, justify='left')
lblFf.grid(row=3, column=0)
txtFf = Entry(f1aa, font=('arial', 14),fg="white",bg='black',textvariable=paneer_butter_masala, bd=2, insertwidth=2, justify='left')
txtFf.grid(row=3, column=1)
# # --------------
lblSd = Label(f1aa, font=('arial', 14),fg='green', text="Nimbu pani", bd=2, justify='left')
lblSd.grid(row=4, column=0)
txtSd = Entry(f1aa, font=('arial', 14), fg="white",bg='black', textvariable=nimbu_pani, bd=2, insertwidth=2, justify='left')
txtSd.grid(row=4, column=1)
# # -------------------
lblAa = Label(f1aa, font=('arial', 14),fg='green', text="Masala Bhindi", bd=2, justify='left')
lblAa.grid(row=5, column=0)
txtAa = Entry(f1aa, font=('arial', 14), fg="white",bg='black', textvariable=masala_bhindi, bd=2, insertwidth=2, justify='left')
txtAa.grid(row=5, column=1)
# # # ===================================Payment Info==========================
lbldate = Label(f1ab, font=('arial', 14),fg='green', text="Date", bd=16, justify='left')
lbldate.grid(row=0, column=0)
txtdate = Entry(f1ab, font=('arial', 14), fg="white",bg='black', textvariable=dateRef, bd=2, insertwidth=2, justify='left')
txtdate.grid(row=0, column=1)
# # --------------
lblCcb = Label(f1ab, font=('arial', 14), fg='green',text="Price of Idly", bd=2, justify='left')
lblCcb.grid(row=1, column=0)
txtCcb = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costidly, bd=2, insertwidth=2, justify='left')
txtCcb.grid(row=1, column=1)
# # --------------
lblCbb = Label(f1ab, font=('arial', 14),fg='green', text="Price of Biryani", bd=2, justify='left')
lblCbb.grid(row=2, column=0)
txtCbb = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costbiryani, bd=2, insertwidth=2, justify='left')
txtCbb.grid(row=2, column=1)
# # --------------
lblCff = Label(f1ab, font=('arial', 14),fg='green', text="Price of Paneer butter masala", bd=2, justify='left')
lblCff.grid(row=3, column=0)
txtCff = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costpaneer_butter_masala, bd=2, insertwidth=2,
               justify='left')
txtCff.grid(row=3, column=1)
# # # --------------
lblCsd = Label(f1ab, font=('arial', 14),fg='green', text="Price of Nimbu pani", bd=2, justify='left')
lblCsd.grid(row=4, column=0)
txtCsd = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costnimbu_pani, bd=2, insertwidth=2, justify='left')
txtCsd.grid(row=4, column=1)
# # # -----------------
lblAaa = Label(f1ab, font=('arial', 14),fg='green', text="Price Of Masala Bhindi", bd=2, justify='left')
lblAaa.grid(row=5, column=0)
txtAaa = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costmasala_bhindi, bd=2, insertwidth=2, justify='left')
txtAaa.grid(row=5, column=1)













# lblAaa = Label(f1ab, font=('arial', 14),fg='green', text="loki", bd=2, justify='left')
# lblAaa.grid(row=6, column=0)
# txtAaa = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costmasala_bhindi, bd=2, insertwidth=2, justify='left')
# txtAaa.grid(row=6, column=1)

# lblAaa = Label(f1ab, font=('arial', 14),fg='green', text="besan", bd=2, justify='left')
# lblAaa.grid(row=7, column=0)
# txtAaa = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costmasala_bhindi, bd=2, insertwidth=2, justify='left')
# txtAaa.grid(row=7, column=1)

# lblAaa = Label(f1ab, font=('arial', 14),fg='green', text="tamatar", bd=2, justify='left')
# lblAaa.grid(row=8, column=0)
# txtAaa = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costmasala_bhindi, bd=2, insertwidth=2, justify='left')
# txtAaa.grid(row=8, column=1)

# lblAaa = Label(f1ab, font=('arial', 14),fg='green', text="Price Of aalo", bd=2, justify='left')
# lblAaa.grid(row=9, column=0)
# txtAaa = Entry(f1ab, font=('arial', 14),  fg="white",bg='black',textvariable=costmasala_bhindi, bd=2, insertwidth=2, justify='left')
# txtAaa.grid(row=9, column=1)




















# ==========================Total Payment Info======
lblPrice = Label(f2aa, font=('arial',16),fg='green',  text="Price", bd=2, justify='left')
lblPrice.grid(row=0, column=0)
txtPrice = Entry(f2aa, font=('arial',16),  fg="white",bg='black',textvariable=subTotal, bd=2, insertwidth=2, justify='left')
txtPrice.grid(row=0, column=1)
# --------------
lblVat = Label(f2aa, font=('arial',16),fg='green',  text="VAT", bd=2, justify='left')
lblVat.grid(row=1, column=0)
txtVat = Entry(f2aa, font=('arial',16),  fg="white",bg='black',textvariable=vat, bd=2, insertwidth=2, justify='left')
txtVat.grid(row=1, column=1)
# --------------
lblTp = Label(f2aa, font=('arial',16), fg='green', text="Total Price", bd=2, justify='left')
lblTp.grid(row=2, column=0)
txtTp = Entry(f2aa, font=('arial',16),  fg="white",bg='black',textvariable=totalPrice, bd=2, insertwidth=2, justify='left')
txtTp.grid(row=2, column=1)
# updatelabel=Label(Bottoms,font=('arial',16,'bold'),text="Total Price")
# updatelabel.pack(fill='both' )
# ==============Buttons==========
btnTotal = Button(f2ab, padx=16, pady=16, bd=2, fg="black", font=('arial', 14), width=15,
                  text="Total Price", command=tPrice).grid(row=0, column=1)
btnRefer = Button(f2ab, padx=16, pady=16, bd=2, fg="black", font=('arial', 14), width=15,
                  text="Sales Reference", command=refNo).grid(row=0, column=0)
btnCrtb = Button(f2ab, padx=16, pady=16, bd=2, fg="black", font=('arial', 14), width=10,
                 text="Generate bill", command=create_bill).grid(row=0, column=2)
btnReset = Button(f2ab, padx=16, pady=16, bd=2, fg="black", font=('arial', 14), width=15,
                  text="Reset", command=reset).grid(row=1, column=0)
btnExit = Button(f2ab, padx=16, pady=16, bd=2, fg="black", font=('arial', 14), width=15,
                 text="Exit", command=iExit).grid(row=1, column=1)
btnSndb = Button(f2ab, padx=16, pady=16, bd=2, fg="black", font=('arial', 14), width=10,
                 text="Other Dishes").grid(row=1, column=2)
root.mainloop()
