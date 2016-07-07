table_name, column_name, column_type, default
#badges
ALTER TABLE badges ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE badges CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE badges ADD COLUMN name varchar(25) ;
ALTER TABLE badges CHANGE COLUMN name name varchar(25) ;


#members
ALTER TABLE members ADD COLUMN id int(5) unsigned zerofill  PRIMARY KEY (`id`) ;
ALTER TABLE members CHANGE COLUMN id id int(5) unsigned zerofill  PRIMARY KEY (`id`) ;
ALTER TABLE members ADD COLUMN user_id varchar(45) NULL ;
ALTER TABLE members CHANGE COLUMN user_id user_id varchar(45) NULL ;


#pledges
ALTER TABLE pledges ADD COLUMN expired tinyint(1) NULL DEFAULT 0;
ALTER TABLE pledges CHANGE COLUMN expired expired tinyint(1) NULL DEFAULT 0;
ALTER TABLE pledges ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE pledges CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE pledges ADD COLUMN name varchar(255) NULL ;
ALTER TABLE pledges CHANGE COLUMN name name varchar(255) NULL ;
ALTER TABLE pledges ADD COLUMN target decimal(10,2) unsigned NULL DEFAULT 0.00;
ALTER TABLE pledges CHANGE COLUMN target target decimal(10,2) unsigned NULL DEFAULT 0.00;
ALTER TABLE pledges ADD COLUMN total decimal(10,2) NULL DEFAULT 0.00;
ALTER TABLE pledges CHANGE COLUMN total total decimal(10,2) NULL DEFAULT 0.00;


#pledge_amounts
ALTER TABLE pledge_amounts ADD COLUMN amount decimal(10,2) NULL ;
ALTER TABLE pledge_amounts CHANGE COLUMN amount amount decimal(10,2) NULL ;
ALTER TABLE pledge_amounts ADD COLUMN environment tinyint(1) NULL DEFAULT 0;
ALTER TABLE pledge_amounts CHANGE COLUMN environment environment tinyint(1) NULL DEFAULT 0;
ALTER TABLE pledge_amounts ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE pledge_amounts CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE pledge_amounts ADD COLUMN pledge_id int(10) NULL ;
ALTER TABLE pledge_amounts CHANGE COLUMN pledge_id pledge_id int(10) NULL ;
ALTER TABLE pledge_amounts ADD COLUMN provider_id tinyint(4) NULL ;
ALTER TABLE pledge_amounts CHANGE COLUMN provider_id provider_id tinyint(4) NULL ;
ALTER TABLE pledge_amounts ADD COLUMN reference varchar(255) NULL ;
ALTER TABLE pledge_amounts CHANGE COLUMN reference reference varchar(255) NULL ;
ALTER TABLE pledge_amounts ADD COLUMN type int(11) DEFAULT 1;
ALTER TABLE pledge_amounts CHANGE COLUMN type type int(11) DEFAULT 1;
ALTER TABLE pledge_amounts ADD COLUMN user_id int(11) NULL ;
ALTER TABLE pledge_amounts CHANGE COLUMN user_id user_id int(11) NULL ;


#requests
ALTER TABLE requests ADD COLUMN description varchar(255) NULL ;
ALTER TABLE requests CHANGE COLUMN description description varchar(255) NULL ;
ALTER TABLE requests ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE requests CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE requests ADD COLUMN name varchar(45) NULL ;
ALTER TABLE requests CHANGE COLUMN name name varchar(45) NULL ;
ALTER TABLE requests ADD COLUMN price decimal(10,2) NULL ;
ALTER TABLE requests CHANGE COLUMN price price decimal(10,2) NULL ;
ALTER TABLE requests ADD COLUMN quantity int(11) NULL DEFAULT 1;
ALTER TABLE requests CHANGE COLUMN quantity quantity int(11) NULL DEFAULT 1;
ALTER TABLE requests ADD COLUMN url varchar(255) NULL ;
ALTER TABLE requests CHANGE COLUMN url url varchar(255) NULL ;
ALTER TABLE requests ADD COLUMN user_id int(10) unsigned NULL ;
ALTER TABLE requests CHANGE COLUMN user_id user_id int(10) unsigned NULL ;


