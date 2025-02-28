import streamlit as st
import os
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["thirupathi"]
users_collection = db["users"]

# User Authentication Functions
def signup(username, password):
    if users_collection.find_one({"username": username}):
        return "Username already exists."
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"username": username, "password": hashed_password})
    return "Signup successful!"

def login(username, password):
    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        return True
    return False

# Login / Signup UI
st.sidebar.title("Authentication")
choice = st.sidebar.radio("Login/Signup", ["Login", "Signup"])
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if choice == "Signup":
    if st.sidebar.button("Signup"):
        msg = signup(username, password)
        st.sidebar.success(msg)

if choice == "Login":
    if st.sidebar.button("Login"):
        if login(username, password):
            st.sidebar.success("Login successful!")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.sidebar.error("Invalid credentials.")

# Page configuration
st.set_page_config(page_title='My Streamlit Website', layout='wide')

# Sidebar Menu
if st.session_state.get("logged_in"):
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Navigation", ["Home", "About", "Contact", "Logout"])
    
    if menu == "Logout":
        st.session_state.clear()
        st.sidebar.success("Logged out successfully.")
        st.experimental_rerun()
else:
    st.warning("Please log in to access the menu.")

# Carousel using Streamlit
image_folder = "images"  # Change this to your local image folder path
image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(("png", "jpg", "jpeg"))]

# Display images as a slideshow
if image_files:
    img_index = st.session_state.get("img_index", 0)
    st.image(image_files[img_index], use_column_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous"):
            st.session_state.img_index = (img_index - 1) % len(image_files)
    with col2:
        if st.button("Next"):
            st.session_state.img_index = (img_index + 1) % len(image_files)
else:
    st.warning("No images found in the 'images' folder!")

# Main Content
if st.session_state.get("logged_in"):
    if menu == "Home":
        st.header("Indian culture in last 5000 years")
        st.write("This book is about the history and culture of India 5000 years ago. It aims at reaching out to the common man, from young students to grown-ups, who are not aware of the various discoveries brought forth through excavations since Independence. To illustrate the point, students from 1950s onwards have not been taught about the discoveries in the field of archaeology and associated sciences, which have disproved the theory of Aryan Invasion. Therefore, they still say that the Aryans invaded India. As a corollary, they are learning that the Aryans threw out the Dravidians who, according to the Britishers, inhabited the Indus valley till the Aryans came. They still talk about it being the ?Indus Valley Civilization? despite the fact the ?centre of gravity? of this civilization was the Sarasvati valley. The fault lies in our teaching system; reluctance to update the school books and books at university level which continue to ?parrot? the thinking of 1950s. The authorities that be need to accept the mass of professional papers, books and evidences of archaeology, anthropology, geology, archaeo-botany, etc. to set right our history which has been much maligned by the colonial rulers and their proteges that have ruled the Indian teaching systems. Section I of the book deals extensively with the richness of the Indus-Sarasvati Civilization: its origin, growth and maturity, its town-planning, trade and commerce, artistic creations, etc. Section II exposes the mind-set of the colonial rulers and their agenda to demean Indian civilization. Each one of their theories has been struck down, not in the least by Indian archaeologists but also by professionals all over the world. This Section demonstrates in clear terms that the Vedic people were neither ?invaders? nor ?immigrants? but indigenous and they themselves were the authors of the Indus-Sarasvati Civilization.")


    elif menu == "About":
        st.header("About India")
        st.write("Anatomically modern humans first arrived on the Indian subcontinent between 73,000 and 55,000 years ago.[1] The earliest known human remains in South Asia date to 30,000 years ago. Sedentariness began in South Asia around 7000 BCE; by 4500 BCE, settled life had spread,[2] and gradually evolved into the Indus Valley Civilisation, one of three early cradles of civilisation in the Old World,[3][4] which flourished between 2500 BCE and 1900 BCE in present-day Pakistan and north-western India. Early in the second millennium BCE, persistent drought caused the population of the Indus Valley to scatter from large urban centres to villages. Indo-Aryan tribes moved into the Punjab from Central Asia in several waves of migration. The Vedic Period of the Vedic people in northern India (1500–500 BCE) was marked by the composition of their extensive collections of hymns (Vedas). The social structure was loosely stratified via the varna system, incorporated into the highly evolved present-day Jāti system. The pastoral and nomadic Indo-Aryans spread from the Punjab into the Gangetic plain. Around 600 BCE, a new, interregional culture arose; then, small chieftaincies (janapadas) were consolidated into larger states (mahajanapadas). Second urbanization took place, which came with the rise of new ascetic movements and religious concepts,[5] including the rise of Jainism and Buddhism. The latter was synthesized with the preexisting religious cultures of the subcontinent, giving rise to Hinduism.Indian cultural influence (Greater India) Timeline of Indian history Chandragupta Maurya overthrew the Nanda Empire and established the first great empire in ancient India, the Maurya Empire. India's Mauryan king Ashoka is widely recognised for his historical acceptance of Buddhism and his attempts to spread nonviolence and peace across his empire. The Maurya Empire would collapse in 185 BCE, on the assassination of the then-emperor Brihadratha by his general Pushyamitra Shunga. Shunga would form the Shunga Empire in the north and north-east of the subcontinent, while the Greco-Bactrian Kingdom would claim the north-west and found the Indo-Greek Kingdom. Various parts of India were ruled by numerous dynasties, including the Gupta Empire, in the 4th to 6th centuries CE. This period, witnessing a Hindu religious and intellectual resurgence is known as the Classical or Golden Age of India. Aspects of Indian civilisation, administration, culture, and religion spread to much of Asia, which led to the establishment of Indianised kingdoms in the region, forming Greater India.[6][5] The most significant event between the 7th and 11th centuries was the Tripartite struggle centred on Kannauj. Southern India saw the rise of multiple imperial powers from the middle of the fifth century. The Chola dynasty conquered southern India in the 11th century. In the early medieval period, Indian mathematics, including Hindu numerals, influenced the development of mathematics and astronomy in the Arab world, including the creation of the Hindu-Arabic numeral system.[7] Islamic conquests made limited inroads into modern Afghanistan and Sindh as early as the 8th century,[8] ")
    elif menu == "Contact":
        st.header("Contact Us")
        st.write("Email: kandadithirupathi4@gmail.com")

# Footer
footer = """
    <style>
        .footer {position: fixed; bottom: 0; width: 100%; background: lightgray; text-align: center; padding: 10px;}
    </style>
    <div class="footer">© 2025 My Streamlit Website. All Rights Reserved.</div>
    """
st.markdown(footer, unsafe_allow_html=True)
