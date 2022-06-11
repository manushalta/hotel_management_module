
{
    'name': "Hotel Management -Entry",

    'summary': """ Hotel Management """,

    'description': """Hotel Management App for keep record of your Guests with identity upload""",

    'author': "Socio",
    'website': "http://www.sociodev.com",


    'category': 'Tools',
    'version': '16.1',


    'depends': ['base', 'calendar'],
    'license': 'AGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'views/main_view.xml',
        'views/join_id.xml',
        'views/rooms.xml',
        'views/floors.xml',
    ],
    'qweb': [
        'views/react_template.xml'
      ],
    'css': [
        'static/src/css/oe_avatar.css'
    ],
    'images': ['static/description/HotelManagementModule.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
