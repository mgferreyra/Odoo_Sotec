# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    
    _inherit = "res.config.settings"

    
    module_google_drive = fields.Boolean('Google_Drive')
        #help="Habilita el uso de Google Drive")
    module_google_spreadsheet = fields.Boolean('Google_Spreadsheet')
        #help="Habilita el uso de Google Drive")

