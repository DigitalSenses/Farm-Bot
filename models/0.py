from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'TestBot'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'f9b0f92b-cf1c-4335-b32a-3ed37556f472'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []

#Reload modules automaticaly when they change
response.generic_patterns = ['*']
from gluon.custom_import import track_changes
track_changes(True)
