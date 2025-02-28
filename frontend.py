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
        st.write("Indian culture has evolved over 5000 years, making it one of the world's oldest and most diverse civilizations. It has been shaped by various influences, including indigenous traditions, foreign invasions, religions, and socio-political changes. Below is an overview of its evolution:

---

### **1️⃣ Indus Valley Civilization (c. 3300–1300 BCE)**
- One of the world's earliest urban civilizations, flourishing in present-day India and Pakistan.
- Cities like Harappa and Mohenjo-Daro had advanced drainage, trade, and urban planning.
- Evidence of art, pottery, and possibly early religious practices related to nature worship.

---

### **2️⃣ Vedic Age (c. 1500–500 BCE)**
- The arrival of the Aryans led to the composition of the **Vedas**, the oldest Hindu scriptures.
- Development of **Sanskrit** as a scholarly and religious language.
- Emergence of the caste system and early Hindu rituals.
- Concept of **karma, dharma, and moksha** took shape.

---

### **3️⃣ Maurya & Gupta Empires (c. 321 BCE–550 CE)**
- **Mauryan Empire** (Chandragupta Maurya, Emperor Ashoka) spread Buddhism and centralized governance.
- **Gupta Empire** is known as the **Golden Age of India**, excelling in science, mathematics, literature (Kalidasa), and temple architecture.
- Hinduism, Buddhism, and Jainism flourished.

---

### **4️⃣ Medieval India & Islamic Influence (c. 700–1700 CE)**
- Arrival of **Islamic rulers** led to the Delhi Sultanate (1206) and Mughal Empire (1526).
- Architectural marvels like **Taj Mahal** and Indo-Islamic art flourished.
- Bhakti and Sufi movements promoted spiritual devotion and harmony.
- Persian and Urdu languages became part of Indian culture.

---

### **5️⃣ Colonial Era & Independence Struggle (c. 1757–1947)**
- **British rule** led to economic exploitation, but also introduced modern education and infrastructure.
- **Mahatma Gandhi's non-violent movement** led to India's independence in 1947.
- A mix of resistance and cultural exchanges influenced India’s legal, political, and linguistic landscapes.

---

### **6️⃣ Modern India (1947–Present)**
- Post-independence, India embraced **secularism, democracy, and rapid economic growth**.
- The IT boom, Bollywood, yoga, and global recognition of Indian traditions.
- Social movements for gender equality, caste upliftment, and environmental conservation.

---

### **Future of Indian Culture (Next 5000 Years?)**
- A blend of **tradition and technology** with AI, digital economy, and space exploration.
- Continued **global influence** in spirituality, cuisine, and philosophy.
- Efforts to preserve **heritage sites** while embracing modernization.

India’s culture has always adapted while keeping its core values intact—**diversity, spirituality, and resilience**. 🚀🇮🇳")
    elif menu == "About":
        st.header("About India")
        st.write("### **India: A Land of Diversity and Heritage** 🇮🇳  

India is a vast and diverse country with a rich history, vibrant culture, and a rapidly growing economy. It is the world's largest democracy and the second-most populous country.  

---

## **1️⃣ General Information**  
- **Official Name**: Republic of India  
- **Capital**: New Delhi  
- **Largest City**: Mumbai  
- **Official Languages**: Hindi & English (22 recognized languages in total)  
- **Currency**: Indian Rupee (₹)  
- **Population**: Over 1.4 billion (as of 2024)  
- **Government**: Federal parliamentary democratic republic  

---

## **2️⃣ Geography & Climate** 🌍  
- **Area**: 3.28 million sq. km (7th largest country in the world)  
- **Borders**: Pakistan, China, Nepal, Bhutan, Bangladesh, Myanmar  
- **Regions**: Himalayas (North), Gangetic Plains, Deccan Plateau, Coastal regions  
- **Climate**: Ranges from tropical in the south to alpine in the Himalayas  

---

## **3️⃣ History & Civilization** 🏛️  
- **Indus Valley Civilization (3300–1300 BCE)**: One of the world’s oldest civilizations  
- **Vedic Period**: Birth of Hinduism, Sanskrit, and early philosophy  
- **Maurya & Gupta Empires**: The Golden Age of India  
- **Medieval Period**: Mughal Empire, Islamic influences, and Indo-Persian culture  
- **British Rule (1858–1947)**: Colonization, economic exploitation, and social reforms  
- **Independence (1947)**: Led by Mahatma Gandhi and the freedom movement  

---

## **4️⃣ Culture & Traditions** 🎭  
- **Religions**: Hinduism, Islam, Christianity, Sikhism, Buddhism, Jainism  
- **Festivals**: Diwali, Holi, Eid, Christmas, Navratri, Pongal, Durga Puja  
- **Cuisine**: Known for its spices, diverse flavors—Biryani, Dosa, Paneer, Butter Chicken  
- **Art & Music**: Classical (Bharatanatyam, Kathak), Bollywood, folk dances  
- **Yoga & Spirituality**: Birthplace of Yoga, Ayurveda, and meditation  

---

## **5️⃣ Economy & Development** 💰  
- **5th largest economy in the world** (GDP-wise)  
- **IT & Software Hub**: Cities like Bengaluru lead in tech innovation  
- **Agriculture & Industry**: Major producer of wheat, rice, textiles, pharmaceuticals  
- **Space & Science**: ISRO’s Chandrayaan & Mangalyaan missions put India on the global space map  

---

## **6️⃣ Modern India & Future Prospects** 🚀  
- Growing infrastructure, metro cities, and smart technology adoption  
- Advancements in AI, space exploration, and clean energy  
- Leadership in global diplomacy & cultural influence  

India is a **blend of ancient traditions and modern aspirations**—a country that continues to evolve while maintaining its unique identity. 🇮🇳🔥  

Let me know if you need details on any specific topic! 🚀")
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
