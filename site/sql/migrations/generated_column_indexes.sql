table_name, column_name, column_type, default
#badges
ALTER TABLE badges ADD INDEX name_UNIQUE (name ASC);


#members
ALTER TABLE members ADD UNIQUE INDEX user_id_UNIQUE (user_id ASC);


#pledges
ALTER TABLE pledges ADD INDEX id_UNIQUE (id ASC);


#pledge_amounts
ALTER TABLE pledge_amounts ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE pledge_amounts ADD INDEX reference_UNIQUE (reference ASC);


#requests
ALTER TABLE requests ADD UNIQUE INDEX id_UNIQUE (id ASC);


#users
ALTER TABLE users ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE users ADD INDEX member_reference_UNIQUE (member_reference ASC);
ALTER TABLE users ADD INDEX email_UNIQUE (email ASC);


#user_badges


#user_detail
ALTER TABLE user_detail ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_detail ADD INDEX user_id_UNIQUE (user_id ASC);
ALTER TABLE user_detail ADD INDEX member_id_UNIQUE (member_id ASC);


#user_detail_lists


#user_membership
ALTER TABLE user_membership ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_membership ADD INDEX subscription_id_UNIQUE (subscription_reference ASC);


