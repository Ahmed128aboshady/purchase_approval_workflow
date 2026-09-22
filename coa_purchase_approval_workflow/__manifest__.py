# -*- coding: utf-8 -*-
{
    'name': "COA Purchase Approval Workflow | Enterprise Procurement Matrix",
    'version': '19.0.1.0.0',
    'category': 'Purchase',
    'summary': "Multi-level purchase order approval workflow with spending thresholds, SLA escalation, and audit trails",
    'description': """
COA Purchase Approval Workflow for Odoo 19 / 18 / 17
=====================================================
Enterprise procurement approval engine with dynamic signatory governance:
- Configurable Multi-Tier Approval Matrix based on PO amount, department, and category.
- SLA & Automatic Escalation: Define deadlines, overdue badges, and automated escalation cron.
- One-Click Email Approval: Direct tokenized approve/reject buttons inside email notifications.
- Bulk Approval Dashboard: Centralized portal to process and validate pending purchase orders.
- Out-of-Office & Delegation: Seamlessly delegate approval authority with start/end validity dates.
- Trusted Vendor Bypass: Expedite trusted supplier orders below pre-configured limits.
- Parallel & Sequential Logic: Support for AND (all sign) and OR (any sign) approval rules.
- HR Management Hierarchy: Auto-route approval requests based on employee reporting structure.
- Budget Control Warnings: Real-time budget consumption insights prior to PO authorization.
- Comprehensive Audit Trail: Full time-stamped log exportable to Excel and branded PDF reports.
    """,
    'author': "Community of accountants (COA-Egypt)",
    'website': "https://www.coa-egy.com",
    'support': "info@coa-egy.com",
    'license': 'OPL-1',
    'price': 49.00,
    'currency': 'USD',
    'depends': [
        'purchase',
        'mail',
        'hr',
    ],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'data/mail_template_data.xml',
        'data/cron_data.xml',
        'views/purchase_approval_matrix_diagram_views.xml',
        'views/purchase_approval_matrix_views.xml',
        'views/purchase_approval_history_views.xml',
        'views/purchase_approval_reject_wizard_views.xml',
        'views/purchase_order_views.xml',
        'views/purchase_approval_dashboard_views.xml',
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/purchase_approval_analytics_views.xml',
        'views/purchase_approval_policy_wizard_views.xml',
        'views/purchase_approval_audit_export_wizard_views.xml',
        'views/purchase_approval_audit_trail_report.xml',
        'views/menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/01_purchase_approval_matrix_list.png',
        'static/description/02_purchase_approval_tier_form.png',
        'static/description/03_purchase_approval_history.png'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
