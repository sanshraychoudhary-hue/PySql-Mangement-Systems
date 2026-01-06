import pymysql as m
con=m.connect(host="localhost", user="root", passwd="trigger")
cur=con.cursor()
print("---------------STARTING CANTEEN MANAGEMENT SYSTEM---------------")
import datetime
import time
t=datetime.date.today()
st=datetime.date.isoformat(t)
ts=st[8:10]+st[5:7]+st[2:4]
# i have added price also in bill_master , because change in price of item should not affect the bill records

'''
###############################################################################################################################################################################################
###############################################################################################################################################################################################

'''
def pcms(x):
    
    print('     __                          __________  ______   ______                                                                 ______      ______                ______            __________ ')
    time.sleep(x)
    print('   /           /\      |\     |      |      |        |         |\     |       |\      /|      /\      |\     |      /\      |           |          |\      /| |         |\     |      |     ')
    time.sleep(x)
    print('  /           /  \     | \    |      |      |        |         | \    |       | \    / |     /  \     | \    |     /  \     |           |          | \    / | |         | \    |      |     ')
    time.sleep(x)
    print(' |           /    \    |  \   |      |      |        |         |  \   |       |  \  /  |    /    \    |  \   |    /    \    |           |          |  \  /  | |         |  \   |      |     ')
    time.sleep(x)
    print('  \         /======\   |   \  |      |      |====    |====     |   \  |       |   \/   |   /======\   |   \  |   /======\   |    =====| |====      |   \/   | |====     |   \  |      |     ')
    time.sleep(x)
    print('   \       /        \  |    \ |      |      |        |         |    \ |       |        |  /        \  |    \ |  /        \  |    |    | |          |        | |         |    \ |      |     ')
    time.sleep(x)
    print('     ==== /          \ |     \|      |      |_______ |________ |     \|       |        | /          \ |     \| /          \ |_________| |________  |        | |________ |     \|      |     ')

#########################################################################################################################################

def pmen():
    print("1:  Add Item")
    print("2:  Bill")
    print("3:  Print Bill")
    print("4:  Add Quantity")
    print("5:  Update Quantity")
    print("6:  Update Price")
    print("7:  Trending")
    print("8:  Print ItemName - ItemCode list")
    print("9:  Show Stocks")
    print("10: Exit")

#########################################################################################################################################    
def main_menu():
    pmen()
    try:
        while True :
            a=int(input("Enter Number to Proceed : "))
            if a ==1:
                while True:
                    add()
                    p=input("Press Enter to ADD more items, else type N : ")
                    if p.strip()=='':
                        continue
                    else:
                        pline()
                        pmen()
                        break

            elif a==2:
                q=bill()
                if q[0]==1:
                    pass
                elif q[0]==0:
                    bllid=addbill(q[1])
                    printbill(bllid)
                pline()
                pmen()
                
            elif a==3:
                bllid2=str(input("Enter BillId : "))
                printbill(bllid2)
                pline()
                pmen()
                
            elif a==4:
                while True:
                    addqty()
                    p=input("Press Enter to ADD more item quanities, else type N : ")
                    if p.strip()=='':
                        continue
                    else:
                        pline()
                        pmen()
                        break
            elif a==5:
                while True:
                    updateqty2(0)
                    p=input("Press Enter to UPDATE more items, else type N : ")
                    if p.strip()=='':
                        continue
                    else:
                        pline()
                        pmen()
                        break
            elif a==6:
                while True:
                    updateprice2(0)
                    p=input("Press Enter to UPDATE more item prices, else type N : ")
                    if p.strip()=='':
                        continue
                    else:
                        pline()
                        pmen()
                        break
            elif a==7:
                q=input("Press 1 for viewing today's trending products, else press 2 for viewing trending products of a particular day : ")
                if q == "1":
                    trending2(ts)
                else :
                    ts2=input("Enter timestamp in format - ddmmyy : ")
                    trending2(ts2)
                pline()
                pmen()

            elif a==8:
                printitmcitmn()
                pline()
                pmen()

            elif a==9:
                showstock()
                pline()
                pmen()
        
            elif a==10:
                print("++++++++++++++++++++++ GOOD DAY!! ++++++++++++++++++++++")
                pline()
            
                break
            else :
                print("ENTER CORRECT NUMBER")
    except:
        print("#################### SOME ERROR OCCURED ####################")
        main_menu()
