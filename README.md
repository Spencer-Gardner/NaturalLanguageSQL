# University DB

## Descrioption
This simple database models a university's structure, including students, professors, courses, enrollments, and classrooms.

## Diagram
<img width="607" alt="image" src="https://github.com/user-attachments/assets/8adb0bf4-1840-4fe7-bc83-4b334d877ce7" />

## Successful Query Example
**Question:** Which classroom is used the most based on scheduled courses?

```sql
SELECT classroom_id
FROM course_schedule
GROUP BY classroom_id
ORDER BY COUNT(course_id) DESC
LIMIT 1;
```

**Response:** Classroom 2 is used the most based on scheduled courses.

## Conclusion
I experimented with both zero-shot and single-domain query strategies using GPT-4o Mini. For both strategies, the model successfully answered all questions.
Though the answers were the same, I found that the responses provided by the single-domain strategy were more helpful and concise.
