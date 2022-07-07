import streamlit as st
import pandas as pd 
from PIL import Image
import numpy_financial as npf


image = Image.open('new_logo.png')
st.image(image)

st.write("""
# Cassava Flour investment project feasibility
This tool uses predetermined information based on averages of business plans of multiple cassava flour processors from D.R. Congo, Nigeria and Colombia. This study was conducted during the development of the **Scaling Readiness Flash Dryer project** during 2019 and 2020. Although the information used could be significantly different with respect to other countries, this exercise could be used as a rough estimate to a pre-feasibility study of investment in cassava flour processing using flash drying technology. However, it is recommended that before making an investment, a complete study and business plan with updated data in your specific locality should be carried out. For inquiries and further information please contact us at latabordaa@unal.edu.co
""")

sel_col, disp_col = st.columns(2)
User_country = sel_col.selectbox('Please select your location (more approximate)', options=['DR. Congo (intermediate investment cost)','Nigeria (low investment cost)','Colombia (high investment cost)'], index=0)


Flour_demand = sel_col.slider('If you have conducted a previous market survey, do you know what is the demand (estimated or projected) for cassava flour in your target market? (in Ton/week)', min_value=5, max_value=35, value=15, step=5)

disp_col.write('Considering that the dryer will be operating for 6 days/week and 8 hours/day, the required capacity of the flash dryer (in Kg/hr) is:')


Capacity1 = 100 
Capacity2 = 200 
Capacity3 = 300 
Capacity4 = 400 
Capacity5 = 500 
Capacity6 = 600 
Capacity7 = 700 


if Flour_demand == 5:
	CY=100
	disp_col.subheader(Capacity1)
elif Flour_demand == 10:
	CY=200
	disp_col.subheader(Capacity2)
elif Flour_demand == 15:
	CY=300
	disp_col.subheader(Capacity3)
elif Flour_demand == 20:
	CY=400
	disp_col.subheader(Capacity4)
elif Flour_demand == 25:
	CY=500
	disp_col.subheader(Capacity5)
elif Flour_demand == 30:
	CY=600
	disp_col.subheader(Capacity6)
elif Flour_demand == 35:
	CY=700
	disp_col.subheader(Capacity7)	

disp_col.write('The price *(in US Dollars)* of the Flash Dryer that you need is:')

def load_data():
	df=pd.DataFrame(datos)
	df_reset=df.set_index('Flash Dryer Price')
	return df_reset

datos = {'F_demand':[5,10,15,20,25,30,35],
	'NIG_Price':[9497,14728,19040,22431,24903,26454,27085],
	'NIG_complementary':[4070,6312,8160,9613,10673,11337,11608],
	'Roots_demand':[16.3,32.6,48.9,65.2,81.5,97.8,114.1],
	'DRC_complementary':[6026,10702,14878,18554,21729,24403,26577],
	'DRC_Price':[14060,24972,34716,43292,50700,56940,62012],
	'Colombia_complementary':[12406,17058,21428,25516,29322,32847,36089],
	'Colombia_Price':[28947,39802,49999,59538,68419,76642,84207],
	'Flash Dryer Price':['US$','US$','US$','US$','US$','US$','US$']}

datos = load_data()


Price_1 = datos[datos['F_demand']==Flour_demand]['Colombia_Price']
Price_2 = datos[datos['F_demand']==Flour_demand]['DRC_Price']
Price_3 = datos[datos['F_demand']==Flour_demand]['NIG_Price']


if User_country == 'Colombia (high investment cost)':
	disp_col.subheader(Price_1)

elif User_country == 'Nigeria (low investment cost)':
	disp_col.subheader(Price_3)

elif User_country == 'DR. Congo (intermediate investment cost)':
	disp_col.subheader(Price_2)


Cassava_demand = sel_col.slider('Approximately how many tons of cassava roots would be available weekly for processing at your location', min_value=16.3, max_value=114.1, value=48.9, step=16.3)
R= Cassava_demand
def load_data():
	df=pd.DataFrame(datos1)
	df_reset=df.set_index('Cassava roots required (Ton/week)')
	return df_reset

datos1 = {'F_demand':[5,10,15,20,25,30,35],
	'Roots_demand':[16.3,32.6,48.9,65.2,81.5,97.8,114.1],
	'Cassava roots required (Ton/week)':['Ton','Ton','Ton','Ton','Ton','Ton','Ton']}

datos1 = load_data()

