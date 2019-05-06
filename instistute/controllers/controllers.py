# -*- coding: utf-8 -*-
from odoo import http

# class Instistute(http.Controller):
#     @http.route('/instistute/instistute/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instistute/instistute/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('instistute.listing', {
#             'root': '/instistute/instistute',
#             'objects': http.request.env['instistute.instistute'].search([]),
#         })

#     @http.route('/instistute/instistute/objects/<model("instistute.instistute"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instistute.object', {
#             'object': obj
#         })