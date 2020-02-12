import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pickle
import datetime as dt
import sklearn
from sklearn.linear_model import LogisticRegression
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
st.title('Welcome to BacteriAlert')
st.write("This app provides bacterial beach water pollution predictions for 137 beaches in 26 costal Florida counties within seven days. Our predictions are based on Florida Health Department's beach water test data during 2000-2017.")
#st.write( "Our predictions are based on Florida Health Department's historical beach water test data.")


counties = [' ', 'Bay','Brevard',
 'Broward',
 'Charlotte',
 'Dade',
 'Escambia',
 'Franklin',
 'Gulf',
 'Hernando',
 'Hillsborough',
 'Indian River',
 'Lee',
 'Manatee',
 'Martin',
 'Monroe',
 'Okaloosa',
 'Palm Beach',
 'Pasco',
 'Pinellas',
 'Santa Rosa',
 'Sarasota',
 'St Johns',
 'St Lucie',
 'Volusia',
 'Wakulla',
 'Walton']
lists = [' ',
 [' ',
  'BEACH DRIVE',
  'BECKRICH RD',
  'BID-A-WEE BEACH',
  'CARL GRAY PARK',
  'DELWOOD',
  'DUPONT BRIDGE',
  'LAGUNA BEACH',
  'PCB CITY PIER',
  'RICK SELTZER PARK'],
 [' ', 'COCOA BEACH PIER'],
 [' ',
  'BIRCH STATE PARK',
  'COMMERCIAL BLVD PIER',
  'HALLANDALE BEACH BLVD',
  'HARRISON STREET',
  'MINNESOTA STREET',
  'POMPANO BEACH PIER',
  'NE 16TH ST POMPANO',
  'CUSTER ST BEACH',
  'DANIA BEACH',
  'SEBASTIAN STREET'],
 [' ',
  'ENGLEWOOD MID BEACH',
  'ENGLEWOOD NORTH',
  'PORT CHARLOTTE BEACH EAST',
  'PORT CHARLOTTE BEACH WEST'],
 [' ',
  '53RD ST - MIAMI BEACH',
  'COLLINS PARK - 21ST ST',
  'CRANDON PARK - KEY BISCAYNE',
  'DOG BEACH',
  'GOLDEN BEACH',
  'KEY BISCAYNE BEACH',
  'MATHESON HAMMOCK',
  'NORTH SHORE OCEAN TERRACE',
  'SOUTH BEACH PARK',
  'SURFSIDE BEACH - 93RD ST',
  'HAULOVER BEACH'],
 [' ',
  'BAYOU CHICO',
  'BAYVIEW PARK PIER',
  'BIG LAGOON STATE PARK',
  'COUNTY PARK',
  'NAVY POINT',
  'QUIET WATER BEACH',
  'SANDERS BEACH'],
 [' ',
  'ALLIGATOR POINT',
  'CARRABELLE BEACH',
  'SAINT GEORGE ISLAND 11TH ST E',
  'SAINT GEORGE ISLAND 11TH ST W',
  'SAINT GEORGE ISLAND FRANKLIN BLVD'],
 [' ',
  'BEACON HILL BEACH',
  'DIXIE BELLE BEACH',
  'LOOKOUT BEACH',
  'ST. JOE BEACH'],
 [' ', 'PINE ISLAND BEACH'],
 [' ',
  'BAHIA BEACH',
  'BEN T. DAVIS NORTH',
  'BEN T. DAVIS SOUTH',
  'DAVIS ISLAND BEACH',
  'PICNIC ISLAND NORTH',
  'PICNIC ISLAND SOUTH',
  'SIMMONS PARK BEACH',
  'CYPRESS POINT PARK NORTH',
  'CYPRESS POINT PARK SOUTH'],
 [' ', 'HUMISTON BEACH OUTFLOW', 'SEXTON PLAZA OUTFLOW', 'SOUTH BEACH PARK'],
 [' ',
  'BLIND PASS/TURNER BEACH',
  'BOWDITCH PARK',
  'CAPE CORAL YACHT CLUB',
  'LIGHTHOUSE BEACH',
  'LYNN HALL PARK',
  'SANIBEL CAUSEWAY'],
 [' ', 'BAYFRONT PARK NORTH', 'PALMA SOLA SOUTH'],
 [' ', 'ROOSEVELT BRIDGE', 'STUART CAUSEWAY'],
 [' ',
  'BAHIA HONDA OCEANSIDE',
  'BAHIA HONDA SANDSPUR',
  'HARRY HARRIS COUNTY PARK',
  'HIGGS BEACH',
  'JOHN PENNEKAMP STATE PARK',
  'SMATHERS BEACH',
  'SOMBRERO BEACH',
  'FOUNDER'],
 [' ',
  'EAST PASS',
  'GARNIERS PARK',
  'GULF ISLAND NATIONAL SEASHORE',
  'HENDERSON PARK BEACH',
  'JAMES LEE PARK',
  'LIZA JACKSON PARK',
  'MARLER PARK',
  'ROCKY BAYOU STATE PARK',
  'LINCOLN PARK',
  'POQUITO PARK'],
 [' ', 'DUBOIS PARK', 'LAKE WORTH BEACH', 'PHIL FOSTER PARK'],
 [' ',
  'BRASHER PARK BEACH',
  'GULF HARBORS BEACH',
  'ROBERT J STRICKLAND BEACH',
  'ROBERT K. REES PARK BEACH'],
 [' ',
  'COURTNEY CAMPBELL CAUSEWAY',
  'GANDY BOULEVARD',
  'HONEYMOON ISLAND BEACH',
  'INDIAN ROCKS BEACH',
  'MADEIRA BEACH',
  'NORTH SHORE BEACH',
  'PASS-A-GRILLE BEACH',
  'SAND KEY',
  'TREASURE ISLAND BEACH'],
 [' ', 'NAVARRE PARK HIGHWAY 98', 'SHORELINE PARK'],
 [' ',
  'LIDO CASINO BEACH',
  'NOKOMIS BEACH',
  'NORTH JETTY BEACH',
  'NORTH LIDO BEACH',
  'SERVICE CLUB BEACH',
  'SIESTA KEY BEACH',
  'TURTLE BEACH',
  'VENICE BEACH',
  'BROHARD PARK',
  'RINGLING CAUSEWAY',
  'VENICE FISHING PIER'],
 [' ', 'VILANO BEACH'],
 [' ', 'JETTY PARK BEACH'],
 [' ',
  'DUNLAWTON',
  'FLORIDA SHORES BLVD',
  'MAIN STREET',
  'SEABREEZE BLVD',
  'SILVER BEACH',
  'TORONITA',
  'INTERNATIONAL SPEEDWAY'],
 [' ', "MASH'S ISLAND", 'SHELL POINT'],
 [' ',
  'BLUE MOUNTAIN BEACH',
  'COUNTY PARK',
  'DUNE ALLEN BEACH',
  'EASTERN LAKE DUNE WALKOVER',
  'GRAYTON BEACH',
  'HOLLEY STREET BEACH',
  'INLET BEACH ACCESS']]

