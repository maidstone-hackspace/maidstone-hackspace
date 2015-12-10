table_name, column_name, column_type, default
#requests
ALTER TABLE requests ADD COLUMN description varchar(255) NULL ;
ALTER TABLE requests CHANGE COLUMN description description varchar(255) NULL ;
ALTER TABLE requests ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE requests CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE requests ADD COLUMN name varchar(45) NULL ;
ALTER TABLE requests CHANGE COLUMN name name varchar(45) NULL ;
ALTER TABLE requests ADD COLUMN price decimal(10,2) NULL ;
ALTER TABLE requests CHANGE COLUMN price price decimal(10,2) NULL ;
ALTER TABLE requests ADD COLUMN url varchar(255) NULL ;
ALTER TABLE requests CHANGE COLUMN url url varchar(255) NULL ;
ALTER TABLE requests ADD COLUMN user_id int(10) unsigned ;
ALTER TABLE requests CHANGE COLUMN user_id user_id int(10) unsigned ;


#users
ALTER TABLE users ADD COLUMN created timestamp NULL ;
ALTER TABLE users CHANGE COLUMN created created timestamp NULL ;
ALTER TABLE users ADD COLUMN email varchar(255) NULL ;
ALTER TABLE users CHANGE COLUMN email email varchar(255) NULL ;
ALTER TABLE users ADD COLUMN first_name varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN first_name first_name varchar(45) NULL ;
ALTER TABLE users ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) ;
ALTER TABLE users CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) ;
ALTER TABLE users ADD COLUMN last_login varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN last_login last_login varchar(45) NULL ;
ALTER TABLE users ADD COLUMN last_name varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN last_name last_name varchar(45) NULL ;
ALTER TABLE users ADD COLUMN member_reference int(5) unsigned zerofill AUTO_INCREMENT ;
ALTER TABLE users CHANGE COLUMN member_reference member_reference int(5) unsigned zerofill AUTO_INCREMENT ;
ALTER TABLE users ADD COLUMN password varchar(160) NULL ;
ALTER TABLE users CHANGE COLUMN password password varchar(160) NULL ;
ALTER TABLE users ADD COLUMN profile_image varchar(255) NULL ;
ALTER TABLE users CHANGE COLUMN profile_image profile_image varchar(255) NULL ;
ALTER TABLE users ADD COLUMN status tinyint(2) NULL DEFAULT 0;
ALTER TABLE users CHANGE COLUMN status status tinyint(2) NULL DEFAULT 0;
ALTER TABLE users ADD COLUMN username varchar(25) ;
ALTER TABLE users CHANGE COLUMN username username varchar(25) ;


#user_detail
ALTER TABLE user_detail ADD COLUMN description text NULL ;
ALTER TABLE user_detail CHANGE COLUMN description description text NULL ;
ALTER TABLE user_detail ADD COLUMN id int(11)  PRIMARY KEY (`id`) ;
ALTER TABLE user_detail CHANGE COLUMN id id int(11)  PRIMARY KEY (`id`) ;
ALTER TABLE user_detail ADD COLUMN image varchar(45) NULL ;
ALTER TABLE user_detail CHANGE COLUMN image image varchar(45) NULL ;
ALTER TABLE user_detail ADD COLUMN member_id int(5) unsigned zerofill ;
ALTER TABLE user_detail CHANGE COLUMN member_id member_id int(5) unsigned zerofill ;
ALTER TABLE user_detail ADD COLUMN profile_image varchar(255) NULL ;
ALTER TABLE user_detail CHANGE COLUMN profile_image profile_image varchar(255) NULL ;
ALTER TABLE user_detail ADD COLUMN skills varchar(255) NULL ;
ALTER TABLE user_detail CHANGE COLUMN skills skills varchar(255) NULL ;
ALTER TABLE user_detail ADD COLUMN user_id int(11) unsigned ;
ALTER TABLE user_detail CHANGE COLUMN user_id user_id int(11) unsigned ;


#user_password_reset
ALTER TABLE user_password_reset ADD COLUMN created timestamp NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE user_password_reset CHANGE COLUMN created created timestamp NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE user_password_reset ADD COLUMN id int(11)  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_password_reset CHANGE COLUMN id id int(11)  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_password_reset ADD COLUMN reset_code varchar(160) ;
ALTER TABLE user_password_reset CHANGE COLUMN reset_code reset_code varchar(160) ;
ALTER TABLE user_password_reset ADD COLUMN user_id int(11) ;
ALTER TABLE user_password_reset CHANGE COLUMN user_id user_id int(11) ;


