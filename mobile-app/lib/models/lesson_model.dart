class LessonModel {
  final int id;
  final String title;
  final String? description;
  final String level;
  final String? category;
  final int durationMinutes;

  LessonModel({required this.id, required this.title, this.description, required this.level, this.category, this.durationMinutes = 30});

  factory LessonModel.fromJson(Map<String, dynamic> json) => LessonModel(
    id: json['id'], title: json['title'], description: json['description'],
    level: json['level'], category: json['category'], durationMinutes: json['duration_minutes'] ?? 30,
  );
}
