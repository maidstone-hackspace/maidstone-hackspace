select name, sum(pledge_amounts.amount) as total, target
    from pledges
    left join pledge_amounts on pledges.id=pledge_amounts.pledge_id 
