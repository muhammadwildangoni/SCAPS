import streamlit as st

def login():
    st.title("Halaman Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "user" and password == "password":  # Ganti ini dengan validasi sesuai kebutuhan Anda
            st.success("Login berhasil!")
            return True
        else:
            st.error("Username atau password salah")
            return False
