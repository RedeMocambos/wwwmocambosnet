# Pacotes necessarios para ambiente completo com Apache+modwsgi e Django
sudo apt-get install libjpeg8-dev libmysqlclient-dev libldap2-dev libsasl2-dev libssl-dev python-virtualenv python2.6 python2.6-dev zip 
virtualenv -p /usr/bin/python2.6 --no-site-packages --distribute ~/VirtualEnvs/wwwmocambosnet
source ~/VirtualEnvs/wwwmocambosnet/bin/activate
pip install -r requirements.txt

# # Pacotes necessarios para django-filer
# sudo apt-get install libfreetype6-dev liblcms1-dev libjpeg8-dev
# pip install django-filer
