#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"))
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2


class Invoice:
    def __init__(self):
        self.issuer = {}
        self.client = {}
        self.lines = []
        self.date = None


class IssuerHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        params = {"origin": "issuer"}

        self.response.write(jinja.render_template("form.html", **params))

    def post(self):

        try:
             invoice.issuer['lblCif'] = str(self.request.get("lblCif"))
             invoice.issuer['lblName'] = str(self.request.get("lblName"))
             invoice.issuer['lblAddress'] = str(self.request.get("lblAddress"))
             invoice.issuer['lblCity'] = str(self.request.get("lblCity"))
             invoice.issuer['lblProvince'] = str(self.request.get("lblProvince"))
             invoice.issuer['lblPostalCode'] = str(self.request.get("lblPostalCode"))
             invoice.issuer['lblCountry'] = str(self.request.get("lblCountry"))
             invoice.issuer['lblContact'] = str(self.request.get("lblContact"))
             invoice.issuer['lblEmail'] = str(self.request.get("lblEmail"))
             invoice.issuer['lblPhone'] = str(self.request.get("lblPhone"))

             return self.redirect('/client')

        except(TypeError, ValueError):
            self.response.write("<html><body><p>Valores introducidos inválidos</p></body></html>")


class ClientHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        params = {"origin": "client"}

        self.response.write(jinja.render_template("form.html", **params))

    def post(self):

        try:
             invoice.client['lblCif'] = str(self.request.get("lblCif"))
             invoice.client['lblName'] = str(self.request.get("lblName"))
             invoice.client['lblAddress'] = str(self.request.get("lblAddress"))
             invoice.client['lblCity'] = str(self.request.get("lblCity"))
             invoice.client['lblProvince'] = str(self.request.get("lblProvince"))
             invoice.client['lblPostalCode'] = str(self.request.get("lblPostalCode"))
             invoice.client['lblCountry'] = str(self.request.get("lblCountry"))
             invoice.client['lblContact'] = str(self.request.get("lblContact"))
             invoice.client['lblEmail'] = str(self.request.get("lblEmail"))
             invoice.client['lblPhone'] = str(self.request.get("lblPhone"))

             print(invoice.issuer)
             print(invoice.client)

             return self.redirect('/invoice')

        except(TypeError, ValueError):
            self.response.write("<html><body><p>Valores introducidos inválidos</p></body></html>")


class InvoiceHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        params = {"invoice": invoice}

        self.response.write(jinja.render_template("invoice.html", **params))


    def post(self):

        try:
            line = {
                "lblCapacity": str(self.request.get("lblCapacity")),
                "lblPriceUnit": str(self.request.get("lblPriceUnit")),
                "lblQuantity": str(self.request.get("lblQuantity")),
                "lblGross": str(self.request.get("lblGross")),
                "lblIva": str(self.request.get("lblIva")),
                "lblTotal": str(self.request.get("lblTotal"))
            }
            invoice.lines.append(line)

            return self.redirect('/invoice')
        except (TypeError, ValueError) as e:
            print("ERROR:", e)
            self.response.write("<html><body><p>Valores introducidos inválidos</p></body></html>")



invoice = Invoice()

app = webapp2.WSGIApplication([
    ('/issuer', IssuerHandler),
    ('/client', ClientHandler),
    ('/invoice', InvoiceHandler)
], debug=True)
