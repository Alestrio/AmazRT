dnf install -y epel-release screen python3 python3-devel gcc

useradd --password iutchalons amazrt

systemctl disable httpd
systemctl stop httpd

rm -rf /home/amazrt/AmazRT*

git clone https://github.com/Alestrio/AmazRT.git /home/amazrt/AmazRT
chown -R amazrt:amazrt /home/amazrt/AmazRT
python3 -m venv /home/amazrt/AmazRT/venv/
source /home/amazrt/AmazRT/venv/bin/activate
pip3 install --upgrade pip
pip3 install pysftp flask flask-login flask-wtf flask-qrcode psycopg2-binary sqlalchemy requests flask-httpauth flask-cors uwsgi
curl -o /home/amazrt/AmazRT/uwsgi.ini http://webrt.chalons.univ-reims.fr/~lebe0036/uwsgi.ini
curl -o /home/amazrt/AmazRT/launch.sh http://webrt.chalons.univ-reims.fr/~lebe0036/launch.sh
chmod +x /home/amazrt/AmazRT/launch.sh

. /home/amazrt/AmazRT/launch.sh