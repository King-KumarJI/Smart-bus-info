create table if not exists bus_info{
    bus_id int PRIMARY KEY,
    route_name VARCHAR (100),
    current_stop VARCHAR(100),
    next_stop VARCHAR(100),
    eta INT,
    depot VARCHAR(50)
}
