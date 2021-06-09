#    AmazRT  -  Parcel Management System
#    First semester Technical Degree project
#      Copyright  (c) 2021 - 2022
#     - Meryem KAYA @MeryemKy
#     - Alexis LEBEL @Alestrio
#     - Malo LEGRAND @HoesMaaad
import json

import requests as requests
from flask_login import UserMixin, current_user
from requests.auth import HTTPBasicAuth

from application.data.entities.AbstractEntity import AbstractEntity
from application.exceptions.ApiException import ApiException
from application.util import config


class ApiService:
    __api_url = config.api_url
    user = None

    def add(self, entity: AbstractEntity):
        addurl = self.__api_url + entity.root_url.replace('/', '')
        if self.user:
            req = requests.post(addurl, json=entity.todict(), auth=HTTPBasicAuth(self.user.login, self.user.password))
        else:
            req = requests.post(addurl, json=entity.todict())

        if req.status_code == 201:
            return True

    def delete(self, entity: AbstractEntity):
        delurl = self.__api_url + entity.root_url + entity.ide
        req = requests.delete(delurl, auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 201:
            return True

    def edit(self, entity: AbstractEntity):
        editurl = self.__api_url + entity.root_url + entity.ide
        req = requests.put(editurl, data=entity.todict(), auth=HTTPBasicAuth(self.user.login, self.user.password))
        if req.status_code == 201:
            return True

    def getall(self, entity: AbstractEntity):
        geturl = self.__api_url + entity.root_url.replace('/', '')
        if self.user:
            req = requests.get(geturl, auth=HTTPBasicAuth(self.user.login, self.user.password))
        else:
            req = requests.get(geturl)

        if req.status_code == 200 or req.status_code == 201:
            return req.json()

    def getOne(self, entity: AbstractEntity, value):
        geturl = self.__api_url + entity.root_url + str(value)
        if self.user:
            req = requests.get(geturl, auth=HTTPBasicAuth(self.user.login, self.user.password))
        else:
            req = requests.get(geturl)

        if req.status_code == 200:
            return req.json()

    def getOneSupplyAuth(self, entity: AbstractEntity, value, auth):
        geturl = self.__api_url + entity.root_url + value
        req = requests.get(geturl, auth=auth)
        if req.status_code == 200 or req.status_code == 201:
            return req.json()
        else:
            print('nope', req.status_code)

    def checkIfLoginExists(self, login):
        geturl = self.__api_url + 'login/' + login
        req = requests.get(geturl)
        if req.status_code == 200 or req.status_code == 201:
            return req.json()
        else:
            print('nope', req.status_code)
