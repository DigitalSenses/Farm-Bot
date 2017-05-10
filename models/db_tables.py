# -*- coding: utf-8 -*-

db.define_table('PostReqs',
               Field('time_stamp','datetime'),
               Field('post_data','text'),
               )

db.define_table('BotUsers',
                Field('username','string'),
                Field('user_type','integer'),
                Field('fullname','string'),
                Field('register_time','datetime'),
                Field('about','text'),
                Field('stats','text'),
                Field('history','text'),
                Field('inventory','text'),
                Field('permissions','text')
                )

db.define_table('Items',
                Field('name','string'),
                Field('descript','string'),
                Field('name_e','string'),
                Field('descript_e','string'),
                Field('time_left','integer'),
                Field('turns_left','integer'),
                Field('flags','text'),
                Field('code_use','text'),
                Field('code_recieve','text'),
                Field('code_give','text'),
                Field('code_tick','text'),
                Field('code_post','text'),
                Field('code_stat','text')
                )
