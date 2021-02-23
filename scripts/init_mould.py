import base
from mould import models

def run()
    exists = models.Mould.objects.filter().exists()
    if not exists:
        models.Mould.objects.create(

        )
if __name__ == "__main__":
    run()