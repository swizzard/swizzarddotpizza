__author__ = 'samuelraker'


class CacheRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ("django_cache",):
            return "main_cache"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ("django_cache",):
            return "main_cache"
        return None

    def allow_syncdb(self, db, model):
        if model._meta.app_label in ("django_cache",):
            return db == "main_cache"
        return None
