from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'armstrong.core.arm_profiles',
        'armstrong.core.arm_profiles.tests.arm_profiles_support',
    ),
    'ROOT_URLCONF': 'armstrong.core.arm_profiles.tests.arm_profile_support.urls',
}

full_name = "armstrong.core.arm_profiles"
main_app = 'arm_profiles'
tested_apps = (main_app, 'arm_profiles_support')
pip_install_first = True
