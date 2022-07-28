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
  Clen = 0.15 * Plen
  Cwid = 0.15 * Pwid
  Chei = 0.15 * Phei
  Nl = Nw = Nh = N = 0
  a = 0.2285
  F = 0
  mP = PartWeight
  mT = 100
  for i in range (1,100):
    if (Plen*i)+(Clen*(i+1)) < 1400 and F < 16:
        Tlen = (Plen*i)+(Clen*(i+1))
        #print('{} Len block'.format(i))
        Nl = i
    else: 
        pass
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972

    if (Pwid*i)+(Cwid*(i+1)) < 1000 and F < 16:
        Twid = (Pwid*i)+(Cwid*(i+1))
        #print('{} Width block'.format(i))
        Nw = i
    else: 
        pass
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972

    if (Phei*i)+(Chei*(i+1))+Ghei < 1500 and F < 16:
        Thei = (Phei*i)+(Chei*(i+1))+Ghei
        #print('{} height block {}'.format(i, Thei))
        Nh = i
    else: 
        pass 
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
  df = pd.DataFrame({
    'Parameters' : 'Value',
    'Trolley Length (mm)': Tlen,
    'Trolley Width (mm)': Twid,
    'Trolley Height (mm)': Thei,
    'Capacity': Nl*Nw*Nh,
    'Pulling Force (kgf)': F,
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
  for i in range (1,100):
    if (Plen*i)+(Clen*(i+1)) < 1400 and F < 16:
      Tlen = (Plen*i)+(Clen*(i+1))
      #print('{} Len block'.format(i))
      Nl = i
    else: 
      pass
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    
    if (Pwid*i)+(Cwid*(i+1)) < 1000 and F < 16:
      Twid = (Pwid*i)+(Cwid*(i+1))
      #print('{} Width block'.format(i))
      Nw = i
    else: 
      pass
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    
    if (Phei*i)+(Chei*(i+1))+Ghei < int(1500*1.2) and F < 16:
      Thei = (Phei*i)+(Chei*(i+1))+Ghei
      #print('{} height block {}'.format(i, Thei))
      Nh = i
    else: 
      pass 
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
  df2 = pd.DataFrame({
    'Parameters' : 'Value',
    'Trolley Length (mm)': Tlen,
    'Trolley Width (mm)': Twid,
    'Trolley Height (mm)': Thei,
    'Capacity': Nl*Nw*Nh,
    'Pulling Force (kgf)': F,
  }, index=[0])    
  #return([Tlen,Twid, Thei, Nl, Nw, Nh, np.prod([Nl,Nw,Nh]),round(F,3)], Clen, Cwid, Chei)
  print(df2)
  return df2
  

def trolley_dim_detector(Plen, Pwid, Phei, PartWeight, Clen, Cwid, Chei, Ghei):
  Tlen = Twid = Thei = 0
  Nl = Nw = Nh = N = 0
  a = 0.2285
  F = 0
  mP = PartWeight
  mT = 100
  for i in range (1,100):
    if (Plen*i)+(Clen*(i+1)) < 1400 and F < 16:
      Tlen = (Plen*i)+(Clen*(i+1))
      #print('{} Len block'.format(i))
      Nl = i
    else: 
      pass
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    
    if (Pwid*i)+(Cwid*(i+1)) < 1000 and F < 16:
      Twid = (Pwid*i)+(Cwid*(i+1))
      #print('{} Width block'.format(i))
      Nw = i
    else: 
      pass
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
    
    if (Phei*i)+(Chei*(i+1))+Ghei < 1500 and F < 16:
      Thei = (Phei*i)+(Chei*(i+1))+Ghei
      #print('{} height block {}'.format(i, Thei))
      Nh = i
    else: 
      pass 
    F = (mT + (mP*Nl*Nw*Nh))*a*0.10972
  df3 = pd.DataFrame({
    'Parameters' : 'Value',
    'Trolley Length (mm)': Tlen,
    'Trolley Width (mm)': Twid,
    'Trolley Height (mm)': Thei,
    'Capacity': Nl*Nw*Nh,
    'Pulling Force (kgf)': F,
  }, index=[0])    
  #return([Tlen,Twid, Thei, Nl, Nw, Nh, np.prod([Nl,Nw,Nh]),round(F,3)], Clen, Cwid, Chei)
  return df3
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
Ghei = stm.number_input("enter the gorund clearance for the the trolley")
# check = stm.checkbox('Select if you want to auto calculate clearance between parts', help = 'distance between parts', )
# check2 = stm.checkbox('Select if you want to protrude higher than the height of the trolley')

check4 = stm.radio("Choose the appropriate", ('Select if you want to auto calculate clearance between parts', 'Select if you want to protrude higher than the height of the trolley', 'Select if you want to calculate it normally'))

if check4 == 'Select if you want to auto calculate clearance between parts':
     stm.write('Part to part clearance will be calculated automatically \n 15 "%" of the dimension ')
else:
    clen = stm.number_input("Enter the clearance between parts in length direction ")
    cwid = stm.number_input("Enter the clearance between parts in Width direction ")
    chei = stm.number_input("Enter the clearance between parts in Height direction ")

check3 = stm.button('Calculate')


if check3:
    stm.write(director(check4))
    print(director(check4))
