# -*- coding: utf-8 -*-from custom_addons.real_estate.models.inheritance import restuser

from odoo import models, fields
from odoo import api 
from odoo.exceptions import ValidationError

class realestate(models.Model):
    _name = 'real.estate'
    _description = 'real_estate.real_estate'
    

    ##Sql Constraints To validate the Price Fileds Input. 
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'The expected price must be strictly positive'),
        ('check_surge_price', 'CHECK(surgeprice >= 0)', 'The selling price must be positive')
        
    ]



    partner_id = fields.Many2one('res.partner',string="Partner")


    title = fields.Char(string ='Title')
    description = fields.Char(string='Description')
    seller_signature = fields.Char(string='Seller Signature')
    pp_address = fields.Char(string="Address")
    expected_price = fields.Integer(string='Expected Price')
    avaiable_from = fields.Date(string='Available From')
    property_image = fields.Image(string="Upload", max_width=100, max_height=100, verify_resolution=False)
    status = fields.Selection([
        ('available','Available'),
        ('unavailable', 'Unavailable')
    ])
    
    ## for computed field. 
    surgeprice = fields.Float(compute = "_compute_total", inverse ="_inverse_total", string = 'Future Price')
    

    ##many 2 one view with owner
    property_id = fields.Many2one('res.partner',string='Owned By')
    owner_info =  fields.Many2one('real.owner',string='Owning')

    newid = fields.Many2many('res.users', string="Working")
    
    ##Computed Field Logic. 
    @api.depends('expected_price')
    def _compute_total(self):
        for record in self:
            record.surgeprice = record.expected_price * 5 

    def _inverse_total(self):
        for record in self:
            record.surgeprice = record.expected_price - (record.expected_price * (10/100))

    ##For Name Constraints of the property.      
    @api.constrains('title')
    def check_title(self):
        for rec in self:
            error = self.env['real.estate'].search([('title', '=', rec.title)])
            if (error == rec.title):
                raise ValidationError(('Same Name'))
    

    


 