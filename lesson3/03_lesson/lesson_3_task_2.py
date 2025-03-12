from smartphone import Smartphone
catalog = [Smartphone ("Nokia","Fonarik", "9999999999"),
            Smartphone ("Samsung", "Galaxy","91111111111"),
            Smartphone ("iPhone","XR","98888888888")]
for Smartphone in catalog:
    print (Smartphone.vendor, "-", Smartphone.model,".",Smartphone.num)
