from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import ttk
import tkinter.messagebox
from tkinter.ttk import Combobox
from tkinter.font import Font

root = Tk()
root.title("REAL TIME CURRENCY CONVERTER")
root.geometry("200x200+0+0")


ip1=StringVar(root)
ip2=StringVar(root)
font1=Font(size=24)
ip1.set("select")
ip2.set("select")

CurrencyCode_list=['GBP','HKD','IDR','ILS','DKK','INR','CHF','MXN','CZK','SGD','THB','HRK','EUR','MYR','NOK','CNY','BGN','PHP','PLN','ZAR','CAD','ISK','BRL','RON','NZD','TRY','JPY', 'RUB','KRW', 'USD', 'AUD','HUF','SEK']

currency=Label(root, text="Currency: ",font=font1)
currency.place(x=105,y=100)

FromCurrency_option=Combobox(root,values=CurrencyCode_list,font=font1)
FromCurrency_option.place(x=250,y=100)
FromCurrency_option.set("Select")

# FromCurrency_option=OptionMenu(root,ip1,*CurrencyCode_list)
# FromCurrency_option.place(x=250,y=100)
# label1=Label(root, text="Convert to ",font=font1)
# label1.place(x=680,y=100)



currency1=Label(root, text="Currency: ",font=font1)
currency1.place(x=886,y=100)

ToCurrency_option=Combobox(root,values=CurrencyCode_list,font=font1)
ToCurrency_option.place(x=1030,y=100)
ToCurrency_option.set("Select")
# ToCurrency_option=OptionMenu(root,ip2,*CurrencyCode_list)
# ToCurrency_option.config(height=1,width=10,font=font1)
# ToCurrency_option.place(x=1030,y=100)

amount=Label(root,text="Enter amount: ",font=font1)
amount.place(x=440,y=230)

value=Entry(root,font=font1)
value.place(x=680,y=232)

amount=Label(root,text="Converted Amount: ",font=font1)
amount.place(x=400,y=470)

output=Entry(root,font=font1)
output.place(x=700,y=470)


def RealTimeCurrencyConversion():
    c = CurrencyRates()

    from_currency = FromCurrency_option.get()
    to_currency = ToCurrency_option.get()

    if(value.get()==""):
        tkinter.messagebox.showerror("Error","Amount not entered")

    elif(from_currency=="Select" or to_currency=="Select"):
        tkinter.messagebox.showerror("Error","Currency not selected")

    else:
        new_amt=c.convert(from_currency,to_currency,float(value.get()))
        new_amount=float("{:.4f}".format(new_amt))
        output.insert(0,str(new_amount))








def Reset():
    value.delete(0,END)
    output.delete(0,END)
    FromCurrency_option.set("Select")
    ToCurrency_option.set("Select")



convert=Button(root,font=('arial',15,'bold'),text="Convert",bg="blue",command=RealTimeCurrencyConversion)
convert.place(x=635,y=330)

reset=Button(root,font=('arial',15,'bold'),text="Reset",bg="red",command=Reset)
reset.place(x=640,y=550)


root.resizable(True, True)
root.mainloop()