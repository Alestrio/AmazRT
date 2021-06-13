#
#   AmazRT  -  Parcel Management System
#   First semester Technical Degree project
#     Copyright  (c) 2021 - 2022
#    - Meryem KAYA @MeryemKy
#    - Alexis LEBEL @Alestrio
#    - Malo LEGRAND @HoesMaaad
#

dnf install -y incron
echo "root" >> /etc/incron.allow
incrontab -e


/home/amazrt/parcels/ IN CREATE python3 /home/amazrt/Amazrt/util/check_received_parcel.py $@