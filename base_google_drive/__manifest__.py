# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Base Google Drive™ integration',
    'version': '17.0.0.1',
    'category': 'Productivity',
    'author': 'SOTEC',
    'installable': True,
    'auto_install': False,
    'depends': ['base_setup', 'google_account'],
    
    'data': [
        
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        
    ],
    'description': """
Restablece las opciones base a las solapas de configuracion para instalar los modulos de google drive y sreadsheet
Integrate google document to Odoo record.
============================================

This module allows you to integrate google documents to any of your Odoo record quickly and easily using OAuth 2.0 for Installed Applications,
You can configure your google Authorization Code from Settings > Configuration > General Settings by clicking on "Generate Google Authorization Code"
""",
    
    'license': 'LGPL-3',
}
