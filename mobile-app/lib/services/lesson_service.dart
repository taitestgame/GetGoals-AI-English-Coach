import 'api_service.dart';
class LessonService {
  final ApiService _api = ApiService();
  Future<List<dynamic>> getAll() async => await _api.get('/lessons');
  Future<dynamic> getById(int id) async => await _api.get('/lessons/$id');
}
