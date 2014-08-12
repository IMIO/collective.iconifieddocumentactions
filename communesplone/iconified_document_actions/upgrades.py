# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def cleanup_skins_and_css(context):
    context.runImportStepFromProfile(
        'profile-communesplone.iconified_document_actions:default', 'cssregistry')
    portal = getToolByName(context, 'portal_url').getPortalObject()
    # remove old registered skin
    if hasattr(portal.portal_skins, 'iconified_document_actions_styles'):
        portal.portal_skins.manage_delObjects(ids=['iconified_document_actions_styles', ])
    # remove old registered CSS, does not fail if resource not exists
    portal.portal_css.unregisterResource('iconified_document_actions.css')
