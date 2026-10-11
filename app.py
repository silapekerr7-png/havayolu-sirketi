import streamlit as st
import pandas as pd
import pickle
 
st.title("Havayolu Yolcu Memnuniyeti Tahmini :airplane:")
model=pickle.load(open('havayolu.pkl','rb'))
kolonlar=pickle.load(open('kolonlar.pkl','rb'))
 
yas=st.number_input('Yaş',7,85,35)
mesafe=st.number_input('Uçuş mesafesi',50,5000,1000)
kalkis=st.number_input('Kalkış gecikmesi (dk)',0,500,0)
varis=st.number_input('Varış gecikmesi (dk)',0,500,0)
cinsiyet=st.radio('Cinsiyet',['Female','Male'])
musteri=st.radio('Müşteri tipi',['Loyal Customer','disloyal Customer'])
seyahat=st.radio('Seyahat türü',['Business travel','Personal Travel'])
sinif=st.selectbox('Sınıf',['Business','Eco','Eco Plus'])
 
puanlar=['Inflight wifi service','Departure/Arrival time convenient','Ease of Online booking','Gate location','Food and drink','Online boarding','Seat comfort','Inflight entertainment','On-board service','Leg room service','Baggage handling','Checkin service','Cleanliness']
veri={'Age':yas,'Flight Distance':mesafe,'Departure Delay in Minutes':kalkis,'Arrival Delay in Minutes':float(varis),'Gender':cinsiyet,'Customer Type':musteri,'Type of Travel':seyahat,'Class':sinif}
for p in puanlar:
    veri[p]=st.number_input(p+' (0-5)',0,5,3)
 
if st.button('Tahmin et'):
    x=pd.get_dummies(pd.DataFrame([veri]))
    x=x.reindex(columns=kolonlar,fill_value=0)
    tahmin=model.predict_proba(x)[0][1]
    st.success(f'Yolcunun memnun olma olasılığı: %{tahmin*100:.1f}')