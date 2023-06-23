import streamlit as st
def main():
    st.title("Maharaja Srirama Chandra Bhanja Deo University")

# Subheader
    st.markdown('<h1 style="color:orange;">   Welcome To Our University</h1>', unsafe_allow_html=True)
    image_url = "https://nou.nic.in/title112.png"
    st.image(image_url, caption=' ')
    

    # University image
    image = "Mscb.jpg"
    st.image(image, use_column_width=True)

    
    st.markdown('<h1 style="color:orange;">About MSCB University:</h1>', unsafe_allow_html=True)
    st.write("The Maharaja Sriram Chandra Bhanja Deo University (MSCB University), formerly North Orissa University (NOU) was established by the Government of Orissa, under the Section 32 of the Odisha University Act, 1989 (Act 5 of 1989), vide notification No. 880 dated 13th July 1998. It was carved out of the Utkal University and became operational since 1999 at Takatpur (98.84 acres) of Baripada in the Mayurbhanj District of Odisha as an affiliating university. The University is recognized by the University Grants Commission under Sections 2(f) and 12(B) of UGC Act,1956 with effect from 15th February 2000 and 21st June 2006, respectively. The territorial jurisdiction of the university extends over Mayurbhanj and Keonjhar districts of the northern part of Odisha, thickly populated with tribal communities. MSCBU's jurisdiction covers 110 colleges (Mayurbhanj-68 + Keonjhar-42) including 3 Autonomous Colleges, 2 Law Colleges, 1 Medical College, 3 Teachers' Education (B.Ed.) Colleges (including one specially for physically challenged) imparting education to a large number of students at the graduate and post-graduate levels. MSCBU is recognized by Bar Council of India, DEC, IGNOU, NCTE and included in the list of Association of Indian Universities and Association of Commonwealth Universities.     ")

    
    st.markdown('<h1 style="color:red;"></h1>', unsafe_allow_html=True)

# GIF
    st.markdown("### ")
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://nou.nic.in/depthome.gif" alt="GIF" width="600" height="600"/>
    </div>
    """,
    unsafe_allow_html=True
)   
    st.markdown('<h1 style="color:red;"></h1>', unsafe_allow_html=True)
    video_url = "https://www.youtube.com/watch?v=1azROQkmHmo&t=308s"
    st.video(video_url, start_time=0)

    st.markdown('<h1 style="color:orange;">MSCB Gallary</h1>', unsafe_allow_html=True)

# GIF
    st.markdown("### ")
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://nou.nic.in/photo.gif" alt="GIF" width="600" height="600"/>
    </div>
    """,
    unsafe_allow_html=True
)   

    st.markdown('<h1 style="color:orange;">MSCB Inter University Sports</h1>', unsafe_allow_html=True)

    video_url = "https://www.youtube.com/watch?v=zP36DKq8X8I"
    st.video(video_url, start_time=0)
if __name__ == "__main__":
    main()