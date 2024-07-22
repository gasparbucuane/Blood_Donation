from django.db.models import TextChoices

class ChoicesBloodType(TextChoices):
        Aplus = "A+"
        Aless = "A-"
        Bplus = "B+"
        Bless = "B-"
        ABplus = "AB"
        ABless = "AB-"
        Oplus = "O+"
        Oless = "O-"
    