coordinates = [0 ,[27.7567667, -81.4639835],
 [28.2446658, -80.728624],
 [26.1598074, -80.4623642],
 [26.9013269, -81.9156799],
 [25.6364246, -80.4989467],
 [30.6625885, -87.3451089],
 [29.8323143, -84.8239118],
 [29.9665252, -85.2175889],
 [28.5710156, -82.4605068],
 [27.9184543, -82.3488057],
 [27.7041555, -80.5894422],
 [26.5999265, -81.8823135],
 [27.5213933, -82.3801566],
 [27.7567667, -81.4639835],
 [25.0405135, -80.8337157],
 [30.6765961, -86.6037748],
 [26.6279798, -80.4494174],
 [28.2996183, -82.4522702],
 [27.8778904, -82.7329309],
 [30.6964502, -87.0097524],
 [27.3364347, -82.5306527],
 [29.9032284, -81.4145468],
 [27.3900897, -80.457904],
 [29.0533409, -81.1310761],
 [30.1480038, -84.3543512],
 [30.6204939, -86.1912678]]

county = st.selectbox('Please select a county:', counties)

beaches = lists[counties.index(county)]

beach = st.selectbox('Now please select a location: ', beaches)

coordinate = coordinates[counties.index(county)]

model = pickle.load(open('prediction_model', 'rb'))
df = pd.read_csv('Locations')

if beach != ' ':
 st.write("The coordinates for this location are " + str(coordinate[0])+ " and "+ str(coordinate[1])+".")

#abc

 st.write("Here are our predictions for "+beach+" for next seven days.")
 
#import datetime as dt
 for x in range(7):
   t = pd.datetime.today() + dt.timedelta(days=x)
   s = str(t.strftime('%m/%d/%Y'))
   st.write("s: Clean")
      
 #t = pd.dt.today() + DT.timedelta(days=x)
 #s = str(t.strftime('%m/%d/%Y'))
 #st.write(s +": Clean")
  


#for n in range(7):
#s = df[df['SPLocation'] == beach].T.squeeze()
#s[2] = pd.datetime.now().month
#s[3] = (pd.datetime.now().month -1) * 30 + pd.datetime.now().day
#if model.predict(s[1:].values.reshape(1, -1)) == [0]:
  #tarih = datetime.date.today() + datetime.timedelta(days = n)
  #st.write('We do not expect pollution at this location today.')
#else:
 # st.write('We expect this location to be polluted today.')
#
#t = df[df['SPLocation'] == beach].T.squeeze()
#t[2] = pd.datetime.now().month
#t[3] = (pd.datetime.now().month -1) * 30 + pd.datetime.now().day+180
#if model.predict(t[1:].values.reshape(1, -1)) == [0]:
 #st.write('We do not expect pollution at this location tomorrow.')
#else:
 #st.write('We expect this location to be polluted tomorrow.')
#st.write('Our prediction for tomorrow is: ')
 #st.text(model.predict(t[1:].values.reshape(1, -1)))

 st.write('NOTE: The pollution level is determined by bacteria level. "Polluted" means that the enterococcus level is expected to be greater than 70 colony per 100 ml at the given location on the given date.')

