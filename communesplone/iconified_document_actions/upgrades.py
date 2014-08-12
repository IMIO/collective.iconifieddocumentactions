# -*- coding: utf-8 -*-


def remove_skins_directory(context):
    context.runImportStepFromProfile(
        'communesplone.iconified_document_actions:default', 'cssregistry')
    portal = context.getSite()
    portal.portal_skins.manage_delObjects(ids=['iconified_document_actions_styles', ])
