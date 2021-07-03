REST_API = {
    "backup": {
        "download_file": "https://api.beget.com/api/backup/downloadFile",
        "download_mysql": "https://api.beget.com/api/backup/downloadMysql",
        "get_file_backup_list": "https://api.beget.com/api/backup/getFileBackupList",
        "get_file_list": "https://api.beget.com/api/backup/getFileList",
        "get_log": "https://api.beget.com/api/backup/getLog",
        "get_mysql_backup_list": "https://api.beget.com/api/backup/getMysqlBackupList",
        "get_mysql_list": "https://api.beget.com/api/backup/getMysqlList",
        "restore_file": "https://api.beget.com/api/backup/restoreFile",
        "restore_mysql": "https://api.beget.com/api/backup/restoreMysql"
    },
    "cron": {
        "add": "https://api.beget.com/api/cron/add",
        "change_hidden_state": "https://api.beget.com/api/cron/changeHiddenState",
        "delete": "https://api.beget.com/api/cron/delete",
        "edit": "https://api.beget.com/api/cron/edit",
        "get_email": "https://api.beget.com/api/cron/getEmail",
        "get_list": "https://api.beget.com/api/cron/getList",
        "set_email": "https://api.beget.com/api/cron/setEmail"
    },
    "dns": {
        "change_records": "https://api.beget.com/api/dns/changeRecords",
        "get_data": "https://api.beget.com/api/dns/getData"
    },
    "domain": {
        "add_directives": "https://api.beget.com/api/domain/addDirectives",
        "add_subdomain_virtual": "https://api.beget.com/api/domain/addSubdomainVirtual",
        "add_virtual": "https://api.beget.com/api/domain/addVirtual",
        "change_php_version": "https://api.beget.com/api/domain/changePhpVersion",
        "check_domain_to_register": "https://api.beget.com/api/domain/checkDomainToRegister",
        "delete": "https://api.beget.com/api/domain/delete",
        "delete_subdomain": "https://api.beget.com/api/domain/deleteSubdomain",
        "get_directives": "https://api.beget.com/api/domain/getDirectives",
        "get_list": "https://api.beget.com/api/domain/getList",
        "get_php_version": "http://api.beget.com/api/domain/getPhpVersion",
        "get_subdomain_list": "https://api.beget.com/api/domain/getSubdomainList",
        "get_zone_list": "https://api.beget.com/api/domain/getZoneList",
        "remove_directives": "https://api.beget.com/api/domain/removeDirectives"
    },
    "ftp": {
        "add": "https://api.beget.com/api/ftp/add",
        "change_password": "https://api.beget.com/api/ftp/changePassword",
        "delete": "https://api.beget.com/api/ftp/delete",
        "get_list": "https://api.beget.com/api/ftp/getList"
    },
    "mail": {
        "change_mailbox_password": "https://api.beget.com/api/mail/changeMailboxPassword",
        "change_mailbox_settings": "https://api.beget.com/api/mail/changeMailboxSettings",
        "clear_domain_mail": "https://api.beget.com/api/mail/clearDomainMail",
        "create_mailbox": "https://api.beget.com/api/mail/createMailbox",
        "drop_mailbox": "https://api.beget.com/api/mail/dropMailbox",
        "forward_list_add_mailbox": "https://api.beget.com/api/mail/forwardListAddMailbox",
        "forward_list_delete_mailbox": "https://api.beget.com/api/mail/forwardListDeleteMailbox",
        "forward_list_show": "https://api.beget.com/api/mail/forwardListShow",
        "get_mailbox_list": "https://api.beget.com/api/mail/getMailboxList",
        "set_domain_mail": "https://api.beget.com/api/mail/setDomainMail"
    },
    "mysql": {
        "add_access": "https://api.beget.com/api/mysql/addAccess",
        "add_db": "https://api.beget.com/api/mysql/addDb",
        "change_access_password": "https://api.beget.com/api/mysql/changeAccessPassword",
        "drop_access": "https://api.beget.com/api/mysql/dropAccess",
        "drop_db": "https://api.beget.com/api/mysql/dropDb",
        "get_list": "https://api.beget.com/api/mysql/getList"
    },
    "site": {
        "add": "https://api.beget.com/api/site/add",
        "delete": "https://api.beget.com/api/site/delete",
        "freeze": "https://api.beget.com/api/site/freeze",
        "get_list": "https://api.beget.com/api/site/getList",
        "is_site_frozen": "https://api.beget.com/api/site/isSiteFrozen",
        "link_domain": "https://api.beget.com/api/site/linkDomain",
        "unfreeze": "https://api.beget.com/api/site/unfreeze",
        "unlink_domain": "https://api.beget.com/api/site/unlinkDomain"
    },
    "stat": {
        "get_db_list_load": "https://api.beget.com/api/stat/getDbListLoad",
        "get_db_load": "https://api.beget.com/api/stat/getDbLoad",
        "get_site_list_load": "https://api.beget.com/api/stat/getSitesListLoad",
        "get_site_load": "https://api.beget.com/api/stat/getSiteLoad"
    },
    "user": {
        "get_account_info": "https://api.beget.com/api/user/getAccountInfo",
        "toggle_ssh": "https://api.beget.com/api/user/toggleSsh"
    }
}
