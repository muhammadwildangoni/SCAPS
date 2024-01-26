import streamlit as st
import time
from PIL import Image
from time import sleep
from stqdm import stqdm
from streamlit_option_menu import option_menu
from main import predict
from io import BytesIO
from tqdm import tqdm


def about_page():
    st.title('Welcome to SCAPS 🤖 (Skin Cancer Prediction System)')

    # Teks
# Teks
    st.markdown("""
    <h2><strong> Let's All Take Care of Our Skin and Keep It Healthy Together 👩‍⚕️🌞 </strong></h2>
    <h4><strong>This application is designed to predict and detect potential skin cancer. </strong></h4>
    
    """ , unsafe_allow_html=True)

    img = Image.open('breast-cancer-awareness.png')
    st.image(img, width=650)


 # Teks tambahan
    st.markdown("""
    <p>This application has been specifically designed to predict and detect potential skin cancer, providing the best protection for your skin health.</p>
    <p>The application has been meticulously trained using 25,331 images from 8 main classes of skin cancer, including:</p>
    <ul>
        <li><strong>Melanoma</strong></li>
        <li><strong>Melanocytic nevus</strong></li>
        <li><strong>Basal cell carcinoma</strong></li>
        <li><strong>Actinic keratosis</strong></li>
        <li><strong>Benign keratosis</strong> (solar lentigo / seborrheic keratosis / lichen planus-like keratosis)</li>
        <li><strong>Dermatofibroma</strong></li>
        <li><strong>Vascular lesion</strong></li>
        <li><strong>Squamous cell carcinoma</strong></li>
    </ul>
    <p>It is important to note that this application integrates Convolutional Neural Network (CNN) technology with ShuffleNet V2 Model, ensuring an accuracy rate of almost 90%.</p>
    <p>The valuable data used to train this model is obtained from reliable sources, including:</p>
    <ul>
        <li><strong>BCN_20000 Dataset: </strong> Dataset from the Department of Dermatology, Hospital Clínic de Barcelona</li>
        <li><strong>HAM10000 Dataset: </strong> Dataset from ViDIR Group, Department of Dermatology, Medical University of Vienna</li>
        <li><strong>MSK Dataset: </strong> Dataset from various hospitals</li>
    </ul>
    <p>Save Your Skin, Achieve True Health! 💙🌞</p>
    """, unsafe_allow_html=True)


def image_prediction_page():
    st.title('Skin Cancer Prediction with Image')
    st.write('Please upload an image for skin cancer prediction.')

    uploaded_files = st.file_uploader("Upload one or multiple files", type=["jpg", "png"], accept_multiple_files=True)

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            progress_bar = st.progress(0)  # Membuat progress bar
            for percent_complete in tqdm(range(50), desc="Prediction Progress"):
                sleep(0.001)  # Menggunakan sleep sebagai contoh simulasi proses
                progress_bar.progress((percent_complete + 1) * 2)  # Mengupdate nilai progress

            # Melakukan prediksi untuk setiap file yang diunggah
            for uploaded_file in uploaded_files:
                prediction = predict(uploaded_file)

                # Menampilkan hasil prediksi
                st.success(f'Prediction for {uploaded_file.name}: {prediction}')

def webcam_prediction_page():
    st.title('Skin Cancer Prediction with Webcam Camera')
    st.write('Use the webcam camera to predict Skin Cancer')

    # Capture image from the camera
    img_file_buffer = st.camera_input("Capture Image")


    # Jika gambar telah diambil
    if img_file_buffer is not None:
        # Menampilkan spinner saat proses prediksi berlangsung
        with st.spinner('Predicting...'):
            # Menggunakan fungsi predict untuk melakukan prediksi
            prediction = predict(BytesIO(img_file_buffer.getvalue()))  # Gunakan fungsi predict dari main.py
            time.sleep(5)  # Hanya contoh simulasi proses prediksi selama 5 detik, ganti dengan fungsi predict yang sesungguhnya

        # Setelah proses selesai, tampilkan hasil prediksi
        st.success('Prediction process completed!')
        st.write(prediction)  # Menampilkan hasil prediksi


def main():
    options = ["About Application", "Prediction with Image", "Prediction with Camera"]
    selected_option = option_menu(None, options, default_index=0, icons=['house', 'cloud-upload', 'camera'], orientation="horizontal")
    

    if selected_option == "About Application":
        about_page()
    elif selected_option == "Prediction with Image":
        image_prediction_page()
    elif selected_option == "Prediction with Camera":
        webcam_prediction_page()

if __name__ == "__main__":
    main()
