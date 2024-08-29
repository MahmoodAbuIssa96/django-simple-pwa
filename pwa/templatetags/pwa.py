from django import template

from pwa.defaults import get_pwa_config

register = template.Library()


@register.inclusion_tag('pwa/metadata.html', takes_context=True)
def pwa_meta_data(context):
	PWA_CONFIG = get_pwa_config(context["request"])
	ICONS = PWA_CONFIG.get('icons', None)
	THEME_COLOR = PWA_CONFIG.get('theme_color', None)
	return {'ICONS':ICONS, 'THEME_COLOR':THEME_COLOR}


@register.inclusion_tag('pwa/meta_script.html')
def pwa_meta_script():
	return {}
