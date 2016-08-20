select users.id as user_id, status, email, first_name, last_name, users.profile_image, description, skills
    from users 
    left join user_detail on user_detail.user_id=users.id 
