# -*- coding: utf-8 -*-
from odoo import http

# class Teacher(http.Controller):
#     @http.route('/teacher/teacher/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/teacher/teacher/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('teacher.listing', {
#             'root': '/teacher/teacher',
#             'objects': http.request.env['teacher.teacher'].search([]),
#         })

#     @http.route('/teacher/teacher/objects/<model("teacher.teacher"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('teacher.object', {
#             'object': obj
#         })