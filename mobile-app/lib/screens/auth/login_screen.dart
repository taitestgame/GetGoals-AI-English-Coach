import 'package:flutter/material.dart';
class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}
class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Login')), body: Padding(padding: const EdgeInsets.all(24), child: Column(children: [
      TextField(controller: _emailController, decoration: const InputDecoration(labelText: 'Email')),
      const SizedBox(height: 16),
      TextField(controller: _passwordController, obscureText: true, decoration: const InputDecoration(labelText: 'Password')),
      const SizedBox(height: 24),
      ElevatedButton(onPressed: () {}, child: const Text('Login')),
    ])));
  }
}
