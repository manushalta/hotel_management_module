from odoo import models, fields, api


class adding_join(models.Model):
    _inherit = 'calendar.event'
    join_id = fields.Char()


class calender_event(models.Model):
    _inherit = 'hotel_management_module.users'
    _description = 'hotel_management_module.users'

    @api.model
    def create(self, values):

        if values.get('join_id', '1') == '1':
            values['join_id'] = self.env['ir.sequence'].next_by_code('hotel_management_module.users') or '1'

        categ_rec = self.env['calendar.event.type'].search([('name', '=', 'Hotel Booking')])
        if not categ_rec: self.env['calendar.event.type'].create({'name': 'Hotel Booking'})
        values['booking'] = True

        # updating rooms model
        changed_val = {
            'status': 'booked',
            'booked_by': values['name'],
            'booked': True
        }

        rec = values['room_id']
        record = self.env['hotel_management_module.rooms'].search([('id', '=', rec)])
        record.write(changed_val)

        # new contact
        new_contact = self.env['res.partner']
        new_contact_vals = {
            'name': values['name'],
            'mobile': values['phone'],
            'email': values['email'],
            'category_id': (11,)
        }
        new_contact.create(new_contact_vals)

        # new event
        new_event = self.env['calendar.event']
        new_event_vals = {
            'name': values['name'],
            'start': values['from_date'],
            'stop': values['to_date'],
            'join_id': values['join_id'],
            'categ_ids': (categ_rec.id,)
        }
        new_event.create(new_event_vals)

        record = super(calender_event, self).create(values)
        return record

    def unlink(self):
        if self.name:
            event_del = self.env['calendar.event'].search([('join_id', '=', self.join_id)])
            event_del.unlink()
            self.from_date = ''
            self.to_date = ''
            self.room_id.booked_by = ''
            self.room_id.write({'status': 'available'})
            self.room_id.booked = False
            self.booking = False

        return super(calender_event, self).unlink()


