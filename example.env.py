# pylint: skip-file
# flake8: noqa: E501
''' 
This file should be renamed to env.py and make sure env.py is added to your .gitignore
to keep it out off version control.
This should never shared with anyone since it will hold your secret information
'''

import os
# Secret config
os.environ['DATABASE_URL'] = ' Input Database api keys here '
os.environ['SECRET_KEY'] = ' Make a secure secret key '
os.environ["CLOUDINARY_URL"] = ' Uri/key for cloudinary '

# email
os.environ['EMAIL_HOST_PASS'] = ' input your email host password '
os.environ['EMAIL_HOST_USER'] = ' input your email host address '

# Stripe
os.environ['STRIPE_CURRENCY'] = ' Input your currecy code you want to use '
os.environ['STRIPE_PUBLIC_KEY'] = '  Input your Stripe public key here '
os.environ['STRIPE_SECRET_KEY'] = ' Input your Sripe Secret key here '

# debug settings,
#  Having anything inside the quotes will result in a True, Left empty results in a false
# Example, 
# os.environ['DEBUG'] = 'x' is true
# os.environ['DEBUG'] = '' is false
# also removing these lines will result in a false
os.environ['DEBUG'] = 'x'
os.environ['DEBUG_DATABASE'] = 'x'