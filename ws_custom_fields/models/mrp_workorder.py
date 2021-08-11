# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    operator_id = fields.Many2one('hr.employee', 'Operator')
    
