import 'package:flutter/material.dart';
class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}
class _RegisterScreenState extends State<RegisterScreen> {
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: const Text('Register')), body: Padding(padding: const EdgeInsets.all(24), child: Column(children: [
      TextField(controller: _nameController, decoration: const InputDecoration(labelText: 'Full Name')),
      const SizedBox(height: 16),
      TextField(controller: _emailController, decoration: const InputDecoration(labelText: 'Email')),
      const SizedBox(height: 16),
      TextField(controller: _passwordController, obscureText: true, decoration: const InputDecoration(labelText: 'Password')),
      const SizedBox(height: 24),
      ElevatedButton(onPressed: () {}, child: const Text('Register')),
    ])));
  }
}
