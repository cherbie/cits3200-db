from .models import funding_opportunities

def get_all_research():
    researches = funding_opportunities.objects.raw('SELECT id, first_name FROM myapp_person')
    return researches