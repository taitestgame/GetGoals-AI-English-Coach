import 'api_service.dart';
class QuizService {
  final ApiService _api = ApiService();
  Future<List<dynamic>> getAll() async => await _api.get('/quizzes');
  Future<dynamic> submit(int quizId, Map<String, dynamic> data) async => await _api.post('/quizzes/$quizId/submit', data);
}
