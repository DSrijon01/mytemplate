# -*- coding: utf-8 -*-


from operator import truediv

from odoo import models, fields
from odoo import api 
from odoo.exceptions import ValidationError
import re 

class realowner(models.Model):
    _name = 'real.owner'
    _description = 'Real Estate Owners'

    name = fields.Char(string='Name', Required = True)
    company = fields.Char(string='Company')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email_address = fields.Char(string='Email Address')
    profile_image = fields.Image(string="Upload", max_width=100, max_height=100, verify_resolution=False)
    owner_signature = fields.Char(string='Seller Signature')
    
    #many 2 one relationship with real esate / Properties. 
    owner_id = fields.Many2one('res.users', string = 'Responsible')
    
    #one 2 many relationship with real estate / Properties. 
    properties_name =  fields.One2many('real.estate','owner_info', string='Owned Property')
    
    ##Email constraints for Owners Emails Uniqueness. 
    @api.constrains('email_address')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email_address)
            
            if valid_email == None:
                raise ValidationError('Please provide a valid E-mail')

   
