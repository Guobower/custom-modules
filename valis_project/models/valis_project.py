# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ValisProject(models.Model):
    _inherit = 'project.project'

    # Fields, methods for test
    hello_world = fields.Char(string='Hello World')

    # Risks smart button
    @api.multi
    def _project_risk_button(self):
        pass

    def attachment_tree_view(self):
        self.ensure_one()
        domain = [
            '|',
            '&', ('res_model', '=', 'project.project'), ('res_id', 'in', self.ids),
            '&', ('res_model', '=', 'project.task'), ('res_id', 'in', self.task_ids.ids)]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                            Documents are attached to the tasks and issues of your project.</p><p>
                            Send messages or log internal notes with attachments to link
                            documents to your project.
                        </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

    # Risks field
    # risk_all = fields.Many2many('valis.risk.internal', 'valis.risk', 'risk_list' 'risk_list_internal', 'Risk All', readonly=False, copy=True)
    risk_count = fields.Integer(compute='_project_risk_button', string="Risks")
    risk_internal = fields.One2many('valis.risk.internal', 'risk_list_internal', 'Risk List Internal', readonly=False,
                                    copy=True, states={'draft': [('readonly', False)]})
    risk_external = fields.One2many('valis.risk.external', 'risk_list_external', 'Risk List External', readonly=False,
                                    copy=True, states={'draft': [('readonly', False)]})

    # Regular Communications field
    regular_communication = fields.One2many('valis.communication', 'communication_list', 'Communication List',
                                            readonly=False,
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


class ValisRiskInternal(models.Model):
    _name = 'valis.risk.internal'
    risk_list_internal = fields.Many2one('valis.project', 'Internal Risk', index=True, ondelete='cascade',
                                         required=True)
    project_risk_area = fields.Text(string="Name or Area of Risk", track_visibility="onchange")
    project_risk_probability = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Hardly ever'),
        ('2', 'Rarely'),
        ('3', 'Occasionally'),
        ('4', 'Often'),
        ('5', 'Very often'),
    ], default='0', index=True, string="Type of Communications", track_visibility="onchange")
    project_risk_degree = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Insignificant'),
        ('2', 'Lower'),
        ('3', 'Average'),
        ('4', 'Significant'),
        ('5', 'Catastrophic'),
    ], default='0', index=True, string="Type of Communications", track_visibility="onchange")
    project_risk_cause = fields.Text(string="Cause of Risk", track_visibility="onchange")
    project_risk_strategy = fields.Text(string="Risk Response Strategy", track_visibility="onchange")
    project_risk_consequence = fields.Text(string='Consequences of Risk', track_visibility="onchange")
    project_risk_recommendation = fields.Text(string='Recommendations for Actions to avoid/minimize risks',
                                              track_visibility="onchange")


class ValisRiskExternal(models.Model):
    _name = 'valis.risk.external'
    risk_list_external = fields.Many2one('valis.project', 'External Risk', index=True, ondelete='cascade',
                                         required=True)
    project_risk_area = fields.Text(string="Name or Area of Risk", track_visibility="onchange")
    project_risk_probability = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Hardly ever'),
        ('2', 'Rarely'),
        ('3', 'Occasionally'),
        ('4', 'Often'),
        ('5', 'Very often'),
    ], default='0', index=True, string="Type of Communications", track_visibility="onchange")
    project_risk_degree = fields.Selection([
        ('0', 'Select an item'),
        ('1', 'Insignificant'),
        ('2', 'Lower'),
        ('3', 'Average'),
        ('4', 'Significant'),
        ('5', 'Catastrophic'),
    ], default='0', index=True, string="Type of Communications", track_visibility="onchange")
    project_risk_cause = fields.Text(string="Cause of Risk", track_visibility="onchange")
    project_risk_strategy = fields.Text(string="Risk Response Strategy", track_visibility="onchange")
    project_risk_consequence = fields.Text(string='Consequences of Risk', track_visibility="onchange")
    project_risk_recommendation = fields.Text(string='Recommendations for Actions to avoid/minimize risks',
                                              track_visibility="onchange")