Roots_Requitment = datos1[datos1['F_demand']==Flour_demand]['Roots_demand']
C= Roots_Requitment

disp_col.subheader(Roots_Requitment)

if int(R)<int(C):
	sel_col.write('The quantity of roots available in your locality **is not enough** to process the quantity of flour demanded')
elif int(R) >= int(C):
	sel_col.write('The quantity of roots available in your locality **is enough** to process the quantity of flour demanded')

#complementary technology
Complementary_tech = sel_col.selectbox('Will you also invest in complementary technology for cassava flour processing? (Press, Granulator, Gas burner (or Diesel heatexchanger), PID control system,… Note:The costs of the complementary technology may vary from country to country, however, the information collected indicates that of the total investment costs, the flash dryer corresponds on average to 70%. For practical purposes of the analysis, we will use this approximate value to estimate the total investment costs)', options=['yes','not'], index=0)

def load_data():
	df=pd.DataFrame(datos2)
	df_reset=df.set_index('Complementary technology Price')
	return df_reset

datos2 = {'F_demand':[5,10,15,20,25,30,35],
	'NIG_complementary':[4070,6312,8160,9613,10673,11337,11608],
	'DRC_complementary':[6026,10702,14878,18554,21729,24403,26577],
	'Colombia_complementary':[12406,17058,21428,25516,29322,32847,36089],
	'Complementary technology Price':['US$','US$','US$','US$','US$','US$','US$']}

datos2 = load_data()


C_Price_1 = datos2[datos2['F_demand']==Flour_demand]['Colombia_complementary']
C_Price_2 = datos2[datos2['F_demand']==Flour_demand]['DRC_complementary']
C_Price_3 = datos2[datos2['F_demand']==Flour_demand]['NIG_complementary']


if User_country == 'Colombia (high investment cost)' and Complementary_tech == 'yes':
	disp_col.subheader(C_Price_1)

elif User_country == 'Nigeria (low investment cost)'and Complementary_tech == 'yes':
	disp_col.subheader(C_Price_3)

elif User_country == 'DR. Congo (intermediate investment cost)'and Complementary_tech == 'yes':
	disp_col.subheader(C_Price_2)


# Toal investment (Flas dryer + Complementary technology)TI)

Inv_col = C_Price_1+Price_1
Inv_DRC = C_Price_2+Price_2
Inv_NIG = C_Price_3+Price_3

disp_col.subheader('The total investment (in USD) is:')

if User_country == 'Colombia (high investment cost)' and Complementary_tech == 'yes':
	TI=Inv_col
	disp_col.write(Inv_col)

elif User_country == 'Nigeria (low investment cost)'and Complementary_tech == 'yes':
	TI=Inv_NIG
	disp_col.write(Inv_NIG)

elif User_country == 'DR. Congo (intermediate investment cost)'and Complementary_tech == 'yes':
	TI=Inv_DRC
	disp_col.write(Inv_DRC)

if User_country == 'Colombia (high investment cost)' and Complementary_tech == 'not':
	TI=Price_1
	disp_col.write(Price_1)

elif User_country == 'Nigeria (low investment cost)'and Complementary_tech == 'not':
	TI=Price_3
	disp_col.write(Price_3)

elif User_country == 'DR. Congo (intermediate investment cost)'and Complementary_tech == 'not':
	TI=Price_2
	disp_col.write(Price_2)




#Cost of cassava roots and processing cost + flour selling price 

Cassava_cost = sel_col.slider('What is the cost of one(1) Ton of cassava roots in a locality (in $USD)?', min_value=10, max_value=350, value=60, step=10)
CCP= Cassava_cost

Flour_price = sel_col.slider('What is the selling price per 1 Ton of HQCF (at factory gate) (in $USD)?', min_value=100, max_value=1500, value=350, step=50)
FP= Flour_price

disp_col.write('Data collected in the countries under study allow us to conclude that the price of roots is on average 75% of flour processing costs (using ratio flour/roots= 1:3.5). Therefore, we could infer that the processing costs could be: ')

disp_col.write('**Cassava flour processing costs per Ton ($USD)**')

CPC =((CCP*3.5)/0.75)
disp_col.markdown(round(CPC,2))

#participation of the type of origin of the investment

sel_col.write('**Please specify the percentage of participation of the type of origin of the investment**')
Owm_Resourses = sel_col.selectbox('Own resources(in %)', options=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], index=0)
Bank_loan = 100-(int(Owm_Resourses))
sel_col.write('Bank loan (in %):')
sel_col.write(Bank_loan)

