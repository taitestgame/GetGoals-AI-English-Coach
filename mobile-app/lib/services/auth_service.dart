import 'api_service.dart';

class AuthService {
  final ApiService _api = ApiService();

  Future<Map<String, dynamic>> login(String email, String password) async {
    return await _api.post('/auth/login', {'email': email, 'password': password});
  }

  Future<Map<String, dynamic>> register(String email, String fullName, String password) async {
    return await _api.post('/auth/register', {'email': email, 'full_name': fullName, 'password': password});
  }
}
