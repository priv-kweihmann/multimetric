import 'dart:io';

main(List<String> args) {

  if (args.isEmpty || args[0].isEmpty) {
    print("Usage: please provide a string");
    /* Just another comment */
    exit(1);
  }

  // Commment
  print(capitalize(args[0]));
}

String capitalize(String input) =>
    '${input[0].toUpperCase()}${input.substring(1)}';
