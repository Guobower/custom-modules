# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ValisCheckbox(models.Model):
    _inherit = 'project.task'

    checkbox_list = fields.One2many('check.list', 'one_checklist', readonly=False,
                                    copy=True, states={'draft': [('readonly', False)]})


class CheckList(models.Model):
    _name = 'check.list'
    one_checklist = fields.Many2one('valis.checkbox', index=True, ondelete='cascade',
                                    required=True)
    check = fields.Boolean()
    check_text = fields.Char()
