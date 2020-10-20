#!/usr/bin/env python
#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


from models import User
def insert_User():
    models.User.objects.create(user_id=1, phone="123", mail="123", name="123", password="123",gender=0)
    
    


if __name__ == "__main__":
    main()
    print('Done!')
