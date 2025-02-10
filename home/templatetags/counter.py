from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)


@register.filter(name='filter_count')
def filter_count(queryset, condition):
    """Filtre le queryset et retourne le nombre d'éléments correspondant à la condition."""
    try:
        # Sépare la chaîne condition pour obtenir le champ et la valeur
        field, value = condition.split(':')
        
        # Convertit "True"/"False" en valeurs booléennes
        if value.lower() == 'true':
            value = True
        elif value.lower() == 'false':
            value = False
        
        # Applique le filtre au queryset
        return queryset.filter(**{field: value}).count()
    except Exception as e:
        # Retourne 0 en cas d'erreur (ou autre gestion des erreurs)
        return 0

