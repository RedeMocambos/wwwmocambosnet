# Pacotes necessarios 
sudo apt-get install libjpeg8-dev libmysqlclient-dev libldap2-dev libsasl2-dev libssl-dev python-virtualenv python2.6 python2.6-dev zip
virtualenv -p /usr/bin/python2.6 --no-site-packages --distribute ~/VirtualEnvs/wwwmocambosnet_testando
source ~/VirtualEnvs/wwwmocambosnet_testando/bin/activate
pip install -r requirements.txt

# # Pacotes necessarios para django-filer
# sudo apt-get install libfreetype6-dev liblcms1-dev libjpeg8-dev
# pip install django-filer