if int(Owm_Resourses)!=0:
	opportunity_rate = sel_col.slider('what is the annual Opportunity cost of the investment(in %)', min_value=1, max_value=25, value=3, step=1)
elif int(Owm_Resourses)==0:
	opportunity_rate=0


#Estimation of Number of payments of the credit (if any)

if int(Bank_loan)!=0:
	annual_rate = sel_col.slider('what is the annual rate of bank interest(in %)', min_value=1, max_value=25, value=12, step=1)
	Time_loan = sel_col.selectbox('Time (in years) to repay the bank loan', options=[1,2,3,4,5,6,7,8,9,10], index=0)
	interest = annual_rate/100
	loan = (Bank_loan/100)* TI
	n=Time_loan
	pay_up= interest*loan
	pay_down= 1-(pow((1+interest),-n))
	payments= pay_up/pay_down
	total_interes=((payments*n)-loan)

	disp_col.write('**Loan Individual payments(each year)**')
	disp_col.write(payments)
	disp_col.write('**Payment in full at the end of the credit period**')
	disp_col.write(payments*n)
	disp_col.write('**Value of credit requested**')
	disp_col.write(loan)
	disp_col.write('**Total value of interest to be covered**')
	disp_col.write(total_interes)


if int(Bank_loan)>0:
	total_interes=((payments*n)-loan)
elif int(Bank_loan)==0:
		total_interes=0
if int(Bank_loan)==0:
	Time_loan=1
	loan=0

#cashflow
#factor = 8(hour)*6(days/week)*4(weeks)*12(monts)=2304/1000 to Tons = 2.304
#55% of capacity 1est year and 67% the more than 2cond year

#Sales of HQCF US$
Sa=(CY*FP*2.304*0.55)
Sb=(CY*FP*2.304*0.67)

#Production costs
pca=(CY*CPC*2.304*0.55)
pcb=(CY*CPC*2.304*0.67)
amr=int(TI)/10

#EBIT (cost of depreciation)
EBITa= ((Sa-pca)-amr)
EBITb= ((Sb-pcb)-amr)

#Interest on bank loans

int_1=int(total_interes)/int(Time_loan)

if int(Time_loan)>=2:
	int_2=int(total_interes)/int(Time_loan)
elif int(Time_loan)<2:
	int_2=0

if int(Time_loan)>=3:
	int_3=int(total_interes)/int(Time_loan)
elif int(Time_loan)<3:
	int_3=0

if int(Time_loan)>=4:
	int_4=int(total_interes)/int(Time_loan)
elif int(Time_loan)<4:
	int_4=0

if int(Time_loan)>=5:
	int_5=int(total_interes)/int(Time_loan)
elif int(Time_loan)<5:
	int_5=0

if int(Time_loan)>=6:
	int_6=int(total_interes)/int(Time_loan)
elif int(Time_loan)<6:
	int_6=0

if int(Time_loan)>=7:
	int_7=int(total_interes)/int(Time_loan)
elif int(Time_loan)<7:
	int_7=0

if int(Time_loan)>=8:
	int_8=int(total_interes)/int(Time_loan)
elif int(Time_loan)<8:
	int_8=0

if int(Time_loan)>=9:
	int_9=int(total_interes)/int(Time_loan)
elif int(Time_loan)<9:
	int_9=0

if int(Time_loan)==10:
	int_10=int(total_interes)/int(Time_loan)
elif int(Time_loan)<10:
	int_10=0

#Interest of opportunity cost on investment capital
opp= (int(TI)*(int(opportunity_rate)/100))/10

#Income tax (%) as 10%

if int(EBITa) >0:
	taxa= (EBITa*0.1)
elif int(EBITa)<=0:
	taxa= 0

if int(EBITb) >0:
	taxb= (EBITb*0.1)
elif int(EBITb)<=0:
	taxb= 0

#Net profit (earnings)

