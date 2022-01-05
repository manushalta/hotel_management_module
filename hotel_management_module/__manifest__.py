
{
    'name': "Hotel Management -Entry",

    'summary': """ Hotel Management """,

    'description': """Hotel Management App for keep record of your Guests with a identity upload""",

    'author': "Socio",
    'website': "http://www.sociodev.com",


    'category': 'Tools',
    'version': '15.0',


    'depends': ['base'],
    'license': 'AGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'views/main_view.xml',
    ],

    'css': [
        'static/src/css/oe_avatar.css'
    ],
    'images': ['static/description/HotelManagementModule.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
