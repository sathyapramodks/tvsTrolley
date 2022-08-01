import streamlit as stm
import requests
import pandas as pd
"""
# Trolley Dimension Determination
This page is used to determine the Dimension if the trolley, Pulling force required to push / pull the entire trolley and trolley capacity

Enter the part details below

"""

def trolley_dim_detector_AutoClearance(Plen, Pwid, Phei, PartWeight, Ghei):
  Tlen = Twid = Thei = 0
  Nl = Nw = Nh = N = 0
  a = 0.2285
  F = 0
  Clen = Plen * 0.15
  Cwid = Pwid *0.15
  Chei = Phei *0.15
  #Flst = []
  mP = PartWeight
  mT = 100
  i = 1
  while F < 16:
    if (Tlen+(Plen+Clen)<1400) or (Twid+Pwid+Cwid<1000) or (Thei+Phei+Chei<1500):
        if (Plen*i)+(Clen*(i+1)) < 1400:
          Tlen = (Plen*i)+(Clen*(i+1))
          Nl=Nl+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nl -= 1
            break
        if (Pwid*i)+(Cwid*(i+1)) < 1000:
          Twid = (Pwid*i)+(Cwid*(i+1))
          Nw=Nw+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nw -= 1
            break
        if (Phei*i)+(Chei*(i+1))+Ghei < (1500+(1500*0.15)):
          Thei = (Phei*i)+(Chei*(i+1))+Ghei
          Nh=Nh+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nh -= 1
            break
    else:
        break
    #F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    #Flst.append(F)
    i+=1
  df = pd.DataFrame({
    'Parameters' : 'Value',
    'Trolley Length (mm)': Tlen,
    'Trolley Width (mm)': Twid,
    'Trolley Height (mm)': Thei,
    'Capacity': Nl*Nw*Nh,
    'Pulling Force (kgf)': (mT + (mP*Nl*Nw*Nh))*a*0.10972,
  }, index=[0])    
  #return([Tlen,Twid, Thei, Nl, Nw, Nh, np.prod([Nl,Nw,Nh]),round(F,3)], Clen, Cwid, Chei)
  return df

# code functioning based on Part height consideration
def trolley_dim_detector_partHeight(Plen, Pwid, Phei, PartWeight, Clen, Cwid, Chei, Ghei):
  Tlen = Twid = Thei = 0
  Nl = Nw = Nh = N = 0
  a = 0.2285
  F = 0
  mP = PartWeight
  mT = 100
  i = 1
  while F < 16:
    if (Tlen+(Plen+Clen)<1400) or (Twid+Pwid+Cwid<1000) or (Thei+Phei+Chei<1500):
        if (Plen*i)+(Clen*(i+1)) < 1400:
          Tlen = (Plen*i)+(Clen*(i+1))
          Nl=Nl+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nl -= 1
            break
        if (Pwid*i)+(Cwid*(i+1)) < 1000:
          Twid = (Pwid*i)+(Cwid*(i+1))
          Nw=Nw+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nw -= 1
            break
        if (Phei*i)+(Chei*(i+1))+Ghei < (1500+(1500*0.15)):
          Thei = (Phei*i)+(Chei*(i+1))+Ghei
          Nh=Nh+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nh -= 1
            break
    else:
        break
    #F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    #Flst.append(F)
    i+=1
  df = pd.DataFrame({
    'Parameters' : 'Value',
    'Trolley Length (mm)': Tlen,
    'Trolley Width (mm)': Twid,
    'Trolley Height (mm)': Thei,
    'Capacity': Nl*Nw*Nh,
    'Pulling Force (kgf)': (mT + (mP*Nl*Nw*Nh))*a*0.10972,
  }, index=[0])    
  #return([Tlen,Twid, Thei, Nl, Nw, Nh, np.prod([Nl,Nw,Nh]),round(F,3)], Clen, Cwid, Chei)
  return df
  

