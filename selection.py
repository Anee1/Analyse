import streamlit as st
import pandas as pd 




#Porfeuille clients
Port = pd.read_csv(r'portfolio.csv', sep=';')

#ensemble des actions du marché
Titre_data = pd.read_csv(r'datap.csv', sep=',',parse_dates=True,index_col = 'date')
Titre_data = Titre_data.sort_index()
Titre_data.fillna(method='ffill', inplace=True)




#configuration
st.sidebar.title("Portefeuille client")
Portefeuille = st.sidebar.selectbox("Choisir un portefeuille", Port['NomClient'].unique())


#historique des titres du portefeuille 
Port_client = Port[Port['NomClient'] == Portefeuille ]
hist_port = Titre_data[Port_client['Titres'].values]
quantite_Titres = Port_client['Quantite'].values

st.write(Port_client)
st.write(quantite_Titres)
st.write(hist_port)
