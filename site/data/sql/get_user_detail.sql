select users.id as user_id, members.id as member_id, user_detail.id as user_detail_id,  username, first_name, last_name, status, email, users.profile_image, last_login, description, skills
    from users
    left join members on users.id=members.user_id
    left join user_detail on users.id = user_detail.user_id
