from odoo import models, fields, api 

class PartnerEreditato(models.Model):
    
        _inherit = 'res.partner'
        active = fields.Boolean(default=True)
