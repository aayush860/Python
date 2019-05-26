import Tkinter
from selenium.webdriver import Chrome
import shutil
import win32com.client
import os
from tkinter import filedialog
from tkinter import StringVar
from tkinter.ttk import *

top = Tkinter.Tk()
s=Style()
top.title("BD_internationals Product")

def helloCallBack():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    global ff
#    ff=filename+'/rr1.xlsx'
#    shutil.copy('vv8.xlsx',ff)


def create_window():
    import json
    import requests

    from num2words import num2words
    import shutil
    import win32com.client
    import os


    filee="C:/Users/new/Desktop/New folder/xxx.xlsx"
    fileee="C:/Users/new/Desktop/New folder/xxxraj.xlsx"
    
    response = requests.get("https://njncjknc.000webhostapp.com/nljksncls.php")				#edited
    json_data = json.loads(response.text)
    i=0
    ii=0

    for d in json_data:
        i=i+1
        print d['place']
        print d['ID']
        if d['place']=="Gujrat":
            ff=filename+'/'+str(d['ID'])+'.xlsx'
            shutil.copy((os.path.join(os.getcwd(),'gujrat.xlsx')),ff)
            x1 = win32com.client.Dispatch("Excel.Application")
            x1.Visible = True
            tt=x1.Workbooks.Open(ff)
            ws=tt.ActiveSheet
            ws.Range("C14").Value=d['client_name']
            ws.Range("O12").Value=d['date']
            ws.Range("D60").Value=d['date']
            ws.Range("O13").Value=d['time']
            ws.Range("D61").Value=d['timeofremoval']
            ws.Range("C15").Value=d['A1']
            ws.Range("C16").Value=d['A2']
            ws.Range("C17").Value=d['A3']
            ws.Range("L20").Value=d['A3']        
            ws.Range("C18").Value=d['A4']
            ws.Range("C20").Value=d['GSTIN']
            ws.Range("P55").Value=str(0)
            ws.Range("M16").Value=d['Name_of_Transporter']
            pname=d['product_name'].split("/")
            ii=0
            y=25
            for pnme in pname:
                if pnme!="":
                    bb="B"+str(y)
                    ws.Range(bb).Value=pnme
                    ii=ii+1
                    aa="A"+str(y)
                    jj="J"+str(y)
                    ws.Range(jj).Value=str(0)
                    ws.Range("J48").Value=str(0)
                    ws.Range(aa).Value=str(ii)
                    y=int(y)+1

            y=25        
            hsncode=d['HSN_code'].split("/")
            for hsn in hsncode:
                if hsn!="":
                    dd="D"+str(y)
                    ws.Range(dd).Value=hsn
                    y=y+1
     
            y=25        
            quantt=d['quan_per_prod'].split("/")
            quantity=list()
            pack=d['pack_per_prod'].split("/")
            packging=list()
            for quan in quantt:
                if quan!="":
                    quantity.append(quan)
            for pck in pack:
                if pck!="":
                    packging.append(pck)

            y=25
            fff=0
            fiqu=list()
            for r in range(0,len(quantity)):
                fiqu.append(int(quantity[r])*int(packging[r]))
                aa="F"+str(y)
                ws.Range(aa).Value=fiqu[r]
                fff=fff+int(fiqu[r])
                ee="E"+str(y)
                ws.Range(ee).Value=str(quantity[r])+"X"+str(packging[r])+" KG"
                y=int(y)+1

            ws.Range("F48").Value=str(fff)

            y=25
            priperpro=d['price_per_prod'].split("/")
            for priper in priperpro:
                if priper!="":
                    dd="G"+str(y)
                    ws.Range(dd).Value=priper
                    y=y+1
            
            y=25
            fiamt=0
            amtperpro=d['total_price_per_prod'].split("/")
            for amtper in amtperpro:
                if amtper!="":
                    dd="H"+str(y)
                    ws.Range(dd).Value=amtper
                    y=y+1
                    fiamt=fiamt+int(amtper)
            
            ws.Range("H48").Value=str(fiamt)


            y=25
            fidis=0
            disperpro=d['disc_val_per_prod'].split("/")
            for disper in disperpro:
                if disper!="":
                    dd="I"+str(y)
                    ws.Range(dd).Value=disper
                    y=y+1
                    fidis=fidis+int(disper)
            
            ws.Range("I48").Value=str(fidis)

            y=25
            fitax=0
            igst=0
            cgst=0
            sgst=0
            taxperpro=d['taxableamount_per_prod'].split("/")
            for taxper in taxperpro:
                if taxper!="":
                    dd="K"+str(y)
                    ws.Range(dd).Value=taxper
                    fitax=fitax+int(taxper)
                    pp="P"+str(y)
                    nn="N"+str(y)
                    ll="L"+str(y)
                    oo="O"+str(y)
                    qq="Q"+str(y)
                    mm="M"+str(y)
                    
                    if d['A3'].find(d['place'].upper())>(-1):
                        ws.Range(pp).Value=str(9)
                        ws.Range(nn).Value=str(9)
                        ws.Range(ll).Value=str(0)
                        fillqqs=((int(taxper)*9)/100)
                        filloos=((int(taxper)*9)/100)
                        ws.Range(oo).Value=fillqqs
                        ws.Range(qq).Value=filloos
                        ws.Range(mm).Value=str(0)
                        igst=0
                        cgst=cgst+fillqqs
                        sgst=sgst+fillqqs
                        ws.Range("O48").Value=sgst
                        ws.Range("Q48").Value=cgst
                        ws.Range("M48").Value=igst
                        
                        
                    elif d['A4'].find(d['place'].upper())>(-1):
                        ws.Range(pp).Value=str(9)
                        ws.Range(nn).Value=str(9)
                        ws.Range(ll).Value=str(0)
                        fillqqs=((int(taxper)*9)/100)
                        filloos=((int(taxper)*9)/100)
                        ws.Range(oo).Value=fillqqs
                        ws.Range(qq).Value=filloos
                        ws.Range(mm).Value=str(0)
                        igst=0
                        cgst=cgst+fillqqs
                        sgst=sgst+fillqqs
                        ws.Range("O48").Value=sgst
                        ws.Range("Q48").Value=cgst
                        ws.Range("M48").Value=igst

                        
                    else:
                        ws.Range(ll).Value=str(18)
                        ws.Range(pp).Value=str(0)
                        ws.Range(nn).Value=str(0)
                        fillmms=((int(taxper)*18)/100)
                        ws.Range(mm).Value=fillmms
                        ws.Range(oo).Value=str(0)
                        ws.Range(qq).Value=str(0)
                        igst=igst+fillmms
                        cgst=0
                        sgst=0
                        ws.Range("O48").Value=sgst
                        ws.Range("Q48").Value=cgst
                        ws.Range("M48").Value=igst
                        

                        
                        
                    y=y+1

            
            ws.Range("K48").Value=str(fitax)
            ws.Range("P50").Value=str(fitax)
            ws.Range("P51").Value=str(cgst)
            ws.Range("P52").Value=str(sgst)
            ws.Range("P53").Value=str(igst)
            ws.Range("P54").Value=str(fitax+igst+sgst+cgst)
            ws.Range("P56").Value=str(fitax+igst+sgst+cgst)
            ws.Range("D57").Value=num2words((fitax+igst+sgst+cgst),lang='en_IN')





                

            tt.Save()
            x1.Application.Quit()


        elif d['place']=='Rajasthan':
            ff=filename+'/'+str(d['ID'])+'.xlsx'
            shutil.copy((os.path.join(os.getcwd(),'raj.xlsx')),ff)
            x1 = win32com.client.Dispatch("Excel.Application")
            x1.Visible = True
            tt=x1.Workbooks.Open(ff)
            ws=tt.ActiveSheet
            ws.Range("C13").Value=d['client_name']
            ws.Range("K11").Value=d['date']
            ws.Range("K17").Value=d['date']
            ws.Range("C56").Value=d['date']
            ws.Range("K12").Value=d['time']
            ws.Range("C57").Value=d['timeofremoval']
            ws.Range("C14").Value=d['A1']
            ws.Range("C15").Value=d['A2']
            ws.Range("C16").Value=d['A3']
            ws.Range("K18").Value=d['A3']        
            ws.Range("C17").Value=d['A4']
            ws.Range("C18").Value=d['GSTIN']
            ws.Range("K50").Value=str(0)
            ws.Range("K44").Value=str(0)
            ws.Range("K45").Value=str(0)
            ws.Range("H15").Value=d['Name_of_Transporter']

            pname=d['product_name'].split("/")
            ii=0
            y=25
            for pnme in pname:
                if pnme!="":
                    bb="B"+str(y)
                    ws.Range(bb).Value=pnme
                    ii=ii+1
                    aa="A"+str(y)
                    ws.Range(aa).Value=str(ii)
                    y=int(y)+1

            y=25        
            hsncode=d['HSN_code'].split("/")
            for hsn in hsncode:
                if hsn!="":
                    dd="E"+str(y)
                    ws.Range(dd).Value=hsn
                    y=y+1
     
            y=25        
            quantt=d['quan_per_prod'].split("/")
            quantity=list()
            pack=d['pack_per_prod'].split("/")
            packging=list()
            for quan in quantt:
                if quan!="":
                    quantity.append(quan)
                    

            y=25
            for pck in pack:
                if pck!="":
                    packging.append(pck)
                    

            y=25
            fff=0
            fiqu=list()
            for r in range(0,len(quantity)):
                fiqu.append(int(quantity[r])*int(packging[r]))
                aa="H"+str(y)
                ws.Range(aa).Value=fiqu[r]
                fff=fff+int(fiqu[r])
                aa="G"+str(y)
                ws.Range(aa).Value=quantity[r]
                aa="F"+str(y)
                ws.Range(aa).Value=packging[r]
                y=int(y)+1

    #        ws.Range("F48").Value=str(fff)

            y=25
            priperpro=d['price_per_prod'].split("/")
            for priper in priperpro:
                if priper!="":
                    dd="I"+str(y)
                    ws.Range(dd).Value=priper
                    y=int(y)+1
            
            y=25
            fiamt=0
            amtperpro=d['total_price_per_prod'].split("/")
            for amtper in amtperpro:
                if amtper!="":
                    dd="K"+str(y)
                    ws.Range(dd).Value=amtper
                    y=y+1
                    fiamt=fiamt+int(amtper)
            ws.Range("K41").Value=str(fiamt)

            others=d['Others']        
            ws.Range("K45").Value=str(others)

            y=25
            fidis=0
            disss=list()
            disperpro=d['disc_percentage_per_prod'].split("/")
            for disper in disperpro:
                if disper!="":
                    fidis=fidis+int(disper)
                    disss.append(disper)
            fidis=(fidis/(len(disss)))
            ws.Range("J42").Value=str(fidis)+"%"
            ws.Range("K42").Value=str(fidis)+"%"
            ws.Range("J43").Value=str(fidis)+"%"


            r=((fiamt*fidis)/100)
            ws.Range("K43").Value=str(r)
            ws.Range("K46").Value=str(fiamt+int(others)-int(r))        
            y=25
            fitax=fiamt+int(others)-int(r)
            igst=0
            cgst=0
            sgst=0
            taxperpro=d['taxableamount_per_prod'].split("/")
            for taxper in taxperpro:
                if taxper!="":
                    print("n")
                    #fitax=fitax+(fiamt-int(r)+int(others))
     #               ws.Range("K46").Value=str(fitax)
                    
                    if d['A3'].find(d['place'].upper())>(-1):
                        ws.Range("J47").Value=str(9)+"%"
                        ws.Range("J48").Value=str(9)+"%"
                        ws.Range("J49").Value=str(0)+"%"
                        fillqqs=((int(fitax)*9)/100)
                        filloos=((int(fitax)*9)/100)
                        igst=0
                        cgst=fillqqs
                        sgst=fillqqs
                        ws.Range("K47").Value=sgst
                        ws.Range("K48").Value=cgst
                        ws.Range("K49").Value=igst

                        
                        
                    elif d['A4'].find(d['place'].upper())>(-1):
                        ws.Range("J47").Value=str(9)+"%"
                        ws.Range("J48").Value=str(9)+"%"
                        ws.Range("J49").Value=str(0)+"%"
                        fillqqs=((int(fitax)*9)/100)
                        filloos=((int(fitax)*9)/100)
                        igst=0
                        cgst=fillqqs
                        sgst=fillqqs
                        ws.Range("K47").Value=sgst
                        ws.Range("K48").Value=cgst
                        ws.Range("K49").Value=igst

                        
                    else:
                        ws.Range("J47").Value=str(0)+"%"
                        ws.Range("J48").Value=str(0)+"%"
                        ws.Range("J49").Value=str(18)+"%"
                        fillig=((int(fitax)*18)/100)
                        igst=fillig
                        cgst=0
                        sgst=0
                        ws.Range("K47").Value=sgst
                        ws.Range("K48").Value=cgst
                        ws.Range("K49").Value=igst
                        

                        
                        
                    y=y+1

            
            ws.Range("K51").Value=str(fitax+igst+sgst+cgst)
            ws.Range("D50").Value=num2words((fitax+igst+sgst+cgst),lang='en_IN')





                

            tt.Save()
            x1.Application.Quit()
            
    



    



def filll():
    x1 = win32com.client.Dispatch("Excel.Application")
    x1.Visible = True
    tt=x1.Workbooks.Open(ff)
    ws=tt.ActiveSheet
    ws.Range("A2").Value="hgvhjuk"
    tt.Save()
    x1.Application.Quit()
    


folder_path = StringVar()
lbl1 = Label(master=top,textvariable=folder_path)
#lbl1.grid(row=0, column=1)
b = Tkinter.Button(top, text="START GENERATING BILL", command=create_window)

#BB= Tkinter.Button(top, text ="filler", command = filll)
top.configure(background='Black')
top.geometry("300x100")
B = Tkinter.Button(top, text ="SPECIFY DIRECTORY TO STORE BILL", command = helloCallBack)
F = Tkinter.Frame(top,bg="Red").pack()
B.pack()

#BB.pack()
b.pack()
#F.pack()
top.mainloop()
