from __future__ import absolute_import

from ipsilon.providers.openidc.plugins.common import OpenidCExtensionBase


class OpenidCExtension(OpenidCExtensionBase):
    name = 'rocky'
    display_name = 'Rocky Tokens'
    scopes = {
        'openid': {
            'display_name': 'openid',
        },
        'profile': {
            'display_name': 'profile',
        },
        'email': {
            'display_name': 'email',
        },
        'address': {
            'display_name': 'address',
        },
        'phone': {
            'display_name': 'phone',
        },
        'https://mbs.rockylinux.org/oidc/mbs-submit-build': {
            'display_name': 'mbs',
        },
        'https://id.fedoraproject.org/scope/groups': {
            'display_name': 'groups',
        }
    }
