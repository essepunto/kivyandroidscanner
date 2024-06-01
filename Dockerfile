# Используем официальный образ Ubuntu
FROM ubuntu:20.04

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y \
    python3 python3-pip \
    zlib1g-dev libncurses5 libncurses5-dev libffi-dev libsqlite3-dev libssl-dev \
    openjdk-11-jdk wget unzip && \
    apt-get clean

# Устанавливаем Buildozer и python-for-android
RUN pip3 install --upgrade pip setuptools
RUN pip3 install cython buildozer python-for-android

# Устанавливаем Android SDK и NDK
RUN mkdir -p /opt/android-sdk/cmdline-tools
RUN cd /opt/android-sdk/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip -O commandlinetools.zip && \
    unzip commandlinetools.zip -d latest && \
    rm commandlinetools.zip

ENV ANDROID_HOME /opt/android-sdk
ENV PATH $ANDROID_HOME/cmdline-tools/latest/bin:$PATH
RUN yes | sdkmanager --licenses
RUN sdkmanager --update
RUN sdkmanager "platform-tools" "platforms;android-31" "build-tools;31.0.0" "ndk;25.1.8937393"

# Копируем исходный код приложения в контейнер
COPY . /app
WORKDIR /app

# Строим APK
CMD ["buildozer", "android", "debug"]
