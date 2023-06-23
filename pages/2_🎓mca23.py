import streamlit as st
import os

def main():
    st.title("Image and Video Gallery")

    # Folder path containing the images and videos
    media_folder = "media"

    # Scan the folder for media files
    media_files = [file for file in os.listdir(media_folder)]

    # Display the media files in the gallery
    for media_file in media_files:
        file_path = os.path.join(media_folder, media_file)
        if media_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            st.image(file_path, caption=media_file, use_column_width=True)
        elif media_file.lower().endswith(('.mp4', '.mov', '.avi')):
            st.video(file_path, format='video/mp4')

if __name__ == '__main__':
    main()
