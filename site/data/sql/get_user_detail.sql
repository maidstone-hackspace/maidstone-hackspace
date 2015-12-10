select users.id as user_id, members.id as member_id, username, first_name, last_name, email, users.profile_image, last_login, description, skills
    from users
    left join members on users.id=members.user_id
    left join user_detail on users.id = user_detail.user_id
