from odoo import models, fields


class academy(models.Model):
    _name = 'academy.teachers'
    _description = 'academy.academy'

    name = fields.Char()
    biography = fields.Html()
