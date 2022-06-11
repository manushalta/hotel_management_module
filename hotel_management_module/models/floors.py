from odoo import models, fields, api


class floor(models.Model):
    _name = 'hotel_management_module.floors'
    _description = 'hotel_management_module.floors'
    _rec_name = 'floor_number'

    floor_number = fields.Integer(string="Floor Number")
    rooms_per_floor = fields.Integer(string="Rooms Per Floor")
    limit_per_floor = fields.Boolean(default=False)
