
APP_LABEL = 'permission_app'
MODEL = 'GeneralPermission'

CAN_VIEW_TESTING_PAGES_PERM_CODENAME = 'can_view_testing_pages'
CAN_VIEW_TESTING_PAGES_PERM = f'{APP_LABEL}.{CAN_VIEW_TESTING_PAGES_PERM_CODENAME}'

CAN_SUBMIT_CONTACT_CODENAME = 'can_submit_contact'
CAN_SUBMIT_CONTACT_PERM = f'{APP_LABEL}.{CAN_SUBMIT_CONTACT_CODENAME}'

GENERAL_PERMISSIONS = {
    CAN_VIEW_TESTING_PAGES_PERM: 'User can view testing pages',
    CAN_SUBMIT_CONTACT_PERM: 'User can submit contact'
}