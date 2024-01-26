import streamlit as st
from main import predict
from PIL import Image

# Profile Rumah Sakit
st.title('Profil Rumah Sakit')
st.write('Sambutan singkat mengenai profil rumah sakit, layanan yang disediakan, dll.')

# Bagian untuk melakukan prediksi Skin Cancer
st.title('Prediksi Skin Cancer')
st.write('Silakan unggah gambar untuk melakukan prediksi Skin Cancer')

if __name__ == "__main__":
    img_file = st.file_uploader("Upload gambar skin cancer disini", type=["png", "jpg"])
    
    if img_file is not None:
        image = Image.open(img_file)
        st.image(image, caption='Image berhasil terupload', use_column_width=True)


    if st.button("Predict"):
        prediction = predict(img_file)
        st.write(prediction)

if __name__ == "__main__":
    from login import login

    if login():
        main()