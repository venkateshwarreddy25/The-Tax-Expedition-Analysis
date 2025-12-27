import pandas as pd
import seaborn as sn
import matplotlib.pyplot as mt

df=pd.read_csv(r'CSV FILES\tax.csv')

print(df.to_string())
print(df.columns)
print(df.info())

label=df[['tip','total','fare','tolls']].sum()
colors=["#075B7A","#26C2677B","#60EE0D","#AC8680"]
mt.figure(figsize=(10, 7))
mt.pie(label,labels=label.index,autopct='%1.1f%%',shadow=False,explode=(.1,.0,.03,.02),colors=colors)
mt.suptitle("Breakdown of Transport Service Charges",fontsize=30)
mt.xlabel('Service Charge',fontsize=20)
mt.show()


mt.figure(figsize=(10, 7))
payment1=df['payment'].head(50)
sn.countplot(x=payment1,data=df.head(50),hue='passengers',palette='gist_rainbow_r')
mt.xlabel('Modes of Payment: Credit Card and Cash',labelpad=-5,size=18,color='green')
mt.ylabel('Total Number Of Persons',labelpad=12,size=15,color='green')
mt.tick_params('both',labelrotation=30,color='blue',size=5)
mt.show()

pick1=df['pickup_zone'].head(9)
sn.countplot(x=pick1,data=df.head(9),hue='payment',palette='Dark2')
mt.tight_layout()
mt.show()

mt.figure(figsize=(15,6))
sn.barplot(x='pickup',y='dropoff',hue='dropoff_zone',palette='gist_rainbow_r',data=df.head(8))
mt.suptitle('Passenger Travel Over Time',size=25,color="#002C29")
mt.xlabel('Coordinating the pickup time and date for the person',size=15,color="#FF5100",labelpad=17)
mt.ylabel('Coordinating the drop-off time and date for the person',size=15,color="#FF0048",labelpad=18)
mt.tick_params(rotation=20,colors="#14003B")
mt.tight_layout()
mt.show()


mt.figure(figsize=(16,7))
sn.barplot(x='distance',y='pickup_zone',hue='dropoff_zone',palette='gist_rainbow',data=df.head(10))
mt.suptitle('Distance measured (km) from origin to destination',color="#080404",size=25)
mt.xlabel('Passenger PickUp',color="#001AFF",size=20,labelpad=25)
mt.ylabel('Passenger Drop-Off',color="#00FF11",size=20)
mt.tick_params(rotation=20,colors="#FF002F")
mt.tight_layout()
mt.show()


sn.histplot(df['passengers'].head(30), kde=True, palette='plasma')
sn.histplot(x='passengers',data=df, kde=True, palette='binary')
mt.suptitle("Passengers prioritize safety by traveling alone")
mt.xlabel('Single passengers travel more frequently than others',color="#00FF26",size=20)
mt.ylabel('Number of passengers traveling',color="#00DDFF",size=20)
mt.show()







