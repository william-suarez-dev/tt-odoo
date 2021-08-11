# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    team_code = fields.Char(string="Code", size=128)
