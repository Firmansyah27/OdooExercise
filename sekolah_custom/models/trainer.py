from odoo import models, fields, api, _

class Trainer(models.Model):
	_name = "trainer"
	_description = "Data Trainer"

	name = fields.Char(required=True)
	evaluasi_ids = fields.One2many("evaluasi", "trainer_id")