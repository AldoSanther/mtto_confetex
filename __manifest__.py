# -*- coding:utf8 -*-
{
    'name': 'Mantenimiento Confetex',
    'category': 'Manufacturing/Maintenance',
    'version': '14.0.1',
    'author': 'José Miguel López Roano',
    'summary': 'Módulo para ordenes de mantenimiento y control de máquinas y herramientas en grupo Confetex',
    'description': '''Modulo para un control de peticiones de mantenimiento y control de máquinas y herramienta con 
                      impresión de código QR en Odoo14''',
    'website': 'https://www.confetex.com',
    'depends': [
        'base',
        'purchase',
        'hr',
        'maintenance',
        'base_automation',
        'mail',
    ],
    'data': [
        'data/secuencia.xml',
        'views/maintenance_equipment_menu_vw.xml',
        'views/maintenance_channel_gd_vw.xml',
        'views/maintenance_equipment_document_vw.xml',
        'views/maintenance_equipment_document_type_vw.xml',
        'views/maintenance_equipment_invw.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}