# -*- encoding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    "name": "Complete timesheet from an iCal server",
    "version": "0.1",
    "author": "Tiny,Odoo Community Association (OCA)",
    "category": "Generic Modules/Human Resources",
    "website": "http://www.openerp.com",
    "description": "Import iCal events (for eg, Outlook) to auto-complete timesheets.",
    "depends": ["hr_timesheet"],
    "init_xml": [],
    "demo_xml": [],
    "update_xml": ["hr_timesheet_wizard.xml"],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
