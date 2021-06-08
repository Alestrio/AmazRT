#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import requests as requests
from flask_login import UserMixin, current_user
from requests.auth import HTTPBasicAuth

from application.data.entities.AbstractEntity import AbstractEntity
from application.exceptions.ApiException import ApiException
from application.util import config


class ApiService:
    __api_url = config.api_url + 'api/'

    def __init__(self):
        self.user = current_user

    def add(self, entity: AbstractEntity):
        addurl = self.__api_url + entity.root_url
        req = requests.post(addurl, data=entity.todict(), auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 201:
            return True
        else:
            raise ApiException(req.status_code)

    def delete(self, entity: AbstractEntity):
        delurl = self.__api_url + entity.root_url + entity.ide
        req = requests.delete(delurl, auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 201:
            return True
        else:
            raise ApiException(req.status_code)

    def edit(self, entity: AbstractEntity):
        editurl = self.__api_url + entity.root_url + entity.ide
        req = requests.put(editurl, data=entity.todict(), auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 201:
            return True
        else:
            raise ApiException(req.status_code)

    def getall(self, entity: AbstractEntity):
        geturl = self.__api_url + entity.root_url
        req = requests.put(geturl, auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 200:
            return req.json()
        else:
            raise ApiException(req.status_code)

    def getOneById(self, entity: AbstractEntity, ide: int):
        geturl = self.__api_url + entity.root_url + str(ide)
        req = requests.put(geturl, auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 200:
            return req.json()
        else:
            raise ApiException(req.status_code)

    def getOneSupplyAuth(self, entity: AbstractEntity, value, auth):
        geturl = self.__api_url + entity.root_url + value
        req = requests.put(geturl, auth=auth)
        if req.status_code == 200:
            return req.json()
        else:
            raise ApiException(req.status_code)
