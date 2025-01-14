{
	'name': 'Agencia_adrv',
	'version': '1.0',
	'category': 'Herramientas',
	'summary': 'Modulo creado para agencias inmobiliares',
	'description': 'Modulo para gestionar agencias inmobiliarias',
	'author': 'Adrian De la Rosa Vicente',
	'website': 'http://iespacomolla.es',
	'depends': [
		'base',
		'sale',
	],
	'data': [
		'views/views_adrian.xml',
		'security/ir.model.access.csv'
	],
	'installable': True,	#Indica que el modulo es instalable
	'application': True,	#Indica si es una aplicacion completa de Odoo
	'auto_install': False,	# Indica si el modulo se instala automaticamente
}
