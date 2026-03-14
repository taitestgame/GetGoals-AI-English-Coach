import 'package:flutter/material.dart';
import 'colors.dart';

class AppTheme {
  static ThemeData get lightTheme => ThemeData(
    colorSchemeSeed: AppColors.primary,
    useMaterial3: true,
    brightness: Brightness.light,
    fontFamily: 'Inter',
  );

  static ThemeData get darkTheme => ThemeData(
    colorSchemeSeed: AppColors.primary,
    useMaterial3: true,
    brightness: Brightness.dark,
    fontFamily: 'Inter',
  );
}
