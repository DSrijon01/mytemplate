# -*- coding: utf-8 -*-


from odoo import models, fields
from odoo import api 





class problemsrijon(models.Model):
    _name = 'problem.srijon'
    _inherit = {'real.owner': 'related_owner'}
    _description = 'Real Estate Customer'

    trader = fields.Char(string='Name')
    customerprofile_image = fields.Image(string="Profile Image", max_width=100, max_height=100, verify_resolution=False)

    ##Many 2 many rekationship between customer and the properties 
    buy_property =  fields.Many2many('real.estate', string='Ordered Property')
    #many to many delegated relation with property owner 
    related_owner = fields.Many2many('real.owner', string='Related Owner')


    
    
    
    
     
