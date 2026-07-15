-- Write your query below
SELECT student_id, exam_id, score
FROM exam_results e
WHERE (student_id, score) IN (
    SELECT student_id, MAX(score)
    FROM exam_results
    GROUP BY student_id
)
AND exam_id = (
    SELECT MIN(exam_id)
    FROM exam_results e2
    WHERE e2.student_id = e.student_id
      AND e2.score = e.score
)
ORDER BY student_id;
