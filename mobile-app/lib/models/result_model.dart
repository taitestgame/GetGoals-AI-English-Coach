class ResultModel {
  final int id;
  final int quizId;
  final double score;
  final int totalQuestions;
  final int correctAnswers;
  final String? feedback;

  ResultModel({required this.id, required this.quizId, required this.score, required this.totalQuestions, required this.correctAnswers, this.feedback});

  factory ResultModel.fromJson(Map<String, dynamic> json) => ResultModel(
    id: json['id'], quizId: json['quiz_id'], score: json['score'].toDouble(),
    totalQuestions: json['total_questions'], correctAnswers: json['correct_answers'], feedback: json['feedback'],
  );
}
