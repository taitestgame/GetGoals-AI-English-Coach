-- GetGoals Database Views
USE GetGoals;
GO

-- User dashboard view
CREATE VIEW vw_UserDashboard AS
SELECT
    u.id AS user_id,
    u.full_name,
    u.email,
    u.english_level,
    COUNT(DISTINCT r.id) AS total_quizzes,
    ISNULL(AVG(r.score), 0) AS avg_score,
    ISNULL(MAX(r.score), 0) AS best_score,
    COUNT(DISTINCT sh.lesson_id) AS lessons_completed,
    (SELECT COUNT(*) FROM user_roadmaps ur WHERE ur.user_id = u.id AND ur.status = 'active') AS active_roadmaps
FROM users u
LEFT JOIN results r ON u.id = r.user_id
LEFT JOIN study_history sh ON u.id = sh.user_id AND sh.activity_type = 'lesson_completed'
GROUP BY u.id, u.full_name, u.email, u.english_level;
GO

-- Lesson overview view
CREATE VIEW vw_LessonOverview AS
SELECT
    l.id,
    l.title,
    l.level,
    l.category,
    l.duration_minutes,
    l.is_published,
    COUNT(DISTINCT q.id) AS quiz_count,
    COUNT(DISTINCT sh.user_id) AS student_count
FROM lessons l
LEFT JOIN quizzes q ON l.id = q.lesson_id
LEFT JOIN study_history sh ON l.id = sh.lesson_id
GROUP BY l.id, l.title, l.level, l.category, l.duration_minutes, l.is_published;
GO