def trolley_dim_detector(Plen, Pwid, Phei, PartWeight, Clen, Cwid, Chei, Ghei):
  Tlen = Twid = Thei = 0
  Nl = Nw = Nh = N = 0
  a = 0.2285
  F = 0
  mP = PartWeight
  mT = 100
  i = 1
  while F < 16:
    if (Tlen+(Plen+Clen)<1400) or (Twid+Pwid+Cwid<1000) or (Thei+Phei+Chei<1500):
        if (Plen*i)+(Clen*(i+1)) < 1400:
          Tlen = (Plen*i)+(Clen*(i+1))
          Nl=Nl+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nl -= 1
            break
        if (Pwid*i)+(Cwid*(i+1)) < 1000:
          Twid = (Pwid*i)+(Cwid*(i+1))
          Nw=Nw+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nw -= 1
            break
        if (Phei*i)+(Chei*(i+1))+Ghei < 1500:
          Thei = (Phei*i)+(Chei*(i+1))+Ghei
          Nh=Nh+1
          F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
        if F>16:
            Nh -= 1
            break
    else:
        break
    #F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    #Flst.append(F)
    i+=1
  df = pd.DataFrame({
    'Parameters' : 'Value',
    'Trolley Length (mm)': Tlen,
    'Trolley Width (mm)': Twid,
    'Trolley Height (mm)': Thei,
    'Capacity': Nl*Nw*Nh,
    'Pulling Force (kgf)': (mT + (mP*Nl*Nw*Nh))*a*0.10972,
  }, index=[0])    
  #return([Tlen,Twid, Thei, Nl, Nw, Nh, np.prod([Nl,Nw,Nh]),round(F,3)], Clen, Cwid, Chei)
  return df
  #return([Tlen,Twid, Thei, Nl, Nw, Nh, np.prod([Nl,Nw,Nh]),round(F,3)])



# director
def director(check):
    if check == 'Select if you want to auto calculate clearance between parts':
        return trolley_dim_detector_AutoClearance(Plen = Plen ,Pwid =  Pwid, Phei =  Phei, PartWeight = PartWeight, Ghei = Ghei)
    elif check == 'Select if you want to protrude higher than the height of the trolley':
        return trolley_dim_detector_partHeight(Plen = Plen ,Pwid =  Pwid, Phei =  Phei, PartWeight = PartWeight, Ghei = Ghei, Clen = clen, Cwid = cwid, Chei = chei)
    else:
        return trolley_dim_detector(Plen = Plen ,Pwid =  Pwid, Phei =  Phei, PartWeight = PartWeight, Ghei = Ghei, Clen = clen, Cwid = cwid, Chei = chei)

Plen = stm.number_input('Enter the length of the Bounding (mm)')
Pwid = stm.number_input("enter the width of the Bounding box (mm)")
Phei = stm.number_input("Enter the height of the Bounding box (mm)")
PartWeight = stm.number_input('Enter the weigth of the part (kg)')
Ghei = stm.number_input("Enter the gorund clearance for the the trolley (mm)")
# check = stm.checkbox('Select if you want to auto calculate clearance between parts', help = 'distance between parts', )
# check2 = stm.checkbox('Select if you want to protrude higher than the height of the trolley')

check4 = stm.radio("Choose the appropriate", ('Select if you want to auto calculate clearance between parts', 'Select if you want to protrude higher than the height of the trolley', 'Select if you want to calculate it normally'))

if check4 == 'Select if you want to auto calculate clearance between parts':
     stm.write('Part to part clearance will be calculated automatically \n 15% of the dimension ')
elif check4 == 'Select if you want to protrude higher than the height of the trolley':
    stm.write('Parts can be stored to a maximum height of 15% the maximum trolley height')
    clen = stm.number_input("Enter the clearance between parts in length direction ")
    cwid = stm.number_input("Enter the clearance between parts in Width direction ")
    chei = stm.number_input("Enter the clearance between parts in Height direction ")
else:
    clen = stm.number_input("Enter the clearance between parts in length direction ")
    cwid = stm.number_input("Enter the clearance between parts in Width direction ")
    chei = stm.number_input("Enter the clearance between parts in Height direction ")

check3 = stm.button('Calculate')


if check3:
    stm.write(director(check4))
    print(director(check4))
