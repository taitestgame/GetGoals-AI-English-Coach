-- GetGoals Stored Procedures
USE GetGoals;
GO

-- Get user progress summary
CREATE PROCEDURE sp_GetUserProgress
    @UserId INT
AS
BEGIN
    SELECT
        u.id AS user_id,
        u.full_name,
        u.english_level,
        COUNT(DISTINCT r.quiz_id) AS quizzes_taken,
        AVG(r.score) AS avg_score,
        MAX(r.score) AS best_score,
        COUNT(DISTINCT sh.lesson_id) AS lessons_completed
    FROM users u
    LEFT JOIN results r ON u.id = r.user_id
    LEFT JOIN study_history sh ON u.id = sh.user_id AND sh.activity_type = 'lesson_completed'
    WHERE u.id = @UserId
    GROUP BY u.id, u.full_name, u.english_level;
END;
GO

-- Get user skill scores
CREATE PROCEDURE sp_GetUserSkillScores
    @UserId INT
AS
BEGIN
    SELECT
        l.category AS skill,
        AVG(r.score) AS avg_score,
        COUNT(*) AS attempts
    FROM results r
    JOIN quizzes q ON r.quiz_id = q.id
    JOIN lessons l ON q.lesson_id = l.id
    WHERE r.user_id = @UserId
    GROUP BY l.category;
END;
GO

-- Get leaderboard
CREATE PROCEDURE sp_GetLeaderboard
    @Top INT = 10
AS
BEGIN
    SELECT TOP (@Top)
        u.id,
        u.full_name,
        u.english_level,
        AVG(r.score) AS avg_score,
        COUNT(*) AS total_quizzes
    FROM users u
    JOIN results r ON u.id = r.user_id
    GROUP BY u.id, u.full_name, u.english_level
    ORDER BY avg_score DESC;
END;
GO
