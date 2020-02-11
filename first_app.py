import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pickle
import sklearn
from sklearn.linear_model import LogisticRegression

st.title('Welcome to BacteriAlert')
st.write("This app provides bacterial beach water pollution predictions for 137 beaches in 26 costal Florida counties within seven days.")
#st.write( "Our predictions are based on Florida Health Department's historical beach water test data.")


counties = ['Bay','Brevard',
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
lists = [['BEACH DRIVE',
  'BECKRICH RD',
  'BID-A-WEE BEACH',
  'CARL GRAY PARK',
  'DELWOOD',
  'DUPONT BRIDGE',
  'LAGUNA BEACH',
  'PCB CITY PIER',
  'RICK SELTZER PARK'],
 ['COCOA BEACH PIER'],
 ['BIRCH STATE PARK',
  'COMMERCIAL BLVD PIER',
  'HALLANDALE BEACH BLVD',
  'HARRISON STREET',
  'MINNESOTA STREET',
  'POMPANO BEACH PIER',
  'NE 16TH ST POMPANO',
  'CUSTER ST BEACH',
  'DANIA BEACH',
  'SEBASTIAN STREET'],
 ['ENGLEWOOD MID BEACH',
  'ENGLEWOOD NORTH',
  'PORT CHARLOTTE BEACH EAST',
  'PORT CHARLOTTE BEACH WEST'],
 ['53RD ST - MIAMI BEACH',
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
 ['BAYOU CHICO',
  'BAYVIEW PARK PIER',
  'BIG LAGOON STATE PARK',
  'COUNTY PARK',
  'NAVY POINT',
  'QUIET WATER BEACH',
  'SANDERS BEACH'],
 ['ALLIGATOR POINT',
  'CARRABELLE BEACH',
  'SAINT GEORGE ISLAND 11TH ST E',
  'SAINT GEORGE ISLAND 11TH ST W',
  'SAINT GEORGE ISLAND FRANKLIN BLVD'],
 ['BEACON HILL BEACH', 'DIXIE BELLE BEACH', 'LOOKOUT BEACH', 'ST. JOE BEACH'],
 ['PINE ISLAND BEACH'],
 ['BAHIA BEACH',
  'BEN T. DAVIS NORTH',
  'BEN T. DAVIS SOUTH',
  'DAVIS ISLAND BEACH',
  'PICNIC ISLAND NORTH',
  'PICNIC ISLAND SOUTH',
  'SIMMONS PARK BEACH',
  'CYPRESS POINT PARK NORTH',
  'CYPRESS POINT PARK SOUTH'],
 ['HUMISTON BEACH OUTFLOW', 'SEXTON PLAZA OUTFLOW', 'SOUTH BEACH PARK'],
 ['BLIND PASS/TURNER BEACH',
  'BOWDITCH PARK',
  'CAPE CORAL YACHT CLUB',
  'LIGHTHOUSE BEACH',
  'LYNN HALL PARK',
  'SANIBEL CAUSEWAY'],
 ['BAYFRONT PARK NORTH', 'PALMA SOLA SOUTH'],
 ['ROOSEVELT BRIDGE', 'STUART CAUSEWAY'],
 ['BAHIA HONDA OCEANSIDE',
  'BAHIA HONDA SANDSPUR',
  'HARRY HARRIS COUNTY PARK',
  'HIGGS BEACH',
  'JOHN PENNEKAMP STATE PARK',
  'SMATHERS BEACH',
  'SOMBRERO BEACH',
  'FOUNDER'],
 ['EAST PASS',
  'GARNIERS PARK',
  'GULF ISLAND NATIONAL SEASHORE',
  'HENDERSON PARK BEACH',
  'JAMES LEE PARK',
  'LIZA JACKSON PARK',
  'MARLER PARK',
  'ROCKY BAYOU STATE PARK',
  'LINCOLN PARK',
  'POQUITO PARK'],
 ['DUBOIS PARK', 'LAKE WORTH BEACH', 'PHIL FOSTER PARK'],
 ['BRASHER PARK BEACH',
  'GULF HARBORS BEACH',
  'ROBERT J STRICKLAND BEACH',
  'ROBERT K. REES PARK BEACH'],
 ['COURTNEY CAMPBELL CAUSEWAY',
  'GANDY BOULEVARD',
  'HONEYMOON ISLAND BEACH',
  'INDIAN ROCKS BEACH',
  'MADEIRA BEACH',
  'NORTH SHORE BEACH',
  'PASS-A-GRILLE BEACH',
  'SAND KEY',
  'TREASURE ISLAND BEACH'],
 ['NAVARRE PARK HIGHWAY 98', 'SHORELINE PARK'],
 ['LIDO CASINO BEACH',
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
 ['VILANO BEACH'],
 ['JETTY PARK BEACH'],
 ['DUNLAWTON',
  'FLORIDA SHORES BLVD',
  'MAIN STREET',
  'SEABREEZE BLVD',
  'SILVER BEACH',
  'TORONITA',
  'INTERNATIONAL SPEEDWAY'],
 ["MASH'S ISLAND", 'SHELL POINT'],
 ['BLUE MOUNTAIN BEACH',
  'COUNTY PARK',
  'DUNE ALLEN BEACH',
  'EASTERN LAKE DUNE WALKOVER',
  'GRAYTON BEACH',
  'HOLLEY STREET BEACH',
  'INLET BEACH ACCESS']]

county = st.selectbox('Please select a county:', counties)

beaches = lists[counties.index(county)]

beach = st.selectbox('Now please select a location: ', beaches)

model = pickle.load(open('prediction_model', 'rb'))
df = pd.read_csv('Locations')
#abc


st.write("Here are our predictions for the chosen location, based on Florida Health Department's historical beach water test data:")
import datetime as dt
for x in range(7):
 t = pd.dt.today() + DT.timedelta(days=x)
 s = str(t.strftime('%m/%d/%Y'))
 st.write(s +": Clean")


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


