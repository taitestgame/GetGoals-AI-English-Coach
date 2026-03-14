class RoadmapModel {
  final int id;
  final String title;
  final String? description;
  final String targetLevel;
  final int estimatedDays;
  final double progress;

  RoadmapModel({required this.id, required this.title, this.description, required this.targetLevel, this.estimatedDays = 30, this.progress = 0});

  factory RoadmapModel.fromJson(Map<String, dynamic> json) => RoadmapModel(
    id: json['id'], title: json['title'], description: json['description'],
    targetLevel: json['target_level'], estimatedDays: json['estimated_days'] ?? 30, progress: (json['progress'] ?? 0).toDouble(),
  );
}
