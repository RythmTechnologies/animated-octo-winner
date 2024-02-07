from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'apps.buluntu':
        create_default_data()

def create_default_data():
    Miktar = apps.get_model('buluntu', 'Miktar')
    BuluntuTypes = apps.get_model('buluntu', 'BuluntuTypes')
    BuluntuAlani = apps.get_model('buluntu', 'BuluntuAlani')
    Renk = apps.get_model('buluntu', 'SetColour')

    if not Miktar.objects.exists():
        # Modelde veri yoksa, varsayılan veriyi oluştur
        Miktar.objects.create(data='Analiz Tüpü')
        Miktar.objects.create(data='Plastik Kutu')
        Miktar.objects.create(data='Korunmuş Ahşap Örneği')

    if not BuluntuTypes.objects.exists():
        BuluntuTypes.objects.create(buluntu="Taş")
        BuluntuTypes.objects.create(buluntu="Keramik")
        BuluntuTypes.objects.create(buluntu="Kemik")
        BuluntuTypes.objects.create(buluntu="Küçük Buluntu")

    if not BuluntuAlani.objects.exists():

        defaults = [
            BuluntuAlani(alan="Pulluk"),
            BuluntuAlani(alan="Çukur"),
            BuluntuAlani(alan="Yapı İçi"),
            BuluntuAlani(alan="Yapı Dışı"),
            BuluntuAlani(alan="Duvar"),
            BuluntuAlani(alan="Karışık"),
            BuluntuAlani(alan="Tahribat"),
            BuluntuAlani(alan="Dolgu"),
            BuluntuAlani(alan="Taban / Taban Üstü"),
            BuluntuAlani(alan="Ocak / Fırın")
        ]

        BuluntuAlani.objects.bulk_create(defaults)

    if not Renk.objects.exists():
        Renk.objects.create(colorName="Kırmızı", color="#FF0000")
