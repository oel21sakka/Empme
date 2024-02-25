from django import template
register = template.Library()

@register.filter(name='is_company')
def is_company(user, company_id):
    return user.is_company(company_id)
