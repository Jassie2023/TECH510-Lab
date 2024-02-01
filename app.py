import streamlit as st

# Page Title
st.title("Jassie's UX Design Portfolio")

image_url = 'https://raw.githubusercontent.com/Jassie2023/TECH510Lab1/819e91b99c19931496e32a829c79ee4e5cea9ce5/test.jpg'

st.image(image_url, caption='Jassie\'s UX Design Portfolio', use_column_width=True)


# About Section
st.header("About Me")
st.write("I am a passionate UX designer with a strong background in creating user-centric experiences. "
         "I enjoy solving complex design challenges and delivering intuitive solutions to users.")

# Education Section
st.header("Education")
st.subheader("Master of User Experience Design - University of Washington")
st.write("Graduated in 2025")

st.subheader("Bachelor of Architecture")
st.write("Graduated in 221")

# Work Experience Section
st.header("Work Experience")

st.subheader("UX Designer - Midea Group")
st.write("Responsible for leading the design team and delivering innovative UX solutions for our products. "
         "Worked on various projects, including mobile apps and web applications.")


# Hobbies and Interests Section
st.header("Hobbies and Interests")
st.write("In my free time, I enjoy hiking, photography, and reading about design trends and human psychology.")

# Interesting Projects Section
st.header("Interesting Projects")

st.subheader("Project 1: Mobile App Redesign")
st.write("Redesigned a popular mobile app, resulting in a 30% increase in user engagement and a 20% "
         "boost in user retention.")

st.subheader("Project 2: E-commerce Website Redesign")
st.write("Led the redesign of a major e-commerce website, focusing on improving the user journey and increasing "
         "conversion rates.")

# Add buttons for LinkedIn and GitHub
linkedin_url = "https://www.linkedin.com/in/yinghe-jassie/"
github_url = "https://github.com/Jassie2023"

if st.button("LinkedIn"):
    st.write(f"Check out my LinkedIn profile: [{linkedin_url}]({linkedin_url})")

if st.button("GitHub"):
    st.write(f"Explore my GitHub projects: [{github_url}]({github_url})")
