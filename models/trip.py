from odoo import models, fields, api, _


class TripModel(models.Model):
    _name = 'trip'
    _description = 'Trip'
    _inherit = 'mail.thread'
    


    name = fields.Char(string="Viaggio")
    da = fields.Many2one("res.partner", string="From")
    a = fields.Many2one("res.partner", string="To")
    indirizzo_di_fatturazione = fields.Many2one("res.company", string="Indirizzo di fatturazione")
    reference_no = fields.Char(string='Riferimento Viaggio', required=True,
                               readonly=True, default=lambda self: ('N°'))
    

    @api.model
    def create(self, vals):
        res = super(TripModel, self).create(vals)
        if vals.get('reference_no', _('New')) == _('New'):
            res['reference_no'] = self.env['ir.sequence'].next_by_code(
                'trip') or _('')
        return res
        