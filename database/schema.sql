-- GetGoals Database Schema
-- SQL Server

CREATE DATABASE GetGoals;
GO
USE GetGoals;
GO

-- Users table
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email NVARCHAR(255) NOT NULL UNIQUE,
    full_name NVARCHAR(255) NOT NULL,
    hashed_password NVARCHAR(255) NULL,
    avatar_url NVARCHAR(500) NULL,
    role NVARCHAR(20) DEFAULT 'user',
    is_active BIT DEFAULT 1,
    auth_provider NVARCHAR(50) DEFAULT 'local',
    auth_provider_id NVARCHAR(255) NULL,
    english_level NVARCHAR(20) NULL,
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

-- Lessons table
CREATE TABLE lessons (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX) NULL,
    content NVARCHAR(MAX) NULL,
    level NVARCHAR(20) NOT NULL,
    category NVARCHAR(100) NULL,
    duration_minutes INT DEFAULT 30,
    order_index INT DEFAULT 0,
    is_published BIT DEFAULT 0,
    thumbnail_url NVARCHAR(500) NULL,
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

-- Quizzes table
CREATE TABLE quizzes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    lesson_id INT NULL FOREIGN KEY REFERENCES lessons(id),
    title NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX) NULL,
    level NVARCHAR(20) NOT NULL,
    quiz_type NVARCHAR(50) NOT NULL,
    questions NVARCHAR(MAX) NULL,
    time_limit_minutes INT DEFAULT 15,
    passing_score INT DEFAULT 60,
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

-- Results table
CREATE TABLE results (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL FOREIGN KEY REFERENCES users(id),
    quiz_id INT NOT NULL FOREIGN KEY REFERENCES quizzes(id),
    score FLOAT NOT NULL,
    total_questions INT NOT NULL,
    correct_answers INT NOT NULL,
    answers NVARCHAR(MAX) NULL,
    time_spent_seconds INT NULL,
    feedback NVARCHAR(500) NULL,
    created_at DATETIME2 DEFAULT GETDATE()
);

-- Study History table
CREATE TABLE study_history (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL FOREIGN KEY REFERENCES users(id),
    lesson_id INT NULL FOREIGN KEY REFERENCES lessons(id),
    quiz_id INT NULL FOREIGN KEY REFERENCES quizzes(id),
    activity_type NVARCHAR(50) NOT NULL,
    description NVARCHAR(MAX) NULL,
    duration_seconds INT NULL,
    created_at DATETIME2 DEFAULT GETDATE()
);

-- Roadmaps table
CREATE TABLE roadmaps (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX) NULL,
    target_level NVARCHAR(20) NOT NULL,
    estimated_days INT DEFAULT 30,
    milestones NVARCHAR(MAX) NULL,
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

-- User Roadmaps table
CREATE TABLE user_roadmaps (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL FOREIGN KEY REFERENCES users(id),
    roadmap_id INT NOT NULL FOREIGN KEY REFERENCES roadmaps(id),
    progress FLOAT DEFAULT 0,
    current_milestone INT DEFAULT 0,
    status NVARCHAR(20) DEFAULT 'active',
    started_at DATETIME2 DEFAULT GETDATE(),
    completed_at DATETIME2 NULL
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_results_user ON results(user_id);
CREATE INDEX idx_study_history_user ON study_history(user_id);
CREATE INDEX idx_user_roadmaps_user ON user_roadmaps(user_id);
