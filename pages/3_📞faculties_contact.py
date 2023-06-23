import streamlit as st
import pandas as pd
from PIL import Image
st.markdown('<h1 style="color:orange;">Faculties</h1>', unsafe_allow_html=True)
def main():
 st.title("Faculties")

    # Faculty data
    # Faculty data
faculties = [
    {
        "image": Image.open('Image 1.png'),
        "name": "1. Prof. Hima Bindu Maringanti, (M.Tech, Ph.D)",
        "position": "Professor and H.O.D",
        "department": "Computer Application",
        "email": "profhbnou2012@gmail.com",
        "Phone": "9861569765 (M)"
    },
    {
        "image": Image.open('Image 2.png'),
        "name": "2. Dr. Jibendu Kumar Mantri, (M.Sc., M.Phil, M.Tech, Ph.D.)",
        "position": "Associate Professor",
        "department": "Computer Application",
        "email": "jkmantri@gmail.com",
        "Phone": "9438084141 (M)"
    },
    {
        "image": Image.open('Image3.png'),
        "name": "3. Dr. Prasanta Kumar Swain, (M.Tech, Ph.D.)",
        "position": "Assistant Professor",
        "department": "Computer Application",
        "email": "prasantkiit@gmail.com",
        "Phone": "9861167683 (M)"
    },
    {
        "image": Image.open('Image 4.png'),
        "name": "4. Mr. Swarupananda Bissoyi, (M.C.A, Ph.D)",
        "position": "Assistant Professor",
        "department": "Computer Application",
        "email": "swarupananda@gmail.com",
        "Phone": "9040841527(M)"
    }
    # Add more faculties here
]


for faculty in faculties:
        st.image(faculty["image"], width=300)
        st.subheader(faculty["name"])
        st.write(f"Position: {faculty['position']}")
        st.write(f"Department: {faculty['department']}")
        st.write(f"Email: {faculty['email']}")
        st.write(f"Phone: {faculty['Phone']}")
        st.write("---")
st.title("Location")


data = {
        'latitude': [21.929966049982852],
        'longitude': [86.76586103524697]
    }
df = pd.DataFrame(data)
    
    # Display the map with your location
st.map(df, zoom=10)
    
    # Generate the URL link to your location
latitude = df['latitude'].values[0]
longitude = df['longitude'].values[0]
location_url = f"https://maps.google.com/?q={latitude},{longitude}"
    
    # Display the URL link
st.header("Click To Get Location")
st.markdown(f"[Click here to view location]({location_url})")
        
if __name__ == '__main__':
    main()
