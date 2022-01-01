FROM ubuntu:18.04

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

ENV CHROME_VERSION "google-chrome-stable"

RUN apt-get update && apt-get install -y gnupg2

ENV CHROME_VERSION "google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list \
  && apt-get update && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable}
CMD /bin/bash

# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# RUN apt-get install libgconf2-4 libnss3-1d libxss1

# RUN apt install ./google-chrome-stable_current_amd64.deb
