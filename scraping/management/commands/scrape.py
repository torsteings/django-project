from django.core.management.base import BaseCommand

from scraping.models import Main
class Command(BaseCommand):
    # define logic of command
    def handle(self, *args, **options):
        try:
            # save in db
            Main.objects.create(
            ticker="test",
            open_price=100.10,
            low_price=99.95,
            profit=-1.0,
            risk=1.05,
            new_candidate="ticker"
            )
        except:
            print('error')

        self.stdout.write( 'job complete' )
