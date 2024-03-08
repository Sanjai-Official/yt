import streamlit as st
from pytube import YouTube



st.title("YouTube Video Information Retriever")

# Allow user input for the YouTube link
video_link = st.text_input("Enter YouTube Video Link (or drop it here):")


# Handle dropped links (if implemented in the future)
# dropped_link = st.empty()  # Placeholder for dropped link functionality

# Extract video ID if a link is provided
if video_link:
    yt = YouTube(video_link)  
    

    
    try:  
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            print(f"Downloading: {yt.title}")
            stream.download('downloads')
            print(f"Downloaded: {yt.title}")

    except:  
        print("Some Error!")  
    print('Task Completed!')  
    
  


    
  