Net_P1= int(EBITa)-(int(int_1)+int(opp)+int(taxa))
Net_P2= int(EBITb)-(int(int_2)+int(opp)+int(taxb))
Net_P3= int(EBITb)-(int(int_3)+int(opp)+int(taxb))
Net_P4= int(EBITb)-(int(int_4)+int(opp)+int(taxb))
Net_P5= int(EBITb)-(int(int_5)+int(opp)+int(taxb))
Net_P6= int(EBITb)-(int(int_6)+int(opp)+int(taxb))
Net_P7= int(EBITb)-(int(int_7)+int(opp)+int(taxb))
Net_P8= int(EBITb)-(int(int_8)+int(opp)+int(taxb))
Net_P9= int(EBITb)-(int(int_9)+int(opp)+int(taxb))
Net_P10= int(EBITb)-(int(int_10)+int(opp)+int(taxb))

#amortization of capital

cap_1=int(loan)/int(Time_loan)

if int(Time_loan)>=2:
	cap_2=int(loan)/int(Time_loan)
elif int(Time_loan)<2:
	cap_2=0

if int(Time_loan)>=3:
	cap_3=int(loan)/int(Time_loan)
elif int(Time_loan)<3:
	cap_3=0

if int(Time_loan)>=4:
	cap_4=int(loan)/int(Time_loan)
elif int(Time_loan)<4:
	cap_4=0

if int(Time_loan)>=5:
	cap_5=int(loan)/int(Time_loan)
elif int(Time_loan)<5:
	cap_5=0

if int(Time_loan)>=6:
	cap_6=int(loan)/int(Time_loan)
elif int(Time_loan)<6:
	cap_6=0

if int(Time_loan)>=7:
	cap_7=int(loan)/int(Time_loan)
elif int(Time_loan)<7:
	cap_7=0

if int(Time_loan)>=8:
	cap_8=int(loan)/int(Time_loan)
elif int(Time_loan)<8:
	cap_8=0

if int(Time_loan)>=9:
	cap_9=int(loan)/int(Time_loan)
elif int(Time_loan)<9:
	cap_9=0

if int(Time_loan)==10:
	cap_10=int(loan)/int(Time_loan)
elif int(Time_loan)<10:
	cap_10=0

#NET balance

N_bal1= (int(amr)+int(Net_P1))-int(cap_1)
N_bal2= (int(amr)+int(Net_P2))-int(cap_2)
N_bal3= (int(amr)+int(Net_P3))-int(cap_3)
N_bal4= (int(amr)+int(Net_P4))-int(cap_4)
N_bal5= (int(amr)+int(Net_P5))-int(cap_5)
N_bal6= (int(amr)+int(Net_P6))-int(cap_6)
N_bal7= (int(amr)+int(Net_P7))-int(cap_7)
N_bal8= (int(amr)+int(Net_P8))-int(cap_8)
N_bal9= (int(amr)+int(Net_P9))-int(cap_9)
N_bal10= (int(amr)+int(Net_P10))-int(cap_10)

#Accumulated balance 

Acc_b1=int(N_bal1)
Acc_b2=int(N_bal2)+int(Acc_b1)
Acc_b3=int(N_bal3)+int(Acc_b2)
Acc_b4=int(N_bal4)+int(Acc_b3)
Acc_b5=int(N_bal5)+int(Acc_b4)
Acc_b6=int(N_bal6)+int(Acc_b5)
Acc_b7=int(N_bal7)+int(Acc_b6)
Acc_b8=int(N_bal8)+int(Acc_b7)
Acc_b9=int(N_bal9)+int(Acc_b8)
Acc_b10=int(N_bal10)+int(Acc_b9)

st.subheader('Cash Flow')

def load_data():
	df=pd.DataFrame(datos3)
	df_reset=df.set_index('Cash_Flow')
	return df_reset

