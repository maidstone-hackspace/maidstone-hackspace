table_name, column_name, column_type, default
#members
ALTER TABLE members ADD INDEX user_id_UNIQUE (user_id ASC);


#pledges
ALTER TABLE pledges ADD INDEX id_UNIQUE (id ASC);


#pledge_amounts
ALTER TABLE pledge_amounts ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE pledge_amounts ADD UNIQUE INDEX reference_UNIQUE (reference ASC);


#requests
ALTER TABLE requests ADD INDEX id_UNIQUE (id ASC);


#users
ALTER TABLE users ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE users ADD UNIQUE INDEX email_UNIQUE (email ASC);


#user_detail
ALTER TABLE user_detail ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_detail ADD UNIQUE INDEX user_id_UNIQUE (user_id ASC);
ALTER TABLE user_detail ADD UNIQUE INDEX member_id_UNIQUE (member_id ASC);


#user_password_reset
ALTER TABLE user_password_reset ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_password_reset ADD UNIQUE INDEX password_UNIQUE (reset_code ASC);
ALTER TABLE user_password_reset ADD UNIQUE INDEX user_id_UNIQUE (user_id ASC);


