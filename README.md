# DjangoSampleProject
 Django Sample Project</br>
 employee app</br> </br> 
 Django:</br>
    pip install Django</br>
    django-admin --version</br>
    django-admin startproject DjangoEmployeeApp</br>
    python3 manage.py startapp Employee </br>
    python3 manage.py migrate</br>
    python3 manage.py createsuperuser</br>
    # after creating your model classes:</br>
    python3 manage.py makemigrations</br>
    python3 manage.py migrate</br>
    python3 manage.py runserver</br>
 
 Enable bootstrap in html:</br>
    SEARCH bootstrap 4 CDN, copy css and js</br>
    paste css under meta tags in head</br>
    paste js before closing body</br>

 Settings py:       

    # Application definition    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Employee' # we add our project here
    ]
    
    # we changed lang, timezone
    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/
    
    LANGUAGE_CODE = 'tr'
    TIME_ZONE = 'Europe/Istanbul'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ["templates"], # we add templates folder
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
