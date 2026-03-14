import 'package:flutter/material.dart';
class LessonProvider extends ChangeNotifier {
  List<dynamic> _lessons = [];
  bool _isLoading = false;
  List<dynamic> get lessons => _lessons;
  bool get isLoading => _isLoading;
  void setLessons(List<dynamic> lessons) { _lessons = lessons; notifyListeners(); }
}
