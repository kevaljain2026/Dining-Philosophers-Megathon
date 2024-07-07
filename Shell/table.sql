create table users (
  user_name varchar(30),
  window_distance int,
  seat_distance int,
  seat_angle int
);

insert into users values("Vansh", 4, 10, 60);
insert into users values("Keval", 4, 10, 120);

create table music_history (
    user_name varchar(30),
    song_name varchar(50),
    year int
);

insert into music_history values("Vansh", "Just the two of us", 1990);
insert into music_history values("Vansh", "Mr Blue Sky", 2018);
