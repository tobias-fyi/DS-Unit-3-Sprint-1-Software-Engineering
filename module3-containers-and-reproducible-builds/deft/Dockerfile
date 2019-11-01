FROM debian
ENV PYTHONBUFFERED=1
RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl -y && \
pip3 install pandas numpy scikit-learn && \
pip3 install -i https://test.pypi.org/simple/ deft==1.0.3 && \
python3 -c "import deft;print('success')"