#########################################################################################################################################    
def pline():
    print("-----------------------------------------------------------------------------------")
#########################################################################################################################################    
               
def add():
    additmmstr()
##########################################################################################################################################
def trending2(ts):
    sql1="select s.item_name,sum(qty) from bill_master z, item_master s where (z.billid  like '{}%' and z.itemcode=s.item_code) group by z.itemcode order by z.qty desc".format(ts)
    cur.execute(sql1)
    r=cur.fetchall()
    print("==============================================")
    print("|ItemName\t\t|\tItems Ordered|")
    print("==============================================")
    for i in r :
        if len(i[0])<6:
            print(i[0],"  ",'\t\t\t|',int(i[1]),'\t\t     |',sep='')
        else:    
            print(i[0],"  ",'\t\t|',int(i[1]),'\t\t     |',sep='')
##########################################################################################################################################        
def GetBillNo():
    sql="SELECT billid FROM bill_master where billid like '"+ts+"%' order by srno desc limit 1"
    a=cur.execute(sql)
    if a==0 :
        bno=0
    else:
        r=cur.fetchall()[0][0]
        bno=r[9:]
    return bno
##########################################################################################################################################        
def showstock():
    cur.execute("select im.item_name,idm.price,idm.qty from itemdetail_master idm, item_master im where idm.item_code=im.item_code")
    r=cur.fetchall()
    print("=================================================================================")
    print("Item\t\t\t\t|Price\t\t\t|Qty Available\t\t|")
    print("=================================================================================")
    for i in r:
        if len(i[0])>10:
            print(i[0],'     ','\t\t|',i[1],"\t\t\t|",i[2],"\t\t\t|",sep='')
        else:
            print(i[0],'     ','\t\t\t|',i[1],"\t\t\t|",i[2],"\t\t\t|",sep='')   
        
##########################################################################################################################################
def bill():
    itmcqty={}
    print("---------------Billing Initiated---------------")
    while True:
        ttl=0
        bvl=0
        itmc=input("enter item code : ")
        itmc=itmc.upper()
        cur.execute("select item_code from item_master where item_code='%s'"%(itmc))
        r=cur.fetchall()
        if (itmc,) in r:
            flag=0
            pass
            
        else:
            print("Please enter Valid CODE")
            flag=1
            break
        itmq=int(input("enter qty : "))
        cur.execute("select qty from itemdetail_master where item_code= '%s'"%(itmc))
        r=cur.fetchall()
        qty=int(r[0][0])
        if qty>=itmq:
            if itmc in itmcqty.keys():
                temp=int(itmcqty[itmc])
                itmcqty[itmc]=temp+int(itmq)
            else :
                itmcqty[itmc]=itmq
        else:
            print("Quantity Not available")
            print("avaialble quantity is : ",qty)
            yn=input("do you want to book it (y/n) : ")
            if yn.lower() in ('y','yes'):
                if itmc in itmcqty.keys():
                    temp=int(itmcqty[itmc])
                    itmcqty[itmc]=temp+int(itmq)
                else :
                    itmcqty[itmc]=itmq
        yn=input("Do you want to enter more items(Y/N) : ")
        if yn.lower() in ('y','yes'):
            continue
        else:
            break
    return flag,itmcqty
