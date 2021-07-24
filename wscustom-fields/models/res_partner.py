# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class StockScrap(models.Model):
    _inherit = 'res.partner'

    partner_code = fields.Char(string="Code", size=128)
