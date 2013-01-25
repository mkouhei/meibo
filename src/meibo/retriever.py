# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from httplib2 import Http
from urllib import urlencode
from lxml import etree
import pyquery
import json
import os

SITE_PASSWORD = "password"
DOMAIN = "example.org"
URI_ADMIN = 'http://ml.example.org/cgi-bin/mailman/admin/'
LIST_JSON_PATH = '/tmp/list.json'


class MailAddressList(object):

    def __init__(self):
        self.h = Http()

    def retrieve_list_of_ml(self, uri):
        """retrieve list of ML uri

        Arguments:

            uri: uri of mailman admin view
                 ex. http://<ml.example.org>/cgi-bin/mailman/admin
        """
        pq = pyquery.PyQuery(uri, encoding='utf-8')
        ml_list = [(uri + i.values()[0].split('../admin/')[1],
                    i.values()[0].split('../admin/')[1])
                   for i in pq('strong').parent('a').parent().find('a')]
        return ml_list

    def login(self, uri, password):
        """login to admin view

        Arguments:

            uri:      uri of each mailing list login form
                      ex. http://<ml.example.org>/cgi-bin/mailman/admin/<hoge>
            password: mailman site administrator's password
        """
        login_data = dict(adminpw=password)
        res, content = self.h.request(uri, 'POST', urlencode(login_data))
        headers = {'cookie': res.get('set-cookie')}
        return headers

    def retrieve_list_of_mail_address(self, uri, headers):
        """retrieve mail list

        Arguments:

            uri:     uri of each mailing list management members view
            headers: headers as set cookies when login
        """
        res, content = self.h.request(uri, 'GET', headers=headers)
        content_u = unicode(content, 'euc-jp').encode('utf-8')
        dom = pyquery.PyQuery(
            etree.fromstring(content_u,
                             parser=etree.XMLParser(recover=True)))
        mail_address_list = [i.text for i in dom.find('td > a') if i.text]
        return mail_address_list


def main():
    ml = MailAddressList()
    ml_list = ml.retrieve_list_of_ml(URI_ADMIN)
    all_list = []
    for uri, ml_name in ml_list:
        headers = ml.login(uri, SITE_PASSWORD)
        mail_address_list = ml.retrieve_list_of_mail_address(
            uri + '/members', headers)
        all_list.append({
                ml_name: "%s@%s" % (ml_name, DOMAIN),
                "members": mail_address_list
                })
    list_json = json.JSONEncoder().encode(all_list)

    with open(os.path.abspath(LIST_JSON_PATH), 'w') as f:
        f.write(list_json)

    return list_json


if __name__ == '__main__':
    main()
