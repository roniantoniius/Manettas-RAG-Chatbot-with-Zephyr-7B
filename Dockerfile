# Gunakan image python sebagai base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh isi project ke dalam container
COPY . .

# Expose port yang akan digunakan oleh Streamlit
EXPOSE 8501

# Jalankan aplikasi Streamlit
CMD ["streamlit", "run", "streamlit.py"]
