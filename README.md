Ilhasoft Carrier
=====================

Library consultation phone carriers around the world.


Install
--------

    pip install ilhasoft-carriers


Usage
--------

    from carrier import Carrier

    c = Carrier()
    objects = c.get_search('iso', 'BR')  # Return all carriers for iso code BR
    objects = c.get_search('mcc', '724')  # Return all carriers for mcc 724
    objects = c.get_search('country_code', '55')  # Return all carriers for Country Code 55

