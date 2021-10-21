from odoo import models, fields, api

class restuser(models.Model):
    
    _inherit = 'res.users'
    _description = 'Real Estate Users'

    # instructor = fields.Boolean("Instructor", default=False)
    pp_ids = fields.Many2many('real.estate', string = "Proprties Owned")