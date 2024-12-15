CREATE TABLE Movies ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        moviename TEXT NOT NULL,
        code INTEGER NOT NULL,
        comment TEXT NOT NULL);

INSERT INTO Movies(moviename, code, comment)VALUES
           ('pianist', '423' , 'I love this movie'),
           ('fallenangels', '11220', 'I love this movie'),
           ('lahaine', '406', 'I love this movie'),
           ('duvidha', '103931', 'I love this movie'),
           ('pastlives', '666277', 'I love this movie'),
           ('tenet', '577922', 'I love this movie'),
           ('joker', '475557', 'I love this movie'),
           ('darkknight', '155', 'I love this movie'),
           ('forrestgump', '13', 'I love this movie');
