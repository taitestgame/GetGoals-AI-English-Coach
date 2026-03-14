import 'package:flutter/material.dart';
class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});
  @override
  Widget build(BuildContext context) {
    Future.delayed(const Duration(seconds: 2), () {
      // Navigate to onboarding or home
    });
    return const Scaffold(body: Center(child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [Icon(Icons.school, size: 80, color: Color(0xFF4F46E5)), SizedBox(height: 16), Text('GetGoals', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold))])));
  }
}
