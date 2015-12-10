table_name, column_name, column_type, default
#requests


#users
ALTER TABLE users ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE users ADD INDEX member_reference_UNIQUE (member_reference ASC);
ALTER TABLE users ADD INDEX email_UNIQUE (email ASC);


#user_detail
ALTER TABLE user_detail ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_detail ADD INDEX user_id_UNIQUE (user_id ASC);
ALTER TABLE user_detail ADD INDEX member_id_UNIQUE (member_id ASC);


#user_password_reset
ALTER TABLE user_password_reset ADD INDEX id_UNIQUE (id ASC);
ALTER TABLE user_password_reset ADD INDEX user_id_UNIQUE (user_id ASC);
ALTER TABLE user_password_reset ADD INDEX password_UNIQUE (reset_code ASC);


