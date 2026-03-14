import 'package:flutter/material.dart';
class RoadmapProvider extends ChangeNotifier {
  Map<String, dynamic>? _roadmap;
  Map<String, dynamic>? get roadmap => _roadmap;
  void setRoadmap(Map<String, dynamic> roadmap) { _roadmap = roadmap; notifyListeners(); }
}
