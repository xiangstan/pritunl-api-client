import logging
from pritunl_scripts.auth import request
from pritunl_scripts.get_organization import get_organization
from pritunl_scripts.get_user import get_user
from pritunl_scripts.get_keys import get_key

def create_user(organization, username, useremail, usergroup):
    groups = usergroup.split(",")
    create = request('POST', '/user/{}'.format(get_organization(organization)), 
    template = {
        "auth_type": "saml",
        'name': username,
        'email': useremail,
        'disabled': False,
        "groups": groups
    })
    if create.status_code == 200:
        logging.info('User: {} created'.format(username))
    else:
        logging.warning(create.status_code)
    try:
        # get_key(organization, username)
        return logging.info('User created Successfully')
    except Exception as e:
        return logging.warning(e)
