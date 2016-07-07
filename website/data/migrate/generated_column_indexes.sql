table_name, column_name, column_type, default
#badges
ALTER TABLE badges ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE badges ADD UNIQUE INDEX name_UNIQUE (name ASC);


#members
ALTER TABLE members ADD INDEX id_UNIQUE (id ASC);


#pledges
ALTER TABLE pledges ADD INDEX id_UNIQUE (id ASC);


#pledge_amounts
ALTER TABLE pledge_amounts ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE pledge_amounts ADD UNIQUE INDEX reference_UNIQUE (reference ASC);


#requests
ALTER TABLE requests ADD INDEX id_UNIQUE (id ASC);


#users
ALTER TABLE users ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE users ADD UNIQUE INDEX member_reference_UNIQUE (member_reference ASC);
ALTER TABLE users ADD UNIQUE INDEX email_UNIQUE (email ASC);


#user_badges
ALTER TABLE user_badges ADD INDEX id_UNIQUE (id ASC);


#user_detail
ALTER TABLE user_detail ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_detail ADD UNIQUE INDEX user_id_UNIQUE (user_id ASC);
ALTER TABLE user_detail ADD UNIQUE INDEX member_id_UNIQUE (member_id ASC);


#user_detail_lists
ALTER TABLE user_detail_lists ADD INDEX id_UNIQUE (id ASC);


#user_membership
ALTER TABLE user_membership ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_membership ADD UNIQUE INDEX subscription_id_UNIQUE (subscription_reference ASC);


#user_oauth
ALTER TABLE user_oauth ADD INDEX id_UNIQUE (id ASC);


