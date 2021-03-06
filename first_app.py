import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pickle
import datetime as dt
import sklearn
import plotly.graph_objects as go


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
st.write("This app provides bacterial beach water pollution predictions for Florida. It covers 137 beaches across 26 coastal counties predicting over seven days. Our predictions are based on Florida Health Department's beach water test data during 2000-2017.")
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

allbeaches = ['BEACH DRIVE',
 'BECKRICH RD',
 'BID-A-WEE BEACH',
 'CARL GRAY PARK',
 'DELWOOD',
 'DUPONT BRIDGE',
 'LAGUNA BEACH',
 'PCB CITY PIER',
 'RICK SELTZER PARK',
 'COCOA BEACH PIER',
 'BIRCH STATE PARK',
 'COMMERCIAL BLVD PIER',
 'HALLANDALE BEACH BLVD',
 'HARRISON STREET',
 'MINNESOTA STREET',
 'NE 16TH ST POMPANO',
 'POMPANO BEACH PIER',
 'ENGLEWOOD MID BEACH',
 'ENGLEWOOD NORTH',
 'PORT CHARLOTTE BEACH EAST',
 'PORT CHARLOTTE BEACH WEST',
 '53RD ST - MIAMI BEACH',
 'COLLINS PARK - 21ST ST',
 'CRANDON PARK - KEY BISCAYNE',
 'DOG BEACH',
 'GOLDEN BEACH',
 'HAULOVER BEACH',
 'KEY BISCAYNE BEACH',
 'MATHESON HAMMOCK',
 'NORTH SHORE OCEAN TERRACE',
 'SOUTH BEACH PARK',
 'SURFSIDE BEACH - 93RD ST',
 'BAYOU CHICO',
 'BAYVIEW PARK PIER',
 'BIG LAGOON STATE PARK',
 'COUNTY PARK',
 'NAVY POINT',
 'QUIET WATER BEACH',
 'SANDERS BEACH',
 'ALLIGATOR POINT',
 'CARRABELLE BEACH',
 'SAINT GEORGE ISLAND 11TH ST E',
 'SAINT GEORGE ISLAND 11TH ST W',
 'SAINT GEORGE ISLAND FRANKLIN BLVD',
 'BEACON HILL BEACH',
 'DIXIE BELLE BEACH',
 'LOOKOUT BEACH',
 'ST. JOE BEACH',
 'PINE ISLAND BEACH',
 'BAHIA BEACH',
 'BEN T. DAVIS NORTH',
 'BEN T. DAVIS SOUTH',
 'DAVIS ISLAND BEACH',
 'PICNIC ISLAND NORTH',
 'PICNIC ISLAND SOUTH',
 'SIMMONS PARK BEACH',
 'HUMISTON BEACH OUTFLOW',
 'SEXTON PLAZA OUTFLOW',
 'BLIND PASS/TURNER BEACH',
 'BOWDITCH PARK',
 'CAPE CORAL YACHT CLUB',
 'LIGHTHOUSE BEACH',
 'LYNN HALL PARK',
 'SANIBEL CAUSEWAY',
 'BAYFRONT PARK NORTH',
 'PALMA SOLA SOUTH',
 'ROOSEVELT BRIDGE',
 'STUART CAUSEWAY',
 'BAHIA HONDA OCEANSIDE',
 'BAHIA HONDA SANDSPUR',
 'HARRY HARRIS COUNTY PARK',
 'HIGGS BEACH',
 'JOHN PENNEKAMP STATE PARK',
 'SMATHERS BEACH',
 'SOMBRERO BEACH',
 'EAST PASS',
 'GARNIERS PARK',
 'GULF ISLAND NATIONAL SEASHORE',
 'HENDERSON PARK BEACH',
 'JAMES LEE PARK',
 'LIZA JACKSON PARK',
 'MARLER PARK',
 'ROCKY BAYOU STATE PARK',
 'DUBOIS PARK',
 'LAKE WORTH BEACH',
 'PHIL FOSTER PARK',
 'BRASHER PARK BEACH',
 'GULF HARBORS BEACH',
 'ROBERT J STRICKLAND BEACH',
 'ROBERT K. REES PARK BEACH',
 'COURTNEY CAMPBELL CAUSEWAY',
 'GANDY BOULEVARD',
 'HONEYMOON ISLAND BEACH',
 'INDIAN ROCKS BEACH',
 'MADEIRA BEACH',
 'NORTH SHORE BEACH',
 'PASS-A-GRILLE BEACH',
 'SAND KEY',
 'TREASURE ISLAND BEACH',
 'NAVARRE PARK HIGHWAY 98',
 'SHORELINE PARK',
 'LIDO CASINO BEACH',
 'NOKOMIS BEACH',
 'NORTH JETTY BEACH',
 'NORTH LIDO BEACH',
 'SERVICE CLUB BEACH',
 'SIESTA KEY BEACH',
 'TURTLE BEACH',
 'VENICE BEACH',
 'VILANO BEACH',
 'JETTY PARK BEACH',
 'DUNLAWTON',
 'FLORIDA SHORES BLVD',
 'MAIN STREET',
 'SEABREEZE BLVD',
 'SILVER BEACH',
 'TORONITA',
 "MASH'S ISLAND",
 'SHELL POINT',
 'BLUE MOUNTAIN BEACH',
 'DUNE ALLEN BEACH',
 'EASTERN LAKE DUNE WALKOVER',
 'GRAYTON BEACH',
 'HOLLEY STREET BEACH',
 'CYPRESS POINT PARK NORTH',
 'CYPRESS POINT PARK SOUTH',
 'FOUNDER',
 'LINCOLN PARK',
 'POQUITO PARK',
 'BROHARD PARK',
 'RINGLING CAUSEWAY',
 'VENICE FISHING PIER',
 'INTERNATIONAL SPEEDWAY',
 'INLET BEACH ACCESS',
 'CUSTER ST BEACH',
 'DANIA BEACH',
 'SEBASTIAN STREET']

