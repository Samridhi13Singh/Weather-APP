import streamlit as st
import json
import requests

st.title("W☁️ther.app")
st.write("This application help to display weather info of any city.")


api_key='76686c1d03fd400780a100945251503'

city = st.text_input("Enter a place here👉 ")
if st.button("Display"):
    p = {
        'appid': api_key,
        'q': city

    }

    base_url = f'http://api.weatherapi.com/v1/current.json?key=76686c1d03fd400780a100945251503&q={city}&aqi=no'
    # print(base_url)

    response = requests.get(base_url, params=p)

    data = response.json()
    # st.write(data)
    var=data['current']['condition']['icon']
    var="https:"+var
    st.image(var,width= 100 )

    st.subheader(f'☁️The weather info of {city}☁️ :')
    st.subheader(f'⏲️The date and time is, {data['location']['localtime']}⏲️')
    st.write(f"🌡️Temp in celcius: {data['current']['temp_c']}C🌡️")
    st.write(f"🌡️Temp in farenheit: {data['current']['temp_f']}F🌡️")
    st.write(f"💧Humdity: {data['current']['humidity']}💧")
    st.write(f'The weather feels like {data["current"]["condition"]["text"]}')
    st.write(f'🍃The wind speed is {data["current"]["wind_kph"]} kph🍃')
    st.write(f'☁️The U.V index is {data["current"]["uv"]}☁️')

