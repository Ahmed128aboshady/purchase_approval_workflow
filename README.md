<div align="center">
  <img src="purchase_approval_workflow/static/description/coa_logo.jpg" width="120" height="120" alt="COA Egypt Logo" />
  <h1>COA Purchase Approval Workflow | Odoo Procurement Governance</h1>
  <p><strong>Multi-Tier Purchase Order Approval Workflow with Spending Limits, SLA Escalation, and Audit Trails</strong></p>

  <p>
    <a href="https://odoo.com"><img src="https://img.shields.io/badge/Odoo-19.0%20%7C%2018.0%20%7C%2017.0-063153.svg?style=for-the-badge&logo=odoo" alt="Odoo Versions" /></a>
    <a href="https://www.coa-egy.com"><img src="https://img.shields.io/badge/Author-COA--Egypt-E61B21.svg?style=for-the-badge" alt="COA Egypt" /></a>
    <img src="https://img.shields.io/badge/License-OPL--1-8C1D22.svg?style=for-the-badge" alt="License OPL-1" />
    <img src="https://img.shields.io/badge/Edition-Community%20%7C%20Enterprise-0F5586.svg?style=for-the-badge" alt="Edition" />
  </p>
</div>

---

## Overview

**COA Purchase Approval Workflow** is an enterprise-grade procurement governance app built for Odoo 19, 18, and 17. It empowers purchasing departments, financial controllers, and executive leadership to implement strict, multi-tiered spending limits and approval matrices for Purchase Orders (POs) and Requests for Quotation (RFQs).

With built-in SLA deadline tracking, automatic escalation, mobile one-click email approvals, out-of-office delegation, and comprehensive PDF/Excel audit reports, your procurement cycle remains fast, compliant, and completely transparent.

---

## Key Features

- **Multi-Tier Spending Thresholds:**
  - Configure unlimited approval levels per department or subsidiary (e.g. Lead &le; $10k, Director &le; $50k, CFO &gt; $50k).
- **SLA Deadlines & Automatic Escalation:**
  - Define response windows for each signatory. Unapproved orders automatically escalate to superiors via automated cron jobs.
- **One-Click Mobile Email Approval:**
  - Managers can sign off or refuse purchase orders directly from notification emails on mobile with encrypted single-use tokens.
- **Out-of-Office & Vacation Delegation:**
  - Temporarily transfer approval rights to designated colleagues during leaves with start and end date controls.
- **Trusted Vendor Fast-Track:**
  - Bypass multi-level approvals for certified vendors below configurable spending ceilings.
- **Real-Time Budget Control Warnings:**
  - Displays remaining budget allocations and overspending alerts directly on the purchase approval screen.
- **Comprehensive Audit Trail:**
  - Full time-stamped history of every submission, approval, refusal note, and delegation, exportable to Excel or branded PDF reports.
- **Bilingual Interface:** Fully localized in English (`en_US`) and Arabic (`ar_001`).

---

## Application Previews

### 1. Purchase Approval Matrices Overview
![Purchase Approval Matrices Overview](purchase_approval_workflow/static/description/01_purchase_approval_matrix_list.png)

### 2. Detailed Approval Tier Form & Spending Rules
![Detailed Approval Tier Form](purchase_approval_workflow/static/description/02_purchase_approval_tier_form.png)

### 3. Complete Purchase Order Approval History & Audit Trail
![Purchase Order Approval History](purchase_approval_workflow/static/description/03_purchase_approval_history.png)

---

## Installation & Configuration

1. Place the `purchase_approval_workflow` directory into your Odoo custom addons path.
2. Update the Apps list in Odoo developer mode.
3. Install **COA Purchase Approval Workflow**.
4. Navigate to **Purchase > Configuration > Approval Matrices** to define your organization's spending thresholds and approver tiers.

---

## Technical Support & Contact

- **Author:** Community of Accountants (COA-Egypt)
- **Website:** [https://www.coa-egy.com](https://www.coa-egy.com)
- **Email:** [info@coa-egy.com](mailto:info@coa-egy.com)
