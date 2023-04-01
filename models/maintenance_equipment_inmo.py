# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api

logger = logging.getLogger(__name__)

class MaintenanceEquipmentInmo(models.Model):
    _inherit = 'maintenance.equipment'

    codigo_interno = fields.Char(string="Carácter", readonly=True, required=False, index=True)
    documentos_ids = fields.One2many(
        comodel_name="maintenance.equipment.document",
        inverse_name="id_equipo_mantenimiento",
        string="Documentos",
        required=False
    )
    id_seccion = fields.Many2one(
        comodel_name="maintenance.equipment.section",
        string="many2one",
        required=False,
        copy=True
    )
    numero_economico = fields.Char(string="Número económico", required=False, index=True, copy=True)
    url_carpeta_google_drive = fields.Char(string="URL carpeta documentos", required=False)
    url_documento_qr = fields.Char(string="URL Documento QR", required=False)
    fecha_compra = fields.Date(string="Fecha de compra", required=False)

    @api.model
    def create(self, values):
        # Add code here
        logger.info('********** Variables: {0}'.format(values))
        values['codigo_interno'] = self.env['ir.sequence'].next_by_code('secuencia.maintenance.equipment1')
        return super(MaintenanceEquipmentInmo, self).create(values)