numbers = [44, 45, 46, 47, 48, 49,
 51,
 52,
 53,
 261,
 211,
 212,
 215,
 216,
 218,
 219,
 222,
 140,
 141,
 145,
 146,
 189,
 191,
 192,
 193,
 194,
 195,
 196,
 197,
 198,
 200,
 202,
 2,
 3,
 4,
 5,
 8,
 11,
 12,
 65,
 66,
 67,
 68,
 69,
 57,
 58,
 60,
 62,
 80,
 105,
 106,
 107,
 108,
 109,
 110,
 111,
 258,
 259,
 147,
 150,
 152,
 153,
 155,
 156,
 114,
 121,
 247,
 248,
 173,
 174,
 178,
 179,
 181,
 182,
 183,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 228,
 230,
 233,
 82,
 84,
 86,
 87,
 89,
 92,
 93,
 94,
 96,
 97,
 98,
 100,
 101,
 16,
 17,
 124,
 127,
 128,
 129,
 130,
 131,
 133, 134, 279, 251, 264, 266, 268, 269, 270, 271, 71, 72, 35, 37, 38, 39, 40, 112, 113, 185, 30, 31, 135, 136, 137, 274, 42, 224, 225, 227]

county = st.selectbox('Please select a county:', counties)

countybeaches = lists[counties.index(county)]

beach = st.selectbox('Now please select a location: ', countybeaches)

model = pickle.load(open('final_model_.pkl', 'rb'))

df = pd.read_csv('feed.csv')

if beach != ' ':
   
 #st.write("The coordinates for this location are " + str(coordinate[0])+ " and "+ str(coordinate[1])+".")
 beach_no = numbers[allbeaches.index(beach)]
 st.write("Here are our predictions for "+beach+" for next seven days:")
 st.write("------------------------------------------------------------")
 import datetime as dt
 
 for n in range(0,8):
   tarih = pd.datetime.today() + dt.timedelta(days = n)
   d = str(tarih.strftime('%Y-%m-%d'))
   dshow = str(tarih.strftime('%m/%d/%Y'))
   s = df[(df.County == county) & (df.Date == d)].T.squeeze()
   #st.markdown(s)
   s[1] = beach_no
   #st.markdown(s)
   #st.markdown(s[1:].values.reshape(1, -1))
   if model.predict(s[1:].values.reshape(1, -1)) == [0]:
      st.markdown(dshow + ": <span style='color:blue'>**Clean**</span>", unsafe_allow_html=True)
      #st.markdown("<span style='color:blue'>some **blue** text</span>", unsafe_allow_html=True)
   else:
      st.markdown(dshow + ": <span style='color:brown'>**Polluted**</span>", unsafe_allow_html=True)
      #st.markdown(dshow + ": <strong>Polluted</strong>", unsafe_allow_html=True)
 #for x in range(7): 
   #t = pd.datetime.today() + dt.timedelta(days=x)
   #s = str(t.strftime('%m/%d/%Y'))
   #st.write(s + ": Clean")
   #st.markdown(s + ": <strong>Clean</strong>", unsafe_allow_html=True)
 #t = pd.dt.today() + DT.timedelta(days=x)
 #s = str(t.strftime('%m/%d/%Y'))
 #st.write(s +": Clean")
 st.write("------------------------------------------------------------")



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

 st.write('**NOTE:** Pollution is determined by bacteria level. "Polluted" means that the enterococcus level is expected to be greater than 70 colony per 100 ml at the given location on the given date.')

 st.write('We use *a machine learning model* to provide these predictions. Air temperature and precipitation are important predictors for our model.')

 st.write("Here are the air temperature predictions at "+beach+" over next seven days, provided by Dark Sky API:")

 fig2 = go.Figure()

 #Add scatter trace for line
 fig2.add_trace(go.Scatter(
	x=df[df['County'] == county].Date.tolist(),
	y=df[df['County'] == county].AirTemp.tolist(),
   	 mode="lines",
    	name="temperature"
	))

 fig2.update_layout(
    xaxis_title="Date",
    yaxis_title="Temperature (in F)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
 )

 st.write(fig2)

 st.write("Here are the precipitation predictions:")

 fig3 = go.Figure()

 #Add scatter trace for line
 fig3.add_trace(go.Scatter(
	x=df[df['County'] == county].Date.tolist(),
	y=df[df['County'] == county].RainFall24h.tolist(),
   	 mode="lines",
    	name="temperature"
	))

 fig3.update_layout(
    xaxis_title="Date",
    yaxis_title="Precipitation (in mm)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
 )

 st.write(fig3)
