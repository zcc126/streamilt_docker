FROM python:3.10
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /app
CMD [ "streamlit", "run", "app/app_streamlit.py"]