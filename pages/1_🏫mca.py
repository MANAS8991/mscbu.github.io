import streamlit as st

def main():
    
    st.markdown('<h1 style="color:orange;">ज्ञातिभिर्वण्टयते नैव चोरेणापि न नीयते । दाने नैव क्षयं याति विद्यारत्नं महाधनम् ॥</h1>', unsafe_allow_html=True)

    # Department name design
    st.markdown(
        """
        <div style='text-align: center; padding: 20px; background-color: #f0f0f0;'>
            <h1 style='color: #333;'>କମ୍ପ୍ୟୁଟର ପ୍ରୟୋଗ ବିଭାଗକୁ ସ୍ୱାଗତ |</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("CA Department")
    image = "Dept0.jpg"
    st.image(image, use_column_width=True)

    st.subheader("2022 Get Togather")
    image = "Img1.jpg"
    st.image(image, use_column_width=True)

    st.subheader("Teachers Day")
    image = "Img2.jpg"
    st.image(image, use_column_width=True)

    st.subheader("2023 UPL Champions")
    image = "Img8.jpg"
    st.image(image, use_column_width=True)

    


    st.markdown('<h1 style="color:yellow;">Awards and Honours</h1>', unsafe_allow_html=True)

    st.markdown('<h1 style="color:red;">Announcements</h1>', unsafe_allow_html=True)

    # Add notice details and PDF download functionality
    notice_details = {
        "Title 1": {
            "Date": "Jun 1, 2023",
            "Description": "2nd Semester exam notice",
            "PDF": "https://drive.google.com/file/d/1WVeYBdd9aNUbuqlfNrMyqT3pROi7xNpW/view?usp=sharing"
        },
        "Title 2": {
            "Date": "Jul 10, 2023",
            "Description": "4th Semester result",
            "PDF": "https://drive.google.com/file/d/1WVeYBdd9aNUbuqlfNrMyqT3pROi7xNpW/view?usp=sharing"
        },
        # Add more notice details here
    }

    for title, details in notice_details.items():
        st.write(f"**{title}**")
        st.write(f"Date: {details['Date']}")
        st.write(f"Description: {details['Description']}")
        st.write(f"[Download PDF]({details['PDF']})")

    st.markdown('<h1 style="color:orange;">Seminar Talks</h1>', unsafe_allow_html=True)

    seminar_details = {
         "Sem10": {
            "Date": "Jun 3, 2023",
            "Title":"Scalable Clustering for Big Data and Efficient Algorithms for IoT and Smart City Applications",
            "Description": "Seminar talk on scalable clustering algorithms for big data analysis and efficient algorithms for IoT and smart city applications.",
            "PDF": "https://drive.google.com/file/d/1WVeYBdd9aNUbuqlfNrMyqT3pROi7xNpW/view?usp=sharing"
        },
        "Sem9": {
            "Date": "Jan 10, 2023",
            "Title":"Improving machine vision using insights from biological vision",
            "Description": "Seminar talk on leveraging insights from biological vision to enhance machine vision capabilities and performance.",
            "PDF": "https://drive.google.com/file/d/1WVeYBdd9aNUbuqlfNrMyqT3pROi7xNpW/view?usp=sharing"  
         },
    # Add more seminar talk details here
    }
    for title, details in seminar_details.items():
        st.write(f"**{title}**")
        st.write(f"Date: {details['Date']}")
        st.write(f"Title: {details['Title']}")
        st.write(f"Description: {details['Description']}")
        st.write(f"[Download PDF]({details['PDF']})")

    st.markdown('<h1 style="color:orange;">Our Students Achievements</h1>', unsafe_allow_html=True)
if __name__ == "__main__":
    main()
