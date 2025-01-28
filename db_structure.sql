CREATE TABLE student (
    student_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    birth_date DATE,
    major VARCHAR(50)
);

CREATE TABLE professor (
    professor_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(50)
);

CREATE TABLE course (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    professor_id INTEGER NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professor (professor_id)
);

CREATE TABLE enrollment (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student (student_id),
    FOREIGN KEY (course_id) REFERENCES course (course_id)
);

CREATE TABLE classroom (
    classroom_id INTEGER PRIMARY KEY,
    building VARCHAR(50) NOT NULL,
    room_number VARCHAR(10) NOT NULL
);

CREATE TABLE course_schedule (
    course_id INTEGER NOT NULL,
    classroom_id INTEGER NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    FOREIGN KEY (course_id) REFERENCES course (course_id),
    FOREIGN KEY (classroom_id) REFERENCES classroom (classroom_id)
);
