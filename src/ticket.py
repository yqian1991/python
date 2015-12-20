# -*- coding:utf-8 -*-
from splinter.browser import Browser
b = Browser(driver_name="chrome")
url = "https://kyfw.12306.cn/otn/leftTicket/init"
b.visit(url)
b.find_by_text(u"登录").click()
b.fill("loginUserDTO.user_name","qianyu668899")
b.fill("userDTO.password","qsjy81zwxy")
b.cookies.all()
b.cookies.add({"_jc_save_fromStation":u"上海"})
b.cookies.add({"_jc_save_fromDate":"2016-02-01"})
b.cookies.add({u'_jc_save_toStation':u'南昌'})
b.cookies.all()
b.reload()
b.find_by_text(u"查询").click()
