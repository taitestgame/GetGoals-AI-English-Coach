class UserModel {
  final int id;
  final String email;
  final String fullName;
  final String? avatarUrl;
  final String role;
  final String? englishLevel;
  final String authProvider;

  UserModel({required this.id, required this.email, required this.fullName, this.avatarUrl, required this.role, this.englishLevel, this.authProvider = 'local'});

  factory UserModel.fromJson(Map<String, dynamic> json) => UserModel(
    id: json['id'], email: json['email'], fullName: json['full_name'],
    avatarUrl: json['avatar_url'], role: json['role'], englishLevel: json['english_level'],
    authProvider: json['auth_provider'] ?? 'local',
  );
}
