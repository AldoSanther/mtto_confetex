# -*- coding:utf8 -*-
{
    'name': 'Mantenimiento Confetex',
    'category': 'Manufacturing/Maintenance',
    'version': '15.0.1',
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
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}