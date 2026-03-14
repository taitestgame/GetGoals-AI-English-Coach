import 'package:flutter/material.dart';
class RoadmapCard extends StatelessWidget {
  final String title;
  final String targetLevel;
  final int estimatedDays;
  const RoadmapCard({super.key, required this.title, required this.targetLevel, required this.estimatedDays});
  @override
  Widget build(BuildContext context) { return Card(child: Padding(padding: const EdgeInsets.all(16), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Text(title, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)), Text('Target: $targetLevel'), Text('Est. $estimatedDays days')]))); }
}
