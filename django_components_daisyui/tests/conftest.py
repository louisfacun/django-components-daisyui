import django
from django.conf import settings
import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def django_setup():
    if not settings.configured:
        settings.configure(
            INSTALLED_APPS=[
                'django_components',
                'django_components_daisyui',
            ],
            SECRET_KEY='test-key-for-pytest',
            USE_TZ=True,
            BASE_DIR=Path(__file__).resolve().parent.parent.parent,
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [Path(__file__).resolve().parent.parent / "components"],
                'APP_DIRS': True,
                'OPTIONS': {
                    'builtins': ['django_components.templatetags.component_tags'],
                },
            }],
            ROOT_URLCONF='django_components_daisyui.urls',
            EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
            COMPONENTS={},
        )
        django.setup()
