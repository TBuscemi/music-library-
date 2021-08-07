SECRET_KEY = 'django-insecure-um+^7mmt!z@23vq!t-x*p&+#&eh5yr+q9dvj=xe_!xh1h4ptqu'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER':'root',
        'PASSWORD':'password',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'autocommit':True
        }
    }
}