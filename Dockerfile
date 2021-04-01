FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /aplicacion
COPY requirements.txt /aplicacion/
RUN apt-get update
RUN apt-get -y install locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8     
RUN apt-get install apache2 -y
RUN apt-get install apache2-dev -y
RUN apt-get install -y libgl1-mesa-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN usermod -a -G video root
COPY . .