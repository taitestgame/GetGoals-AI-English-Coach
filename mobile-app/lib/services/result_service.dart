import 'api_service.dart';
class ResultService {
  final ApiService _api = ApiService();
  Future<List<dynamic>> getMyResults() async => await _api.get('/results');
  Future<dynamic> getSummary() async => await _api.get('/results/summary/me');
}
