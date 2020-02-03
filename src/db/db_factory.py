from .file_system_db import FileSystemDb


class DbFactory(object):
    def get_db(self, db_type, *db_target):
        print(db_type)
        return FileSystemDb(*db_target)
