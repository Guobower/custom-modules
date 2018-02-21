# -*- coding: utf-8 -*-
from odoo import http

# class MyScaffolded(http.Controller):
#     @http.route('/valis_project/valis_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/valis_project/valis_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('valis_project.listing', {
#             'root': '/valis_project/valis_project',
#             'objects': http.request.env['valis_project.valis_project'].search([]),
#         })

#     @http.route('/valis_project/valis_project/objects/<model("valis_project.valis_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('valis_project.object', {
#             'object': obj
#         })