# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ValisProject(models.Model):
    _inherit = 'project.project'

    # Fields, methods for test
    hello_world = fields.Char(string='Hello World')

    # Regular Communications field
    regular_communication = fields.One2many('valis.communication', 'communication_list', 'Communication List', readonly=False,
                                    copy=True, states={'draft': [('readonly', False)]})

    # Main fields
    project_founder = fields.Many2one('res.users', string='Project Founder', default=lambda self: self.env.user,
                                      track_visibility="onchange")
    project_admin = fields.Many2one('res.users', string='Project Administrator', default=lambda self: self.env.user,
                                    track_visibility="onchange")
    project_type = fields.Selection([
        ('0', 'Investment model'),
        ('1', 'Service model'),
        ('2', 'Other'),
    ], default='0', index=True, string="Type of Project", track_visibility="onchange")
    project_priority = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Low'),
        ('2', 'Standard'),
        ('3', 'High'),
    ], string='Priority', index=True, track_visibility="onchange")
    project_relation = fields.Many2one('project.project', string='Project Relations', track_visibility="onchange")

    project_description = fields.Text(string='Project Description', track_visibility="onchange")

    project_objective = fields.Text(string='Project Objectives', track_visibility="onchange")
    project_strategic_objective = fields.Text(string='Project Strategic Objectives', track_visibility="onchange")
    project_functional_objective = fields.Text(string='Project Functional Objectives', track_visibility="onchange")
    project_result = fields.Text(string='Project Result', track_visibility="onchange")

    key_assumption = fields.Text(string="Key Assumptions", track_visibility="onchange")
    project_constraint = fields.Text(string="Projects Constraints", track_visibility="onchange")

    project_thirdparty_organization = fields.Many2one('res.users', string='Third-party Organizations',
                                                      default=lambda self: self.env.user,
                                                      track_visibility="onchange")
    project_external_name = fields.Many2one('res.users', string='Name of External Project Participant',
                                            default=lambda self: self.env.user,
                                            track_visibility="onchange")

    project_income = fields.Float(string='Income from the Project', track_visibility="onchange")
    project_consumption = fields.Float(string='Consumption on the Project', track_visibility="onchange")
    project_credit = fields.Float(string='The Need for Credit', track_visibility="onchange")
    project_profit = fields.Float(string='Profit', track_visibility="onchange")
    project_budget_comment = fields.Text(string="Comment", track_visibility="onchange")

    project_ppi = fields.Text(string='Project PPI', track_visibility="onchange")
    project_kpi = fields.Text(string='Project KPI', track_visibility="onchange")

    project_customer_sponsor = fields.Many2one('res.users', string='Project Sponsor',
                                               default=lambda self: self.env.user,
                                               track_visibility="onchange")
    project_customer_curator = fields.Many2one('res.users', string='Project Curator',
                                               default=lambda self: self.env.user,
                                               track_visibility="onchange")
    project_customer_executor = fields.Many2one('res.users', string='Customer Executor',
                                                default=lambda self: self.env.user,
                                                track_visibility="onchange")
    project_executor = fields.Many2one('res.users', string='Executor',
                                       default=lambda self: self.env.user,
                                       track_visibility="onchange")
    project_executor_sponsor = fields.Many2one('res.users', string='Project Sponsor',
                                               default=lambda self: self.env.user,
                                               track_visibility="onchange")
    project_executor_curator = fields.Many2one('res.users', string='Project Curator',
                                               default=lambda self: self.env.user,
                                               track_visibility="onchange")
    project_executor_manager = fields.Many2one('res.users', string='Project Manager',
                                               default=lambda self: self.env.user,
                                               track_visibility="onchange")
    project_external_executor = fields.Many2one('res.users', string='External Executor',
                                                default=lambda self: self.env.user,
                                                track_visibility="onchange")
    project_internal_executor = fields.Many2one('res.users', string='Internal Executor',
                                                default=lambda self: self.env.user,
                                                track_visibility="onchange")
    # Expert analysis recommendations fields
    project_recommendation_result = fields.Text(
        string="Conclusions/recommendations on the results of the project analysis", track_visibility="onchange")
    project_recommendation_manager = fields.Text(string="Recommendations for choosing a project manager",
                                                 track_visibility="onchange")

    # Statusbar fields
    state = fields.Selection([
        ('project_request', 'Project request'),
        ('expert_analysis', 'Expert analysis'),
        ('project_charter', 'Project charter'),
    ], default='project_request')

    # This function is triggered when the user clicks on the button 'Go to Project Request'
    @api.multi
    def project_request_progressbar(self):
        self.ensure_one()
        self.write({
            'state': 'project_request'
        })

    # This function is triggered when the user clicks on the button 'Go to Expert Analysis'
    @api.multi
    def expert_analysis_progressbar(self):
        self.ensure_one()
        self.write({
            'state': 'expert_analysis'
        })

    # This function is triggered when the user clicks on the button 'Go to Project Charter'
    @api.multi
    def project_charter_progressbar(self):
        self.ensure_one()
        self.write({
            'state': 'project_charter'
        })

class ValisCommunication(models.Model):
    _name = 'valis.communication'
    communication_list = fields.Many2one('valis.project', 'Regular Communications', index=True, ondelete='cascade',
                                         required=True)
    project_type_communication = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Periodic status meeting'),
        ('2', 'Weekly status meeting'),
        ('3', 'Quarterly status meeting'),
        ('4', 'Project completion report'),
    ], default='0', index=True, string="Type of Communications", track_visibility="onchange")
    project_periodicity = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Weekly'),
        ('2', 'Monthly'),
        ('3', 'Quarterly'),
        ('4', 'Upon reaching the gate'),
        ('5', 'As needed'),
    ], default='0', index=True, string="Periodicity", track_visibility="onchange")
    project_recipient = fields.Text(string='Recipient', track_visibility="onchange")