#############################################################################################################################################        
def printbill(bllid):
    print("Bill id : ",bllid)
    sql2="select im.item_name,bm.qty,bm.price,bm.total from bill_master bm , item_master im where bm.billid='%s' and bm.itemcode = im.item_code"%(bllid)
    cur.execute(sql2)    
    rec=cur.fetchall()
    ttlbll=0
    print("=========================================================================================================")
    print("|ItemName\t\t\t|  Qty\t\t\t| Price\t\t\t|  Total                |")
    print("=========================================================================================================")
    for i in rec:
        ttlbll=ttlbll+int(i[3])
        for j in i:
            if str(type(j))[8:11] == "str":
                if len(j.strip())>10 :
                    print(j.strip(),'  ',end='\t\t')
                    print('|',end='')
                else:    
                    print(j.strip(),'  ',end='\t\t\t')
                    print('|',end='')
            else :
                print(j,end='\t\t\t')
                print('|',end='')
        print()
	
    print('\t\t\t',"TOTAL BILL VALUE : ",ttlbll)
##############################################################################################################################################  
def addbill1(itmc,itmq,bno):
    ttl=0
    cur.execute("select price from itemdetail_master where item_code= '%s'"%(itmc))
    r=cur.fetchall()
    pr=int(r[0][0])
    bllid=ts+"bno"+str(bno)
    ttl=int(itmq)*int(pr)
    sql5="insert into bill_master (billid,itemcode,qty,price,total) values ('%s','%s',%d,%d,%d)"%(bllid,itmc,itmq,pr,ttl)
    cur.execute(sql5)
    con.commit()
    cur.execute("update itemdetail_master set qty=qty-%d where item_code='%s' and timestamp='%s'"%(itmq,itmc,ts))
    con.commit()
    return bllid

    
def addbill(itmcqty):
    bno=GetBillNo()
    bno=int(bno)+1
    bno=str(bno)
    for i in itmcqty:
        itmc=i
        itmq=itmcqty[i]
        bll=addbill1(itmc,itmq,bno)
    return bll        
###################################################################################################################################################################    
def addqty():
    print("---------------Add Quantity Initiated---------------")
    itmc=input("enter item code : ")
    itmc=itmc.upper()
    cur.execute("select item_code from itemdetail_master")
    rec=cur.fetchall()
    if (itmc,) in rec:
        cur.execute("select qty from itemdetail_master where item_code='%s'"%(itmc))
        rec=cur.fetchall()
        print("Current quantity is : ",rec[0][0])
        t=rec[0][0]
        qty=int(input("enter quantity to add : "))
        qtyn=qty+t
        cur.execute("update itemdetail_master set qty = %d where item_code='%s'"%(qtyn,itmc))
        con.commit()
        print("Added")
    else:
        print("enter valid name and try again")
        addqty()
###################################################################################################################################################################
def updateprice2(itmc):
    print("---------------Price Update Initiated---------------")
    if itmc==0:
        itmc=input("enter item code : ")
        itmc=itmc.upper()
    else:
        itmc=itmc.upper()
    cur.execute("select item_code from itemdetail_master")
    rec=cur.fetchall()
    if (itmc,) in rec:
        cur.execute("select price from itemdetail_master where item_code = '%s'"%(itmc))
        rec=cur.fetchall()
        print("Current Price is : ",rec[0][0])
        pr=int(input("enter new price : "))
        cur.execute("update itemdetail_master set price = %d where item_code='%s'"%(pr,itmc))
        con.commit()
        print("UPDATE SUCCESSFUL")
    else:
        print("enter valid name and try again")
###################################################################################################################################################################
def updateqty2(itmc):
    print("---------------Update Quantity Initiated---------------")
    if itmc==0:
        itmc=input("enter item code : ")
        itmc=itmc.upper()
    else:
        itmc=itmc.upper()
    cur.execute("select item_code from itemdetail_master")
    rec=cur.fetchall()
    if (itmc,) in rec:
        cur.execute("select qty from itemdetail_master where item_code = '%s'"%(itmc))
        rec=cur.fetchall()
        print("Current Quantity is : ",rec[0][0])
        qty=int(input("enter new quantity : "))
        cur.execute("update itemdetail_master set qty = %d where item_code='%s'"%(qty,itmc))
        con.commit()
        print("UPDATE SUCCESSFUL")
    else:
        print("enter valid name and try again")
