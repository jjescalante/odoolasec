# -*- coding: utf-8 -*-
from odoo import http

# class Lasec(http.Controller):
#     @http.route('/lasec/lasec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lasec/lasec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lasec.listing', {
#             'root': '/lasec/lasec',
#             'objects': http.request.env['lasec.lasec'].search([]),
#         })

#     @http.route('/lasec/lasec/objects/<model("lasec.lasec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lasec.object', {
#             'object': obj
#         })