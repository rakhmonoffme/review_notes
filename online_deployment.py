#Kutubxonalar
import streamlit as st
import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score
#Model load
model=load('model.joblib')

try:
    x_test=pd.read_csv('s_test.csv')
    y_test=pd.read_csv('y_test.csv')
    y_test=y_test.squeeze()# df --> series
    show_accuracy=True
except:
    show_accuracy=False

#Page, UI header
st.set_page_config(page_title='Yomgirni bashorat qilish uchun app',layout='centered')
st.title('Ob xavo: Yomgir yoki yoq')
st.markdown('Bugungi ob xavo malumotlarini kiriting va yomgirni bizning app yordamida bashorat qiling!')

# User inputlari uchun

pressure = st.number_input('Xavo bosimi',min_value=800.0,max_value=10000000.0,value=900.0)
maxtemp = st.number_input('Maksimal harorat',min_value=-50.0,max_value=60.0,value=25.0)
temparature = st.number_input('O\'rtacha harorat',min_value=-50.0,max_value=60.0,value=25.0)
mintemp = st.number_input('Minimal harorat',min_value=-50.0,max_value=60.0,value=25.0)
dewpoint = st.number_input('Dewpoint',min_value=-50.0,max_value=60.0,value=25.0)
humidity=st.number_input('Namlik',min_value=0.0,max_value=100.0,value=60.0)
cloud = st.number_input('Bulut',min_value=0.0,max_value=100.0,value=25.0)
sunshine = st.number_input('Quyosh nuri',min_value=0.0,max_value=24.0,value=12.0)
winddirection = st.number_input('Shamol yo\'nalishi',min_value=0.0,max_value=360.0,value=180.0)
windspeed = st.number_input('Shamol tezligi',min_value=0.0,max_value=100.0,value=10.0)


#Prediction logic
if st.button('Yomgirni bashorat qiling!'):
    input_date=pd.DataFrame([{
        'pressure':pressure,
        'maxtemp':maxtemp,
        'temparature':temparature,
        'mintemp':mintemp,
        'dewpoint':dewpoint,
        'humidity':humidity,
        'cloud':cloud,
        'sunshine':sunshine,
        'winddirection':winddirection,
        'windspeed':windspeed,
    }])
    
    
    #Predict qiling
    prediction=model.predict(input_date)[0]
    if prediction==1:
        st.success('Yomgir yogadi')
    else:
        st.info('Yomgir yoq')
        #Accuract uchun if 
    if show_accuracy:
        y_pred=model.predict(x_test)
        acc=accuracy_score(y_test,y_pred)
        st.metric('Yomgir yogish aniqligi:',f"{acc}")
    else:
        st.warning('Xatolik bor! Kodni qaytadan tekshirib koring')