# We're using Ubuntu 20.10
FROM python:3.8
#
# Clone repo and prepare working directory
#
RUN git clone -b Decha-Userbot https://github.com/ayay182/Decha-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ayay182/Decha-Userbot/Decha-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
