# -*- coding: utf-8 -*-
# from odoo import http
#
#
# class HotelManagementModule(http.Controller):
#     @http.route('/index', auth='public')
#     def index(self, **kw):
#
#         return http.request.render('hotel_management_module.to_render')
#
#     @http.route('/hotel_management_module/hotel_management_module/objects', auth='public')
#     def list(self, **kw):
#         print("List From Controller!")
#         return http.request.render('hotel_management_module.listing', {
#             'root': '/hotel_management_module/hotel_management_module',
#             'objects': http.request.env['hotel_management_module.users'].search([]),
#         })
#
#     @http.route('/hotel_management_module/hotel_management_module/objects/<model("hotel_management_module.users"):obj>',
#                 auth='public')
#     def object(self, obj, **kw):
#         print("List From Controller!")
#         return http.request.render('hotel_management_module.object', {
#             'object': obj
#         })
