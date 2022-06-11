from odoo import models, fields, api

class hotel_management_module(models.Model):
    _name = "hotel_management_module.rooms"
    _rec_name = 'room_type'
    _description = "hotel_management_module.rooms"
    room_type = fields.Char(string="Room Type")
    floor_no = fields.Many2one('hotel_management_module.floors', 'Select Floor')

    attached_washroom = fields.Boolean(default=False)
    breakfast_incl = fields.Boolean(default=False)
    hot_bathtub = fields.Boolean(default=False)
    led_tv = fields.Boolean(default=False)
    free_wifi = fields.Boolean(default=False)
    room_description = fields.Text()

    picture0 = fields.Binary(string='Room Picture')
    picture1 = fields.Binary()
    picture2 = fields.Binary()

    booked = fields.Boolean(default=False)
    dimensions = fields.Char(string="Dimensions")
    booked_by = fields.Char()
    status = fields.Selection([
        ('booked', 'Booked'),
        ('available', 'Available'),
    ], string="Status", default="available")

    room_price = fields.Integer()

