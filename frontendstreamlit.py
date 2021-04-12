import streamlit as st 
import api 
from streamlit_player import st_player



def Front():
    st.title("Photo of the day NASA")
    #st.write(api.ImageDay('2020-09-28','2020-09-28'))
    date = st.date_input("Input your birthday")
    #name = st.text_input("Enter your name")
    result = api.ImageDay(date,date)
    if result[0]['media_type'] == 'image':
        st.image(str(result[0]['url']))
    else:
        st_player(result[0]['url'])

    st.title(result[0]['title'])
    st.subheader(result[0]['explanation'])
    
    


    #st.image(image)

    
    

if __name__ == '__main__':
    Front()