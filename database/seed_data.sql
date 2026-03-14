-- GetGoals Seed Data
USE GetGoals;
GO

-- Insert admin user (password: Admin@123)
INSERT INTO users (email, full_name, hashed_password, role, english_level)
VALUES ('admin@getgoals.com', 'Admin User', '$2b$12$LJ3m6pVbBOAoFn0hPzLwOeF/K8cLqoJqzqKF4RJvH5B/5RKrd8S2K', 'admin', 'C2');

-- Insert sample lessons
INSERT INTO lessons (title, description, level, category, duration_minutes, order_index, is_published) VALUES
('Basic Greetings', 'Learn common English greetings and introductions', 'A1', 'vocabulary', 20, 1, 1),
('Present Simple Tense', 'Master the present simple tense', 'A1', 'grammar', 30, 2, 1),
('Daily Routines', 'Vocabulary and phrases for daily activities', 'A1', 'vocabulary', 25, 3, 1),
('Past Simple Tense', 'Learn to talk about past events', 'A2', 'grammar', 30, 4, 1),
('Reading Comprehension A2', 'Practice reading short texts', 'A2', 'reading', 35, 5, 1),
('Intermediate Grammar', 'Conditional sentences and more', 'B1', 'grammar', 40, 6, 1);

-- Insert sample roadmaps
INSERT INTO roadmaps (title, description, target_level, estimated_days, milestones) VALUES
('Beginner to Elementary', 'A1 to A2 learning path', 'A2', 30, '["Complete basic vocabulary","Master present tenses","Learn past tenses","Pass A2 assessment"]'),
('Elementary to Intermediate', 'A2 to B1 learning path', 'B1', 45, '["Expand vocabulary","Learn conditional sentences","Improve reading","Pass B1 assessment"]'),
('Intermediate to Upper', 'B1 to B2 learning path', 'B2', 60, '["Advanced grammar","Academic writing","Listening practice","Pass B2 assessment"]');
