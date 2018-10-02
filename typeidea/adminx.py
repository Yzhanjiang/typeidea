#!/usr/bin/env python 
#coding:utf8
import  xadmin
from xadmin.views import CommAdminView

class BaseOwnerAdmin(object):
    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin,self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(owner=request.user)

    def save(self):
        if self.org_obj:
            return self(BaseOwnerAdmin,self).save_models()

        self.new_obj.owner = self.request.user
        return self(BaseOwnerAdmin,self).save_models()


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(CommAdminView):
    site_title = "Typeidea管理后台"
    site_footer = "@ power by zhan"
    menu_style = "accordion"



xadmin.site.register(CommAdminView,GlobalSetting)