#users
ALTER TABLE users ADD COLUMN created timestamp NULL ;
ALTER TABLE users CHANGE COLUMN created created timestamp NULL ;
ALTER TABLE users ADD COLUMN email varchar(255) ;
ALTER TABLE users CHANGE COLUMN email email varchar(255) ;
ALTER TABLE users ADD COLUMN first_name varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN first_name first_name varchar(45) NULL ;
ALTER TABLE users ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE users CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE users ADD COLUMN last_login varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN last_login last_login varchar(45) NULL ;
ALTER TABLE users ADD COLUMN last_name varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN last_name last_name varchar(45) NULL ;
ALTER TABLE users ADD COLUMN memberid varchar(45) NULL ;
ALTER TABLE users CHANGE COLUMN memberid memberid varchar(45) NULL ;
ALTER TABLE users ADD COLUMN member_reference int(5) unsigned zerofill ;
ALTER TABLE users CHANGE COLUMN member_reference member_reference int(5) unsigned zerofill ;
ALTER TABLE users ADD COLUMN password varchar(160) NULL ;
ALTER TABLE users CHANGE COLUMN password password varchar(160) NULL ;
ALTER TABLE users ADD COLUMN profile_image varchar(255) NULL ;
ALTER TABLE users CHANGE COLUMN profile_image profile_image varchar(255) NULL ;
ALTER TABLE users ADD COLUMN status tinyint(2) NULL DEFAULT 0;
ALTER TABLE users CHANGE COLUMN status status tinyint(2) NULL DEFAULT 0;
ALTER TABLE users ADD COLUMN username varchar(25) NULL ;
ALTER TABLE users CHANGE COLUMN username username varchar(25) NULL ;


#user_badges
ALTER TABLE user_badges ADD COLUMN badge_id int(10) unsigned ;
ALTER TABLE user_badges CHANGE COLUMN badge_id badge_id int(10) unsigned ;
ALTER TABLE user_badges ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_badges CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_badges ADD COLUMN user_id int(10) unsigned ;
ALTER TABLE user_badges CHANGE COLUMN user_id user_id int(10) unsigned ;


#user_detail
ALTER TABLE user_detail ADD COLUMN description text NULL ;
ALTER TABLE user_detail CHANGE COLUMN description description text NULL ;
ALTER TABLE user_detail ADD COLUMN id int(11)  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_detail CHANGE COLUMN id id int(11)  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_detail ADD COLUMN image varchar(45) NULL ;
ALTER TABLE user_detail CHANGE COLUMN image image varchar(45) NULL ;
ALTER TABLE user_detail ADD COLUMN member_id int(5) unsigned zerofill NULL ;
ALTER TABLE user_detail CHANGE COLUMN member_id member_id int(5) unsigned zerofill NULL ;
ALTER TABLE user_detail ADD COLUMN profile_image varchar(255) NULL ;
ALTER TABLE user_detail CHANGE COLUMN profile_image profile_image varchar(255) NULL ;
ALTER TABLE user_detail ADD COLUMN skills varchar(255) NULL ;
ALTER TABLE user_detail CHANGE COLUMN skills skills varchar(255) NULL ;
ALTER TABLE user_detail ADD COLUMN user_id int(11) unsigned NULL ;
ALTER TABLE user_detail CHANGE COLUMN user_id user_id int(11) unsigned NULL ;


#user_detail_lists
ALTER TABLE user_detail_lists ADD COLUMN id int(11)  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_detail_lists CHANGE COLUMN id id int(11)  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_detail_lists ADD COLUMN text text NULL ;
ALTER TABLE user_detail_lists CHANGE COLUMN text text text NULL ;
ALTER TABLE user_detail_lists ADD COLUMN type varchar(10) NULL ;
ALTER TABLE user_detail_lists CHANGE COLUMN type type varchar(10) NULL ;
ALTER TABLE user_detail_lists ADD COLUMN user_id int(10) unsigned ;
ALTER TABLE user_detail_lists CHANGE COLUMN user_id user_id int(10) unsigned ;


#user_membership
ALTER TABLE user_membership ADD COLUMN amount decimal(10,2) DEFAULT 0.00;
ALTER TABLE user_membership CHANGE COLUMN amount amount decimal(10,2) DEFAULT 0.00;
ALTER TABLE user_membership ADD COLUMN id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_membership CHANGE COLUMN id id int(10) unsigned  PRIMARY KEY (`id`) AUTO_INCREMENT ;
ALTER TABLE user_membership ADD COLUMN join_date datetime NULL ;
ALTER TABLE user_membership CHANGE COLUMN join_date join_date datetime NULL ;
ALTER TABLE user_membership ADD COLUMN provider_id tinyint(1) NULL ;
ALTER TABLE user_membership CHANGE COLUMN provider_id provider_id tinyint(1) NULL ;
ALTER TABLE user_membership ADD COLUMN status tinyint(1) ;
ALTER TABLE user_membership CHANGE COLUMN status status tinyint(1) ;
ALTER TABLE user_membership ADD COLUMN subscription_reference varchar(45) ;
ALTER TABLE user_membership CHANGE COLUMN subscription_reference subscription_reference varchar(45) ;
ALTER TABLE user_membership ADD COLUMN user_id int(10) unsigned ;
ALTER TABLE user_membership CHANGE COLUMN user_id user_id int(10) unsigned ;


