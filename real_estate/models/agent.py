# -*- coding: utf-8 -*-


from odoo import models, fields
from odoo import api 
from odoo.exceptions import ValidationError
import re



class estateagent(models.Model):
    _name = 'estate.agent'
    _description = 'Real Estate Agents'

    agentname = fields.Char(string='Name')
    agentcompany = fields.Char(string='Company')
    agentaddress = fields.Char(string='Address')
    agentphone = fields.Char(string='Phone')
    agentemail_address = fields.Char(string='Email Address')
    
    ###many 2 many relationship with the realestate/properties 
    agent_id = fields.Many2many('real.estate', string = 'Maintaining')
    
    ###constrains for email address. 
    @api.constrains('agentemail_address')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.agentemail_address)
            ##valid_email = self.env['estate.agent'].search([('agentemail_address', '=', record.agentemail_address)])
            if valid_email == None:
                raise ValidationError('Please provide a valid E-mail')
            



   
    
    
    
    