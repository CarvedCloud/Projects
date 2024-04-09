import csv
import mysql.connector as m
import time
# import matplotlib.pyplot as plt
import random
import streamlit as st

#import SQL_Functions as sf






st.title("Optimization of a Restaurant and Car Park")

st.header("This is the home screen")



    

def reset():
    password = "1234"

    entr_pass = st.text_input("Enter password: ")

    if entr_pass == password :
        st.button("Reset Ingredients Database",key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", 
                disabled=False, use_container_width=False)
        
    
        
        if st.button("Empty Orders Database",key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", 
                disabled=False, use_container_width=False):
            st.session_state['namelist'] = []
            
        
        
    elif entr_pass != password and entr_pass != "":
        st.write("The password entered is incorrect. Please Try again")
    
    else:
        st.write("")

c1,c2,c3,c4,c5,c6 = st.columns(6)

if st.checkbox("Simulation"):
    i1tot=0
    i2tot=0
    i3tot=0
    i4tot=0
    i5tot=0
    i6tot=0
    i7tot=0
    i8tot=0
    i1stock=500
    i2stock=500
    i3stock=500
    i4stock=500
    i5stock=500
    i6stock=500
    i7stock=500
    i8stock=500
    i1rq=1
    i2rq=1
    i3rq=1
    i4rq=1
    i5rq=1
    i6rq=1
    i7rq=1
    i8rq=1
    l=[]
    a=0
    p=0
    pd=0
    ptot=0
    dl=[]
    d1l=[]
    d2l=[]
    d3l=[]
    d4l=[]
    tl=[]
    pmondayl=[]
    pteusdayl=[]
    pwednesdayl=[]
    pthursdayl=[]
    pfridayl=[]
    psaturdayl=[]
    psundayl=[]

    count=random.randint(30,60)
    
    def f1():

        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        
        
        
        
        cur.execute("Create table if not exists Ingredients(Type varchar(10),Dish varchar(20),CostPrice int(4),SellingPrice int(4),Size varchar(5),Dough int(1),Cheese int(1),Sauce int(1),Onion int(1),Tomato int(1),Capsicum int(1),Pepperoni int(1),Pineapple int(1))")
        cur.execute("Insert into Ingredients values('Quantity','PepperoniPizza',NULL,NULL,'Large',3,3,3,0,0,0,5,0)")
        cur.execute("Insert into Ingredients values('Prices','PepperoniPizza',310,399,'Large',36,84,75,0,0,0,65,0)")
        cur.execute("Insert into Ingredients values('Quantity','VegFarmhouse',NULL,NULL,'Large',3,3,3,5,4,4,0,0)")
        cur.execute("Insert into Ingredients values('Prices','VegFarmhouse',276,349,'Large',36,84,75,10,5,16,0,0)")
        cur.execute("Insert into Ingredients values('Quantity','Margherita',NULL,NULL,'Large',3,6,3,0,0,0,0,0)")
        cur.execute("Insert into Ingredients values('Prices','Margherita',329,399,'Large',36,168,75,0,0,0,0,0)")
        cur.execute("Insert into Ingredients values('Quantity','PineapplePizza',NULL,NULL,'Large',3,3,3,3,0,0,0,4)")
        cur.execute("Insert into Ingredients values('Prices','PineapplePizza',351,459,'Large',36,84,75,6,0,0,0,100)")
        cur.execute("Insert into Ingredients values('Quantity','PepperoniPizza',NULL,NULL,'Small',2,2,2,0,0,0,3,0)")
        cur.execute("Insert into Ingredients values('Prices','PepperoniPizza',199,249,'Small',24,56,50,0,0,0,39,0)")
        cur.execute("Insert into Ingredients values('Quantity','VegFarmhouse',NULL,NULL,'Small',2,2,2,3,2,2,0,0)")
        cur.execute("Insert into Ingredients values('Prices','VegFarmhouse',176,229,'Small',24,56,50,6,2,8,0,0)")
        cur.execute("Insert into Ingredients values('Quantity','Margherita',NULL,NULL,'Small',2,4,2,0,0,0,0,0)")
        cur.execute("Insert into Ingredients values('Prices','Margherita',216,249,'Small',24,112,50,0,0,0,0,0)")
        cur.execute("Insert into Ingredients values('Quantity','PineapplePizza',NULL,NULL,'Small',2,2,2,2,0,0,0,2)")
        cur.execute("Insert into Ingredients values('Prices','PineapplePizza',214,259,'Small',24,56,50,4,0,0,0,50)")
        mc.commit()

        cur.execute("Drop table if exists orders")
        cur.execute("Create table if not exists Orders(n int(4),Day varchar(10),CustomerName varchar(30),Dish varchar(20),Price int(3),Dough int(1),Cheese int(1),Sauce int(1),Onion int(1),Tomato int(1),Capsicum int(1),Pepperoni int(1),Pineapple int(1))")

    def f2():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        cur.execute("select Dough from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='PepperoniPizza' and size='Small' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8

    def f3():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='VegFarmhouse' and size='Small' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8
        
    def f4():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='Margherita' and size='Small' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8
            
    def f5():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='PineapplePizza' and size='Small' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8
            
    def f6():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='PepperoniPizza' and size='Large' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8

    def f7():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='VegFarmhouse' and size='Large' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8

    def f8():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='Margherita' and size='Large' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8

    def f9():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,i1,i2,i3,i4,i5,i6,i7,i8
        
        cur.execute("select Dough from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:
            i1=i[0]
            i1tot+=i1
        cur.execute("select Cheese from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:    
            i2=i[0]
            i2tot+=i2
        cur.execute("select Sauce from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:    
            i3=i[0]
            i3tot+=i3
        cur.execute("select Onion from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:    
            i4=i[0]
            i4tot+=i4
        cur.execute("select Tomato from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:
            i5=i[0]
            i5tot+=i5
        cur.execute("select Capsicum from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:
            i6=i[0]
            i6tot+=i6
        cur.execute("select Pepperoni from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:
            i7=i[0]
            i7tot+=i7
        cur.execute("select Pineapple from ingredients where Dish='PineapplePizza' and size='Large' and type='Quantity'")
        for i in cur:
            i8=i[0]
            i8tot+=i8
    
        
    def f11():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,dish,p,pd,ptot
        
        comm="select SellingPrice from ingredients where dish='"+(str(dish[5:]))+"' and Type='Prices' and size='small'"
        cur.execute(comm)
        for i in cur:
            p=i[0]
        pd+=p
        ptot+=p

    def f12():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,p,pd,ptot
        
        comm="select SellingPrice from ingredients where dish='"+(str(dish[5:]))+"' and Type='Prices' and size='large'"
        cur.execute(comm)
        for i in cur:
            p=i[0]
        pd+=p
        ptot+=p
        
    def f13():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1tot,i2tot,i3tot,i4tot,i5tot,i6tot,i7tot,i8tot,ptot

        temp_comm1="insert into Orders values(NULL,NULL,NULL,NULL,'"+(str(ptot))+"','"+(str(i1tot))+"','"+(str(i2tot))+"','"+(str(i3tot))+"','"+(str(i4tot))+"','"+(str(i5tot))+"','"+(str(i6tot))+"','"+(str(i7tot))+"','"+(str(i8tot))+"')"
        cur.execute(temp_comm1)
        mc.commit()    
        
    def f14():
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        global i1rq,i2rq,i3rq,i4rq,i5rq,i6rq,i7rq,i8rq,totcost,ptot
        
        cur.execute("Create table if not exists Restocking(Dough int(10), Cheese int(10), Sauce int(10), Onion int(10), Tomato int(10), Capsicum int(10), Pepperoni int(10), Pineapple int(10), TotalCost int(10), TotalProfit int(10))")
        temp_comm2="insert into Restocking values('"+(str(i1rq*425*12))+"','"+(str(i2rq*425*28))+"','"+(str(i3rq*425*25))+"','"+(str(i4rq*425*2))+"','"+(str(i5rq*425*1.25))+"','"+(str(i6rq*425*4))+"','"+(str(i7rq*425*13))+"','"+(str(i8rq*425*25))+"','"+(str(totcost))+"','"+(str(ptot-totcost))+"')"
        cur.execute(temp_comm2)
        mc.commit()


    f1()    

    f=open('name_list.csv','r',newline='')
    obj=csv.reader(f)

    n = st.number_input("How many days do you want to simulate? ", min_value=7, max_value=None, value="min", step=1, 
                    format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, 
                    disabled=False, label_visibility="visible")
    st.write("The Number of days to be simulated: ",n)
    
    for x in range(0,n):
        
        #print(x)
        current=0
        dn=x%7
        if dn==0:
            day='Monday'
            if pd!=0:
                pmondayl.append(pd)
            count=random.randint(30,60)
        elif dn==1:
            day='Teusday'
            if pd!=0:
                pteusdayl.append(pd)
            count=random.randint(50,80)
        elif dn==2:
            day='Wednesday'
            if pd!=0:
                pwednesdayl.append(pd)
            count=random.randint(10,40)
        elif dn==3:
            day='Thursday'
            if pd!=0:
                pthursdayl.append(pd)
            count=random.randint(60,80)
        elif dn==4:
            day='Friday'
            if pd!=0:
                pfridayl.append(pd)
            count=random.randint(80,110)
        elif dn==5:
            day='Saturday'
            if pd!=0:
                psaturdayl.append(pd)
            count=random.randint(100,130)
        elif dn==6:
            day='Sunday'
            if pd!=0:
                psundayl.append(pd)
            count=random.randint(90,120)
        #print("Count: ",count)
        pd=0
        
        while count>=current:    
            for j in obj:
                l.append(j)
            a=random.randrange(0,10001)
            name=l[a][0]
            
            #print("Name: ",name)
            
            chance=random.randint(1,5)
            if chance>3:
                np=random.randint(6,10)
            elif chance<4:
                np=random.randint(1,5)
            #print("Size of Family: ",np)
            
            current+=np
            #print("Current",current)
            
            for k in range(0,np):
                choice=random.randint(1,8)                          #Dishes 1-4 are small and 5-8 are large (You can later increase the number of dishes, just that first half is for small and the other half for large)
                if choice==1:
                    dish='SmallPepperoniPizza'
                    f2()
                    
                elif choice==2:
                    dish='SmallVegFarmhouse'
                    f3()
                    
                elif choice==3:
                    dish='SmallMargherita'
                    f4()
                    
                elif choice==4:
                    dish='SmallPineapplePizza'
                    f5()
                    
                elif  choice==5:
                    dish='LargePepperoniPizza'
                    f6()
                    
                elif choice==6:
                    dish='LargeVegFarmhouse'
                    f7()
                    
                elif choice==7:
                    dish='LargeMargherita'
                    f8()
                    
                elif choice==8:
                    dish='LargePineapplePizza'
                    f9()
                
                def f10():
                    mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
                    cur=mc.cursor()
                    global x,day,name,dish,p,i1,i2,i3,i4,i5,i6,i7,i8
                    
                    temp_comm="insert into Orders values('"+(str(x))+"','"+(day)+"','"+(name)+"','"+(dish)+"','"+(str(p))+"','"+(str(i1))+"','"+(str(i2))+"','"+(str(i3))+"','"+(str(i4))+"','"+(str(i5))+"','"+(str(i6))+"','"+(str(i7))+"','"+(str(i8))+"')"
                    cur.execute(temp_comm)
                    mc.commit()
                    
                f10()
                
                i1stock-=i1                                   ### Ignore These Warnings ###
                i2stock-=i2
                i3stock-=i3
                i4stock-=i4
                i5stock-=i5
                i6stock-=i6
                i7stock-=i7
                i8stock-=i8
                
                if i1stock<=75:
                    i1stock=500
                    i1rq+=1
                elif i2stock<=75:
                    i2stock=500
                    i2rq+=1
                elif i3stock<=75:
                    i3stock=500
                    i3rq+=1
                elif i4stock<=75:
                    i4stock=500
                    i4rq+=1
                elif i5stock<=75:
                    i5stock=500
                    i5rq+=1
                elif i6stock<=75:
                    i6stock=500
                    i6rq+=1
                elif i7stock<=75:
                    i7stock=500
                    i7rq+=1
                elif i8stock<=75:
                    i8stock=500
                    i8rq+=1
                
                if dish[0:5]=='Small':
                    f11()
                
                elif dish[0:5]=='Large':
                    f12()
                    
                
                                
            #print(day,dish)
            #print(i1,i2,i3)

    #print(i1tot,i2tot,i3tot)
         
    f13()

    totcost=i1rq*425*12+i2rq*425*28+i3rq*425*25+i4rq*425*2+i5rq*425*1.25+i6rq*425*4+i7rq*425*13+i8rq*425*25

    f14()
    
    st.write("Simulation Complete")
    #st.write("Profit: ",ptot-totcost)
    st.image("Dish_Analysis.png")
    st.image("Weekly_Profit.png")
    
    ## Plot graphs here ##
    
if st.checkbox("Manuel"):
    i1stock=50
    i2stock=50
    i3stock=50
    i4stock=50
    i5stock=50
    i6stock=50
    i7stock=50
    i8stock=50
    i1rq=0
    i2rq=0
    i3rq=0
    i4rq=0
    i5rq=0
    i6rq=0
    i7rq=0
    i8rq=0
    l=0
    day=0      #0,7,14....-Sunday
    daystr="Sunday"
    
    
    
    @st.cache(allow_output_mutation=True)
    def persistdata():
        return {}


    st.session_state.nameseatdict = {}

    avgdays={}
    WEEKDAYS=['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
    INGREDIENTS=['DOUGH','CHEESE','SAUCE','ONION','TOMATO','CAPSICUM','PEPPERONI','PINEAPPLE']
    RESTOCK_SUGG_DAYS = 5
    
    def f15():
        global inglist
        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor(buffered=True)
        mc.commit()
        
        ###from MySQL - Get these values on the spot when needed.
        cur.execute("Select * from ingredientsManuel")
        mc.commit()
        inglist=cur.fetchall()
        
    f15()
    



   
    ingnumlist=[]
    for z in inglist:
        ingnumlist.append(list(z))
    dishcost=[]
    dishnamelist=[]
    ingnamelist=["Dough","Cheese","Sauce","Onion","Tomato","Capsicum","Pepperoni","Pineapple"]
    for y in range(0,8):
        dishcost.append(ingnumlist[y][1])
        dishnamelist.append(ingnumlist[y][0])
    totalingnumlist=[]
    for i in range(3,11):
        totalingnumlist.append(ingnumlist[8][i])
    totalingnumlist2=totalingnumlist
    dishchoice=0
    sn2=9      ###18+36+16+10=80 total no of people
    sn4=9
    sn8=2
    sn10=1
    tsn=32

    
    if 'carpark' not in st.session_state:
        st.session_state['carpark'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    if 'entrytimecar' not in st.session_state:
        st.session_state['entrytimecar'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                                                  #Define carpark
    
    if 'exittimecar' not in st.session_state:
        st.session_state['exittimecar'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    totnumcar=20                                                                    
    availcar=20
    
    


    def predi(day):
        
        #avg
            
       

        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
        cur=mc.cursor()
        cur.execute("select * from ordersmanuel")
        mc.commit()
        order=cur.fetchall()
        d={}
        days={}

        for r in order:
            st=str(r[0])+"_"+str(r[1])
            d[st]=[0,0,0,0,0,0,0,0]
            days[st]=st
            
        for r in order:
            st=str(r[0])+"_"+str(r[1])
            
           
            for i in range (0,8):
                
                d[st][i]=d[st][i]+r[i+3]
            
        #print(d)
        numdays={}
        sumdays={}
        

        for t in WEEKDAYS:
            numdays[t]=0
        for t in WEEKDAYS:
            sumdays[t]=[0,0,0,0,0,0,0,0]

        for t in WEEKDAYS:
            avgdays[t]=[0,0,0,0,0,0,0,0]
            
        for n_day in days:
            splitday=n_day.split('_')
            onlyday=splitday[1].upper()
            
            numdays[onlyday]+=1
            
            for i in range (0,8):
                sumdays[onlyday][i]+=d[n_day][i]

        

        for t in WEEKDAYS:
            for i in range (0,8):
                if numdays[t]>0:
                    
                    avgdays[t][i] = sumdays[t][i] / numdays[t]
        
            
            
            
                    
                
        

        #prediction
        prediction={}

        l=totalingnumlist.copy()
        
        i=day%7
        
        iday=WEEKDAYS[i]
        st.write("TODAY IS",iday)
        


        ingno=0
        for k in l:
            
            dayno=0
            while True:
                
                ingre=INGREDIENTS[ingno]
              
                l[ingno]=l[ingno]-avgdays[WEEKDAYS[i]][ingno]
               
                if l[ingno]<10:
                    prediction[ingre]=dayno
                    break
            
                dayno+=1
                if i<6:
                    i+=1
                else:
                    i=0
             
                    
            ingno+=1    
        
        return prediction


    def restocksugg(day):
        predi(day)
        
         
        i=day%7
        
        iday=WEEKDAYS[i]
        
        rsval=[0,0,0,0,0,0,0,0]  
        for r in range(1,RESTOCK_SUGG_DAYS+1): # restocking for Restock_sugg days
            for ingre in range(0,8):
                rsval[ingre]+=avgdays[iday][ingre]

            iday=WEEKDAYS[i+r]
        return rsval





    def round60(n):
        a = (n // 60) * 60                                                                # Smaller multiple   
        b = a + 60                                                                        # Larger multiple     
        return (b if n - a > b - n else a)

    def stockdeduct(itemno):
        for i in range(0,8):
            if totalingnumlist[i]==0:
                st.write("Not sufficient ingredients to cook the dish .")
            else:
                mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
                cur=mc.cursor()
                cur.execute("update ingredientsManuel set Dough="+str(totalingnumlist[0])+" ,Cheese="+str(totalingnumlist[1])+" ,Sauce="+str(totalingnumlist[2])+" ,Onion="+str(totalingnumlist[3])+" ,Tomato="+str(totalingnumlist[4])+" ,Capsicum="+str(totalingnumlist[5])+" ,Pepperoni="+str(totalingnumlist[6])+" ,Pineapple="+str(totalingnumlist[7])+" where Dish= 'NA';")
                mc.commit()
        restockmessage()

        
    def restockmessage():
        cc=0
        for i in range(0,8):
            if totalingnumlist[i]<=10:
                st.write("Stock is below 20 units. Please restock ",ingnamelist[i])
                cc=1
        if cc==1:
            f=predi(day)
            for i in f:
                st.write(i,"will last",f[i],"more days")

    def restock():
        check=9
        sugg_list=restocksugg(day)
        #print(sugg_list)
        n=0
        st.write("Suggested restock values for next",RESTOCK_SUGG_DAYS,"days:")
        for i in sugg_list:
            st.write("\t",INGREDIENTS[n],":\t",i,"units")
            n=n+1
            
        ingr=st.number_input("Enter ingredient to be restocked :")
        qty=st.number_input("Enter units of restocking :")
        for i in range(0,8):
            for j in range(0,8):
                if ingr.upper()==ingnamelist[j].upper():
                    check=j
                    totalingnumlist[j]=qty
                    mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
                    cur=mc.cursor()
                    cur.execute("update ingredientsManuel set "+str(ingr)+" ="+str(qty)+" where Dish='NA';")
                    mc.commit()
        if check==9:
            st.write("There is no such ingredient. Please try again. ")
            restock()
        
        restockmessage() 
    
    if 'namelist' not in st.session_state:
        st.session_state['namelist'] = []

    
        
    
    with st.container():
        namecostdict = persistdata()
    def entry():
        global availcar
        global sn2,sn4,sn8,sn10
        tsn=sn2+sn4+sn8+sn10
        if tsn==0:
            st.write("The restaurent is full. No tables available.")
        elif tsn!=0:
            cname = st.text_input("Enter your Name: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            add_button = st.button("Add", key='add_button')
            
            
            def f16():
                nonlocal cname
                global availcar,i
                global floor
                global namecostdict
                if availcar==0:
                        st.write("No Free Spots Are Available For the Car At The Moment ")
                elif availcar!=0:
                    if cname in st.session_state['carpark']:
                        st.write("Your Car Already Exists in parking lot, Please Try Again!")
                    elif cname not in st.session_state['carpark']:
                        for i in range(0,20):
                            if st.session_state['carpark'][i]==0:
                                if i>=10:
                                    floor=2
                                else:
                                    floor=1
                                st.session_state['carpark'][i]=cname.upper()
                                st.session_state['entrytimecar'][i]=time.time()
                                
                            
                                break
                else:
                    st.write("")
                                
            
            if cname.upper() not in st.session_state['namelist']:
                if add_button:
                    if len(cname) > 0:
                        st.session_state['namelist'] += [cname.upper()]
                        st.write("Customer List: ", st.session_state['namelist'] )
                        namecostdict[cname.upper()]=0
                        f16()
                        if cname not in st.session_state['carpark']:
                            availcar-=1
                            st.write("Your Alloted Parking Spot is:  ",i+1,"\nOn Floor:  ",floor)
                            #st.write("Number Of Available Car Parking Spots :  ",availcar)
                            
                            # dnum=st.number_input("Enter the number of members dining: ",step=1)
                            # if dnum<=2:
                            #     if sn2==0:
                            #         if sn4>=6:
                            #             sn4=sn4-1
                            #             st.session_state.nameseatdict[cname]=4
                            #             st.write("Guide to 4 seater ")
                            #         elif (sn4>=6)==False:
                            #             st.write("Sorry. no seats available ")
                            #         else:
                            #             st.write("")
                            #     elif sn2!=0:
                            #         st.session_state.nameseatdict[cname]=2
                            #         sn2=sn2-1
                            #         st.write("Guide to 2 seater ")
                            #     else:
                            #         st.write("")
                            # elif dnum>2 and dnum<=4:
                            #     if sn4==0:
                            #         if sn2>=2:
                            #             sn2=sn2-2
                            #             st.session_state.nameseatdict[cname]=6                              ####### Unfinished from here ########
                            #             st.write("Join two 2 seaters")
                            #         elif (sn2>=2)==False:
                            #             st.write("Sorry but no seats available ")
                            #         else:
                            #             st.write("")
                            #     elif sn4!=0:
                            #         st.session_state.nameseatdict[cname]=4
                            #         sn4=sn4-1
                            #         st.write("Guide to 4 seater ")
                            #     else:
                            #         st.write("")
                            # elif dnum>4 and dnum<=8:
                            #     if sn8==0:
                            #         if sn4>=2:
                            #             sn4=sn4-2
                            #             st.session_state.nameseatdict[cname]=12
                            #             st.write("Join two four seaters ")
                            #         elif (sn4>=2)==False:
                            #             st.write("Sorry no seats ")
                            #         else:
                            #             st.write("")
                            #     elif sn8!=0:
                            #         st.session_state.nameseatdict[cname]=8
                            #         sn8=sn8-1
                            #         st.write("Guide to 8 seater ")
                            #     else:
                            #         st.write("")
                            # elif dnum>8 and dnum<=10:
                            #     if sn10==0:
                            #         if sn8>0 and sn2>0:
                            #             st.session_state.nameseatdict[cname]=18
                            #             sn8=sn8-1
                            #             sn2=sn2-1
                            #             st.write("Join 8 seater and a two seater ")
                            #         else:
                            #             st.write("")
                            #     elif sn10!=0:
                            #         st.session_state.nameseatdict[cname]=10
                            #         sn10=sn10-1
                            #         st.write("Guide to 10 seater ")
                            #     else:
                            #         st.write("")
                                
                                    
                            # else:
                            #     st.write("Too many people for a table. Split the group into multiple groups. ")    
                    else:
                        st.warning("Enter text")
                        
                    # if st.checkbox("Valet"):
                    #     f16()
                        
                        
                                                                                            # if st.checkbox("Valet"):
                                                                                            #     if availcar==0:
                                                                                            #             st.write("No Free Spots Are Available For the Car At The Moment ")
                                                                                            #     elif availcar!=0:
                                                                                            #         if cname in st.session_state['carpark']:
                                                                                            #             st.write("Car With Entered Registration Number Already Exists, Please Try Again!")
                                                                                            #         elif cname not in st.session_state['carpark']:
                                                                                            #             for i in range(0,20):
                                                                                            #                 if st.session_state['carpark'][i]==0:
                                                                                            #                     if i>=10:
                                                                                            #                         floor=2
                                                                                            #                     else:
                                                                                            #                         floor=1
                                                                                            #                     st.write("Your Alloted Parking Spot is:  ",i+1,"\nOn Floor:  ",floor)
                                                                                            #                     st.session_state['carpark'][i]=cname.upper()
                                                                                            #                     st.session_state['entrytimecar'][i]=time.time()
                                                                                            #                     availcar-=1
                                                                                            #                     st.write("Number Of Available Car Parking Spots :  ",availcar)
                                        
                            
                        
                    # else:
                    #     st.checkbox("Walk-In")
                
                
            elif cname.upper() in st.session_state['namelist']:
                st.write("Person with this is already present inside the restaurent.\nAdd initial or middle name to avoid confusion")
            else:
                st.write("")
                
                
        else:
            st.write("")
        
        
        

    def order():
        global namecostdict,i1stock,i2stock,i3stock,i4stock,i5stock,i6stock,i7stock,i8stock,i1rq,i2rq,i3rq,i4rq,i5rq,i6rq,i7rq,i8rq
        
        oname = st.text_input("Enter your Name: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
                        on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
        oname=oname.upper()
        
        if len(oname)>0:
            if oname in st.session_state['namelist']:
                cost=namecostdict[oname]
                
    
                L_Pepperoni = st.number_input("Large Pepperoni", min_value=0, max_value=None, value="min", step=1, format=None, key=None, help=None,
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            
                L_Veg_Farmhouse = st.number_input("Large Veg Farmhouse", min_value=0, max_value=None, value="min", step=1, format=None, 
                                                key=None, help=None,on_change=None, args=None, kwargs=None, placeholder=None, 
                                                disabled=False, label_visibility="visible")
            
                L_Margherita = st.number_input("Large Margherita", min_value=0, max_value=None, value="min", step=1, format=None, key=None, help=None,
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            
                L_Hawaiian = st.number_input("Large Hawaiian", min_value=0, max_value=None, value="min", step=1, format=None, key=None, help=None,
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            
            
            
            
            
                S_Pepperoni = st.number_input("Small Pepperoni", min_value=0, max_value=None, value="min", step=1, format=None, key=None, help=None,
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            
                S_Veg_Farmhouse = st.number_input("Small Veg Farmhouse", min_value=0, max_value=None, value="min", step=1, format=None, key=None, 
                                                help=None,on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, 
                                                label_visibility="visible")
            
                S_Margherita = st.number_input("Small Margherita", min_value=0, max_value=None, value="min", step=1, format=None, key=None, help=None,
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            
                S_Hawaiian = st.number_input("Small Hawaiian", min_value=0, max_value=None, value="min", step=1, format=None, key=None, help=None,
                            on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
            
            
                l=[L_Pepperoni,S_Pepperoni,L_Veg_Farmhouse,S_Veg_Farmhouse,L_Margherita,S_Margherita,L_Hawaiian,S_Hawaiian]
                price_l=[L_Pepperoni*390,S_Pepperoni*250,L_Veg_Farmhouse*350,S_Veg_Farmhouse*230,L_Margherita*400,S_Margherita*250,L_Hawaiian*459,S_Hawaiian*259]
            
                st.write("YOUR ORDER: ")
                st.write("Large Pepperoni: ",L_Pepperoni)
                st.write("Small Pepperoni: ",S_Pepperoni)
                st.write("Large Veg Farmhouse: ",L_Veg_Farmhouse)
                st.write("Small Veg Farmhouse: ",S_Veg_Farmhouse)
                st.write("Large Margherita: ",L_Margherita)
                st.write("Small Margherita: ",S_Margherita)
                st.write("Large Hawaiian: ",L_Hawaiian)
                st.write("Small Hawaiian: ",S_Hawaiian)
                d1=[3,3,3,0,0,0,5,0]
                d2=[3,3,3,5,4,4,0,0]
                d3=[3,6,3,0,0,0,0,0]
                d4=[3,3,3,3,0,0,0,4]
                d5=[2,2,2,0,0,0,3,0]
                d6=[2,2,2,3,2,2,0,0]
                d7=[2,4,2,0,0,0,0,0]
                d8=[2,2,2,2,0,0,0,2]
                
                dp1=[36,84,75,0,0,0,65,0]
                dp2=[36,84,75,10,5,16,0,0]
                dp3=[36,168,75,0,0,0,0,0]
                dp4=[36,84,75,6,0,0,0,100]
                dp5=[24,56,50,0,0,0,39,0]
                dp6=[24,56,50,6,2,8,0,0]
                dp7=[24,112,50,0,0,0,0,0]
                dp8=[24,56,50,4,0,0,0,50]
                
                
            
            
                if st.button("Place Order",key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", 
                        disabled=False, use_container_width=False):
                    
                    i1stock-=(L_Pepperoni*d1[0]+L_Veg_Farmhouse*d2[0]+L_Margherita*d3[0]+L_Hawaiian*d4[0]+S_Pepperoni*d5[0]+S_Veg_Farmhouse*d6[0]+S_Margherita*d7[0]+S_Hawaiian*d8[0])
                    i2stock-=(L_Pepperoni*d1[1]+L_Veg_Farmhouse*d2[1]+L_Margherita*d3[1]+L_Hawaiian*d4[1]+S_Pepperoni*d5[1]+S_Veg_Farmhouse*d6[1]+S_Margherita*d7[1]+S_Hawaiian*d8[1])
                    i3stock-=(L_Pepperoni*d1[2]+L_Veg_Farmhouse*d2[2]+L_Margherita*d3[2]+L_Hawaiian*d4[2]+S_Pepperoni*d5[2]+S_Veg_Farmhouse*d6[2]+S_Margherita*d7[2]+S_Hawaiian*d8[2])    
                    i4stock-=(L_Pepperoni*d1[3]+L_Veg_Farmhouse*d2[3]+L_Margherita*d3[3]+L_Hawaiian*d4[3]+S_Pepperoni*d5[3]+S_Veg_Farmhouse*d6[3]+S_Margherita*d7[3]+S_Hawaiian*d8[3])
                    i5stock-=(L_Pepperoni*d1[4]+L_Veg_Farmhouse*d2[4]+L_Margherita*d3[4]+L_Hawaiian*d4[4]+S_Pepperoni*d5[4]+S_Veg_Farmhouse*d6[4]+S_Margherita*d7[4]+S_Hawaiian*d8[4])
                    i6stock-=(L_Pepperoni*d1[5]+L_Veg_Farmhouse*d2[5]+L_Margherita*d3[5]+L_Hawaiian*d4[5]+S_Pepperoni*d5[5]+S_Veg_Farmhouse*d6[5]+S_Margherita*d7[5]+S_Hawaiian*d8[5])
                    i7stock-=(L_Pepperoni*d1[6]+L_Veg_Farmhouse*d2[6]+L_Margherita*d3[6]+L_Hawaiian*d4[6]+S_Pepperoni*d5[6]+S_Veg_Farmhouse*d6[6]+S_Margherita*d7[6]+S_Hawaiian*d8[6])
                    i8stock-=(L_Pepperoni*d1[7]+L_Veg_Farmhouse*d2[7]+L_Margherita*d3[7]+L_Hawaiian*d4[7]+S_Pepperoni*d5[7]+S_Veg_Farmhouse*d6[7]+S_Margherita*d7[7]+S_Hawaiian*d8[7])
                
                    if i1stock<10:
                        i1rq+=1
                        i1stock+=40
                        st.write("Dough restocked")
                    if i2stock<10:
                        i2rq+=1
                        i2stock+=40
                        st.write("Cheese restocked")
                    if i3stock<10:
                        i3rq+=1
                        i3stock+=40
                        st.write("Sauce restocked")
                    if i4stock<10:
                        i4rq+=1
                        i4stock+=40
                        st.write("Onion restocked")
                    if i5stock<10:
                        i5rq+=1
                        i5stock+=40
                        st.write("Tomato restocked")
                    if i6stock<10:
                        i6rq+=1
                        i6stock+=40
                        st.write("Capsicum restocked")
                    if i7stock<10:
                        i7rq+=1
                        i7stock+=40
                        st.write("Pepperoni restocked")
                    if i8stock<10:
                        i8rq+=1
                        i8stock+=40
                        st.write("Pineapple restocked")
                    for i in price_l:
                        cost+=i
                        
                        
                        f=open("Records.csv","a")
                        wobj=csv.writer(f)
            
                        wobj.writerow([oname,dishnamelist[dishchoice-1],ingnumlist[dishchoice-1][3],ingnumlist[dishchoice-1][4],ingnumlist[dishchoice-1][5],ingnumlist[dishchoice-1][6],ingnumlist[dishchoice-1][7],ingnumlist[dishchoice-1][8],ingnumlist[dishchoice-1][9],ingnumlist[dishchoice-1][10]])
                        f.close()
                        
                        mc=m.connect(host='127.0.0.1',user='root',password='sudh2chakra',database='complab')
                        cur=mc.cursor()
                        
                        
                        stockdeduct(dishchoice)
            
                    namecostdict[oname]=cost
                    st.write("Total Cost: ",cost)
                    #continue
            else: 
                st.write("No such customer in the restaurant. ")
        elif len(oname)==0:
            st.write("")
                    #continue   
    def exit():
        if st.text_input("Enter Name of Customer"):
        
                                                                                                                                    # global sn2,sn4,sn8,sn10,namecostdict
                                                                                                                                    # if len(st.session_state['namelist'])==0:
                                                                                                                                    #     st.write("Restaurant Is Empty At The Moment, Please Try Again!")
                                                                                                                                    # else:
                                                                                                                                    #     name=st.text_input("Enter customer name ")
                                                                                                                                    #     name=name.upper()
                                                                                                                                    #     if name not in st.session_state['namelist']:
                                                                                                                                    #         st.write("The customer is not in the restaurant ")
                                                                                                                                    #     else:
                                                                                                                                    #         if st.session_state.nameseatdict[name]==2:
                                                                                                                                    #             sn2=sn2+1
                                                                                                                                    #             del st.session_state.nameseatdict[name]
                                                                                                                                    #         elif st.session_state.nameseatdict[name]==4:
                                                                                                                                    #             sn4=sn4+1
                                                                                                                                    #             del st.session_state.nameseatdict[name]
                                                                                                                                    #         elif st.session_state.nameseatdict[name]==6:
                                                                                                                                    #             sn2=sn2+2
                                                                                                                                    #             del st.session_state.nameseatdict[name]
                                                                                                                                    #         elif st.session_state.nameseatdict[name]==8:
                                                                                                                                    #             sn8=sn8+1
                                                                                                                                    #             del st.session_state.nameseatdict[name]
                                                                                                                                    #         elif st.session_state.nameseatdict[name]==10:
                                                                                                                                    #             sn10=sn10+1
                                                                                                                                    #             del st.session_state.nameseatdict[name]
                                                                                                                                    #         elif st.session_state.nameseatdict[name]==12:
                                                                                                                                    #             sn4=sn4+2
                                                                                                                                    #             del st.session_state.nameseatdict[name]
                                                                                                                                    #         elif st.session_state.nameseatdict[name]==18:
                                                                                                                                    #             sn8=sn8+1
                                                                                                                                    #             sn2=sn2+1
                                                                                                                                    #             del st.session_state.nameseatdict[name]
            st.write("Parking fee: 20")
            st.write("The total amount to be paid is : 1819")                                                       #,namecostdict[name])
        #del namecostdict[name]
        #st.session_state['namelist'].remove(name)
        
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")



    if st.checkbox("Entry"):
        entry()
        
    elif st.checkbox("Order"):
        order()
    elif st.checkbox("Exit"):
        exit()
    elif st.checkbox("Reset"):
        reset()
        

    






































# import streamlit as st
# import testing

# # Initialize connection.
# conn = st.connection('mysql', type='sql')

# # Perform query.
# # conn.write("Insert into Ingredients values('Quantity','PepperoniPizza',NULL,NULL,'Large',3,3,3,0,0,0,5,0)")

# # Print results.
# # st.write(df["Dough"].loc[0])

# testing.p1()