###################################################################################################################################################################
def additmmstr():
    print("---------------Add Item Initiated---------------")
    print("--------------------------------preffered format for item code Burger 30rs > BG30")
    itmc=input("Enter item code : ")
    itmc=itmc.upper()
    cur.execute("select item_code from item_master")
    rec=cur.fetchall()
    if (itmc,) in rec:
        print("Item Code Already present, please re-enter data")
        f=input("do you want to update instead(Y/N) : ")
        if f.lower() in ("y",'yes'):
            p=int(input("For UPDATING price enter - 1 , For UPDATING quantity enter - 2 , For UPDATING both enter 3  : "))
            if p == 1 :
                updateprice2(itmc)
            elif p == 2 :
                updateqty2(itmc)
            elif p == 3:
                updateprice2(itmc)
                updateqty2(itmc)
    else:
        itmn=input("Enter item name : ")
        itmp=itmc
        cur.execute("insert into item_master (item_name,item_code) values ('%s','%s')"%(itmn,itmc))
        con.commit()
        additmdtls(itmp)
##################################################################################################################################################################    
def additmdtls(itmc):
    print("---------------Add Item Details Initiated---------------")
    itmc=itmc.upper()
    cur.execute("select item_code from itemdetail_master")
    rec=cur.fetchall()
    if (itmc,) in rec:
        print("Item Code Already present , please re-enter data")
        f=input("do you want to update instead(Y/N) : ")
        if f.lower() in ("y",'yes'):
            p=int(input("For UPDATING price enter - 1 , For UPDATING quantity enter - 2 , For UPDATING both enter 3  : "))
            if p == 1 :
                updateprice2(itmc)
            elif p == 2 :
                updateqty2(itmc)
            elif p == 3:
                updateprice2(itmc)
                updateqty2(itmc)
        else:
            pass
        pass
    else:
        itmp=int(input("enter item price : "))
        qty=int(input("enter available quantity : "))
        cur.execute("insert into itemdetail_master (timestamp,item_code,price,qty) values ('%s','%s',%d,%d)"%(ts,itmc,itmp,qty))
        con.commit()
###################################################################################################################################################################   
def createdb():
    print("---------------Creation Initiated---------------")
    cur.execute("CREATE DATABASE canteen")
    cur.execute("USE canteen")
    cur.execute("create table item_master (srno INTEGER AUTO_INCREMENT UNIQUE , \
                item_name varchar(45) NOT NULL, \
                item_code varchar(10) primary key)")
    
    cur.execute("create table bill_master (srno INTEGER AUTO_INCREMENT UNIQUE, \
                billid varchar(30), \
                itemcode varchar(10), \
                qty INTEGER, \
                price Integer,\
                total INTEGER)")

    cur.execute("create table itemdetail_master (srno INTEGER AUTO_INCREMENT UNIQUE ,\
                timestamp varchar(7), \
                item_code varchar(10) Primary Key, \
                price integer, \
                qty integer) ")


    print("ALL DATABASE,TABLES CREATED SUCCESFULLY")
    conn()              
#####################################################################################################################################################################
def printitmcitmn():
    print("==========================================================")
    print("Item Code\t\t   |\t   Item Name             |")
    print("==========================================================")
    cur.execute("select item_code,item_name from item_master")
    r=cur.fetchall()
    for i in range(len(r)):
        print(r[i][0]," ","\t\t\t   |\t  ",end='')
        if len(r[i][1].strip())> 10:
            print(r[i][1],'\t |')
        else:
            print(r[i][1],'\t\t |')
#####################################################################################################################################################################   
def conn():
    try:
        cur.execute("use canteen")
    except:
        createdb()
#####################################################################################################################################################################
conn()
pcms(0.2)
main_menu()
