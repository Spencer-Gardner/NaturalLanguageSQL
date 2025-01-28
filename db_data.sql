INSERT INTO student (student_id, name, birth_date, major) VALUES
(1, 'Alice Johnson', '2002-05-14', 'Computer Science'),
(2, 'Brian Smith', '2001-08-22', 'Mathematics'),
(3, 'Catherine Lee', '2003-02-10', 'Physics'),
(4, 'David Brown', '2000-11-30', 'History'),
(5, 'Emma Davis', '2002-07-25', 'Biology'),
(6, 'Frank Wilson', '2001-04-18', 'Economics');

INSERT INTO professor (professor_id, name, department) VALUES
(1, 'Dr. John Miller', 'Computer Science'),
(2, 'Dr. Susan White', 'Mathematics'),
(3, 'Dr. Mark Harris', 'Physics'),
(4, 'Dr. Linda Carter', 'History'),
(5, 'Dr. Robert Lewis', 'Biology');

INSERT INTO course (course_id, course_name, department, professor_id) VALUES
(1, 'Introduction to Programming', 'Computer Science', 1),
(2, 'Data Structures', 'Computer Science', 1),
(3, 'Calculus I', 'Mathematics', 2),
(4, 'General Physics', 'Physics', 3),
(5, 'World History', 'History', 4),
(6, 'Genetics', 'Biology', 5);

INSERT INTO enrollment (student_id, course_id, grade) VALUES
(1, 1, 'A'),
(1, 2, 'B+'),
(2, 3, 'A-'),
(3, 4, 'B'),
(4, 5, 'A'),
(5, 6, 'B+'),
(6, 1, 'A'),
(6, 3, 'B');

INSERT INTO classroom (classroom_id, building, room_number) VALUES
(1, 'Science Hall', '101'),
(2, 'Engineering Building', '202'),
(3, 'Mathematics Center', '303'),
(4, 'Liberal Arts Hall', '404'),
(5, 'Biology Wing', '505');

INSERT INTO course_schedule (course_id, classroom_id, day_of_week, start_time, end_time) VALUES
(1, 2, 'Monday', '09:00:00', '10:30:00'),
(2, 2, 'Wednesday', '10:00:00', '11:30:00'),
(3, 3, 'Tuesday', '14:00:00', '15:30:00'),
(4, 1, 'Thursday', '08:30:00', '10:00:00'),
(5, 4, 'Friday', '11:00:00', '12:30:00'),
(6, 5, 'Monday', '13:00:00', '14:30:00');