datos3 = {'Year_1':[Sa,pca,(Sa-pca),amr,EBITa,int_1,opp,taxa,Net_P1,amr,Net_P1,cap_1,N_bal1,Acc_b1],
	'Year_2':[Sb,pcb,(Sb-pcb),amr,EBITb,int_2,opp,taxb,Net_P2,amr,Net_P2,cap_2,N_bal2,Acc_b2],
	'Year_3':[Sb,pcb,(Sb-pcb),amr,EBITb,int_3,opp,taxb,Net_P3,amr,Net_P3,cap_3,N_bal3,Acc_b3],
	'Year_4':[Sb,pcb,(Sb-pcb),amr,EBITb,int_4,opp,taxb,Net_P4,amr,Net_P4,cap_4,N_bal4,Acc_b4],
	'Year_5':[Sb,pcb,(Sb-pcb),amr,EBITb,int_5,opp,taxb,Net_P5,amr,Net_P5,cap_5,N_bal5,Acc_b5],
	'Year_6':[Sb,pcb,(Sb-pcb),amr,EBITb,int_6,opp,taxb,Net_P6,amr,Net_P6,cap_6,N_bal6,Acc_b6],
	'Year_7':[Sb,pcb,(Sb-pcb),amr,EBITb,int_7,opp,taxb,Net_P7,amr,Net_P7,cap_7,N_bal7,Acc_b7],
	'Year_8':[Sb,pcb,(Sb-pcb),amr,EBITb,int_8,opp,taxb,Net_P8,amr,Net_P8,cap_8,N_bal8,Acc_b8],
	'Year_9':[Sb,pcb,(Sb-pcb),amr,EBITb,int_9,opp,taxb,Net_P9,amr,Net_P9,cap_9,N_bal9,Acc_b9],
	'Year_10':[Sb,pcb,(Sb-pcb),amr,EBITb,int_10,opp,taxb,Net_P10,amr,Net_P10,cap_10,N_bal10,Acc_b10],
	'Cash_Flow':['Sales of HQCF US$','Production costs US$','EBITDA* (Operating results) US$','Costs of depreciation & maintenance US$','EBIT** US$','Interest on bank loans US$','Interest of opportunity cost on investment capital US$','Taxes US$','Net profit (earnings) US$','Depreciation US$','Results for each period US$','Loans amortized (repayment of capital to bank) US$','Net balance US$','Accumulated balance US$']}

datos3 = load_data()

st.write(datos3)
st.write('*EBITDA= Earnings Before Interest, Taxes, Depreciation & Amortization')
st.write('**EBIT= Earnings Before Interest & Taxes')

st.subheader('Evaluation of economic indicators')

cashflows = [-int(TI),int(Net_P1),int(Net_P2),int(Net_P3),int(Net_P4),int(Net_P5),int(Net_P6),int(Net_P7),int(Net_P8),int(Net_P9),int(Net_P10)]
rate=opportunity_rate/100

npv =npf.npv(rate,cashflows)
irr =npf.irr(cashflows)
st.write(f"Internal rate of return (IRR): {round(irr*100,2)}%")
st.write(f"Net present value (NPV): ${round(npv,2)}")
st.write(f"Financial viability: ${round((int(npv)-int(TI)),2)}")


#PV = (int(Net_P1)/(1+(float(rate))) + (int(Net_P2)/(1+(float(rate))**2)) + (int(Net_P3)/(1+(float(rate))**3)) + (int(Net_P4)/(1+(float(rate))**4)) + (int(Net_P5)/(1+(float(rate))**5)) +(int(Net_P6)/(1+(float(rate))**6)) + (int(Net_P7)/(1+(float(rate))**7)) + (int(Net_P8)/(1+(float(rate))**8)) + (int(Net_P9)/(1+(float(rate))**9)) + (int(Net_P10)/(1+(float(rate))**10)))
#NPV2 = PV - int(TI)
#st.write(f"Net present value (NPV): ${round(NPV2,1)}")


st.write("""
# Tips To evaluate the feasibility of the project. 

The **internal rate of return (or profitability of the project)** should be at least the one expected by the investors (indicated in the space "opportunity costs"). Some experts in the cassava flour industry consider that the minimum profitability of cassava flour processing should be 15-20%.

**The net present value (NPV)** brings the future cash flows to a current present value, taking the "opportunity cost" rate as the discount rate. This analysis allows to see the future profits (or losses) of the project, at the current rate of money. This value is expected to be positive and significantly higher than the total investment of the project. Additionally, this variable is considered the value of the project. If investors want to sell the project, this should be the minimum sale value.

**The financial viability** of the project is the difference between the net present value (NPV) and the total initial investment of the project. This is the profit obtained by the investors once the resources obtained have been recovered. 

If i) the cash flow is positive and increasing over time, ii) the profitability of the project (%) is higher than the opportunity cost (%) and iii) the investment generates value because the viability of the project gives a positive value, it could be concluded that the project is attractive for investment.

""")

st.markdown('*Copyright (C) 2021 CIRAD & CIAT*')
st.markdown('**Authors: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Thierry Tran (thierry.tran@cirad.fr)**')


image = Image.open('logo_rtb.png')
st.image(image)

image = Image.open('cirad_logo.png')
st.image(image)

image = Image.open('CIAT_logo.png')
st.image(image)

image = Image.open('IITA_logo.png')
st.image(image)

