import 'api_service.dart';
class AIServiceMobile {
  final ApiService _api = ApiService();
  Future<dynamic> predictLevel(Map<String, dynamic> data) async => await _api.post('/ai/predict-level', data);
  Future<dynamic> getRecommendation() async => await _api.get('/ai/recommendation');
  Future<dynamic> getWeakSkills() async => await _api.get('/ai/weak-skills');
}
