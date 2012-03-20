from trans.management.commands import UnitCommand
from optparse import make_option

class Command(UnitCommand):
    help = 'updates checks for units'

    def handle(self, *args, **options):
        base = self.get_units(*args, **options)

        if base.count() == 0:
            return

        for unit in base.iterator():
            unit.check()
