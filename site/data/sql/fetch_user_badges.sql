select users.id as user_id, user_detail.id as user_detail_id,  username, first_name, last_name, status, email, users.profile_image, last_login, description, skills
    from users
    join user_badges on users.id=user_badges.user_id
