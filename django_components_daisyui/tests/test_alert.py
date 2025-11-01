from django_components.testing import djc_test

@djc_test
def test_alert_component_usage(django_setup):
    from django.template import Template, Context

    template = Template('{% load component_tags %}{% component "alert" title="Test Title" %}{% endcomponent %}')
    result = template.render(Context())
    assert 'Test Title' in result
