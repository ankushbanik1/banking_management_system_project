import pandas as pd
import time
import datetime
import random
import csv
from datetime import date


def account():
    df=pd.read_csv("bankdata.csv")
    global name,pancard,phone_number,acc_num
    name=input("Enter your name.")
    day=date.today()
    pancard=input("Enter your pancard number.")
    phone_number=(input("Enter your phone number."))
    while len(str(phone_number))!=10:
            print("Phone Number should be 10 digits")
            phone_number=int(input("Enter your phone number."))
    
    print("You Have to diposit Minimum 500/- ")
    response=input("Do u want to continue? (y/n)")
    if response=='y':
        debit=(input("enter your Debit card Number:"))
        while len(str(debit))!=16:
            print("Debit card  Number should be 16 digits")
            debit=int(input("enter your Debit card Number:"))
            
    
        cvv=input("enter your CVV Code:")
        while len(str(cvv))!=3 :
            print("CVV Number should be 3 digits")
            cvv=input("enter  your CVV Code:")
            
        (balance)=int(input("enter amount to be added(Minimum 500/-):"))
        while balance< 500:
            print("Minimum Deposit Amount is 500/-")
            balance=input("enter amount to be added:")
        print("Proccesing....Please wait...")
        acc_num="%0.12d" % random.randint(0,9999999999)
        time.sleep(1.5)
        print("Your account Has been created...")
        time.sleep(1.5)
        print("Your Account Number is : {}".format(acc_num))
        print("Account Holder Name is : {}".format(name))
        print("Your Balance is : {}".format(balance))
        b=pd.DataFrame([[acc_num,name,day,pancard,phone_number,balance]])
        b.columns=df.columns
        df=df.append(b)
        df.to_csv("bankdata.csv",index=False)
    # ADDING THE AVAILABLE QUERY IN THE DATA RECORD
    if response!='y':
        
        while True:
            exit()
def withdrwal():
    k=0
    df=pd.read_csv("bankdata.csv")
    print("Please verify Your Account with name and account number")
    name=input("Enter Holder name?")
    acc_num=input("Enter account number name?")
    for i in range(len(df["name"])):
        if int(acc_num)==df["acc_num"][i] and name==df['name'][i]:
            k=1
            day= df["date"][i]
            pan=df['pancard'][i]
            phone=df['phone_number'][i]        

            break
    if(k==1):
        print("hey,Its nice to see you again in our platform..\n Wellcome!!!")
        time.sleep(2)
        print("Your Balance is{} ".format(df['balance'][i]))
        ammount=input("Enter amount for  withdrawl..")
        if str(ammount)>str(df['balance'][i]):
            print("Insufficient Balance to withdraw")
            
        else:
            bal=(int(df['balance'][i])-int(ammount))
            print(bal)
            for i in range(len(df["acc_num"])):
                if int(acc_num)==df["acc_num"][i] and name==df['name'][i]:
                    
                    df= pd.read_csv('bankdata.csv')
                    df.drop(i,inplace=True)
                    df.to_csv('bankdata.csv',index=False)   
                    b=pd.DataFrame([[acc_num,name,day,pan,phone,bal]])
                    b.columns=df.columns
                    df=df.append(b)
                    df.to_csv("bankdata.csv",index=False)
                    print("Thank You see you again!!")
    
    else:
        
        print("your Account Details is not correct please check and try again ")
        
def diposit():
    
    k=0
    df=pd.read_csv("bankdata.csv")
    print("Please verify Your Account with name and account number")
    name=input("Enter Holder name?")
    acc_num=input("Enter account number name?")
    for i in range(len(df["name"])):
        if int(acc_num)==df["acc_num"][i] and name==df['name'][i]:
            day= df["date"][i]
            pan=df['pancard'][i]
            phone=df['phone_number'][i]
            k=1
            break
    if(k==1):
        print("hey,Its nice to see you again in our platform..\n Wellcome!!!")
        time.sleep(2)
        print("Available Balance Balance is{} ".format(df['balance'][i]))
        ammount=input("Enter amount for  diposit.")
        
        bal=(int(df['balance'][i])+int(ammount))
        print('Now Your Available balance is '.format(bal))
        print("Thank You see you again!!")
        for i in range(len(df["acc_num"])):
            
            if int(acc_num)==df["acc_num"][i] and name==df['name'][i]:
                    
                df= pd.read_csv('bankdata.csv')
                df.drop(i,inplace=True)
                df.to_csv('bankdata.csv',index=False)  
                
                b=pd.DataFrame([[acc_num,name,day,pan,phone,bal]])
                b.columns=df.columns
                df=df.append(b)
                df.to_csv("bankdata.csv",index=False)
    
    else:
        print("your Account Details is not correct please check and try again ")     
def view_balance():
    k=0
    df=pd.read_csv("bankdata.csv")
    print("Please verify Your Account with name and account number")
    name=input("Enter Holder name?")
    acc_num=input("Enter account number name?")
    for i in range(len(df["name"])):
        if int(acc_num)==df["acc_num"][i] and name==df['name'][i]:
            
            k=1
            break
    if(k==1):
        print("hey,Its nice to see you again in our platform..\n Wellcome!!!")
        time.sleep(2)
        print("Your Available Balance Balance is{} ".format(df['balance'][i]))
        time.sleep(1)
        print("Thank You see you again!!")
def delete_account():
    k=0
    df=pd.read_csv("bankdata.csv")
    print("Please verify Your Account with name and account number")
    name=input("Enter Holder name?")
    acc_num=input("Enter account number name?")
    for i in range(len(df["name"])):
        if int(acc_num)==df["acc_num"][i] and name==df['name'][i]:
            
            k=1
            break
    if(k==1):
        
        df= pd.read_csv('bankdata.csv')
        df.drop(i,inplace=True)
        df.to_csv('bankdata.csv',index=False)
        print("SuccessFully Closed Your Account")
        
        openn=input("Again Want To Open an Account? (y/n)")
                    
        if openn=='y':
            account()
        else:
            while True:
                print("Thank You see you again!!")
                exit()
                    
        
def main():
    
    print("1. Create Bank Account ")
    print("2. Money withdrawl")
    print("3. diposit Money")
    print("4. View balance ")
    print("5. Delete account")

    slot=input("Enter Your Option.?")

    if slot=="1":
        account()

    elif slot=="2":
        withdrwal()    
    elif slot=="3":
        diposit() 
    elif slot=="4":
        view_balance() 
        
    elif slot=="5":
        delete_account()     

if __name__ == "__main__":
    while True:
        main()
    

      