# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def cleanup_skins_and_css(context):
    context.runImportStepFromProfile(
        'profile-collective.iconifieddocumentactions:default', 'cssregistry')
    portal = getToolByName(context, 'portal_url').getPortalObject()
    # remove old registered skin
    if hasattr(portal.portal_skins, 'iconifieddocumentactions_styles'):
        portal.portal_skins.manage_delObjects(ids=['iconifieddocumentactions_styles', ])
    # remove old registered CSS, does not fail if resource not exists
    portal.portal_css.unregisterResource('iconifieddocumentactions.css')
